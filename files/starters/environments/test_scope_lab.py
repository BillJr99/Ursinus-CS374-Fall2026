"""test_scope_lab.py: the provided tests for the CS374 lab Environments and Type Checking.

Put this file next to your scope_lab.py and run, from that folder:

    python3 test_scope_lab.py            # all eleven tests
    python3 test_scope_lab.py --trace    # the tests, then the Step 1.4 trace program

The tests are numbered in the order you write the methods, so they pass one
at a time as you go:

    Part 1 (Environment)
     1. define writes into this scope's own table          (define)
     2. lookup finds a name here or in any enclosing scope (lookup)
     3. define in an inner scope shadows the outer binding (define + lookup)
     4. assign updates the nearest enclosing binding       (assign)
     5. assign to an undefined name raises, creating nothing
     6. leaving a block restores the outer bindings
    Part 2 (the checker)
     7. literals                                           (check_expr)
     8. variables, typed through the Part 1 scope table    (check_expr)
     9. arithmetic operators                               (check_expr)
    10. comparison and equality operators                  (check_expr)
    11. if and while conditions                            (check_condition)

A method you have not written yet shows up as a FAIL that says so, not as a
crash.  You never edit this file.
"""

import contextlib
import io
import sys
import unittest

try:
    from scope_lab import (Environment, LangError, LangNameError, LangTypeError,
                           Num, Str, BoolLit, Var, BinOp, Let, Print, Block, If,
                           While, Program, check, check_stmt, check_expr,
                           NUM, STR, BOOL)
except ImportError as exc:
    sys.exit(
        f"Could not import from scope_lab.py ({exc}).\n"
        "Run this script from the folder that holds scope_lab.py, and check that\n"
        "you have not renamed any class or function in the starter."
    )


class todo:
    """Turn a method that still raises NotImplementedError into a clean FAIL."""

    def __init__(self, test):
        self.test = test

    def __enter__(self):
        return self

    def __exit__(self, kind, exc, tb):
        if kind is NotImplementedError:
            raise self.test.failureException(
                f"not written yet: {exc} still raises NotImplementedError") from None
        return False


# ---------------------------------------------------------------------------
# Part 1: the scope table
# ---------------------------------------------------------------------------

class Part1Environment(unittest.TestCase):

    def test_01_define_writes_this_scope(self):
        """define stores the binding in this scope's own table and never touches the parent."""
        with todo(self):
            outer = Environment()
            outer.define("x", 2)
            inner = Environment(parent=outer)
            inner.define("x", 51)
            inner.define("flag", None)
        self.assertEqual(outer._bindings, {"x": 2}, "the outer table after define")
        self.assertEqual(inner._bindings, {"x": 51, "flag": None}, "the inner table after define")

    def test_02_lookup_walks_the_chain(self):
        """lookup checks this scope first, then each enclosing scope, then raises."""
        with todo(self):
            top = Environment()
            top.define("a", 1)
            mid = Environment(parent=top)
            mid.define("b", 2)
            bot = Environment(parent=mid)
            bot.define("c", 3)
            bot.define("nothing", None)
            self.assertEqual(bot.lookup("c"), 3, "a name bound in the current scope")
            self.assertEqual(bot.lookup("b"), 2, "a name bound one scope out")
            self.assertEqual(bot.lookup("a"), 1, "a name bound two scopes out")
            self.assertIsNone(bot.lookup("nothing"), "a name bound to None still counts as bound")
            with self.assertRaises(LangNameError) as caught:
                bot.lookup("nope")
        self.assertIsInstance(caught.exception, LangError)
        self.assertIn("nope", str(caught.exception), "the message must contain the name")

    def test_03_define_shadows(self):
        """An inner define hides the outer binding without changing it."""
        with todo(self):
            outer = Environment()
            outer.define("x", 2)
            inner = Environment(parent=outer)
            inner.define("x", 51)
            self.assertEqual(inner.lookup("x"), 51, "the inner x shadows the outer x")
            self.assertEqual(outer.lookup("x"), 2, "the outer x is unchanged")

    def test_04_assign_updates_nearest(self):
        """assign updates the nearest enclosing binding and never creates one."""
        with todo(self):
            outer = Environment()
            outer.define("y", 10)
            inner = Environment(parent=outer)
            inner.assign("y", 11)
            self.assertEqual(outer.lookup("y"), 11, "assign from the inner scope reached the outer y")
            self.assertNotIn("y", inner._bindings, "assign created a new y in the inner scope")
            top = Environment()
            top.define("y", 1)
            mid = Environment(parent=top)
            mid.define("y", 2)
            bot = Environment(parent=mid)
            bot.assign("y", 3)
            self.assertEqual(mid.lookup("y"), 3, "the nearest y (one scope out) changed")
            self.assertEqual(top.lookup("y"), 1, "the y two scopes out did not change")

    def test_05_assign_undefined_raises(self):
        """assign to a name no scope defines raises LangNameError and creates nothing."""
        with todo(self):
            outer = Environment()
            inner = Environment(parent=outer)
            with self.assertRaises(LangNameError) as caught:
                inner.assign("nope", 0)
            self.assertIn("nope", str(caught.exception), "the message must contain the name")
            self.assertNotIn("nope", inner._bindings, "the failed assign created a binding")
            self.assertNotIn("nope", outer._bindings, "the failed assign created a binding")

    def test_06_leaving_a_block_restores(self):
        """The shadowing program prints 51, 2, 11, and the block's names vanish with it."""
        out = io.StringIO()
        with todo(self):
            with contextlib.redirect_stdout(out):
                outer = Environment()                 # the program's top-level scope
                outer.define("x", 2)                  # let x = 2;
                outer.define("y", 10)                 # let y = 10;
                inner = Environment(parent=outer)     # {   enter the block
                inner.define("x", 51)                 #     let x = 51;
                inner.assign("y", 11)                 #     y = 11;
                inner.define("z", 99)                 #     let z = 99;
                print(inner.lookup("x"))              #     print x;
                del inner                             # }   leave the block
                print(outer.lookup("x"))              # print x;
                print(outer.lookup("y"))              # print y;
            with self.assertRaises(LangNameError):
                outer.lookup("z")                     # z lived only in the block
        self.assertEqual(out.getvalue().split(), ["51", "2", "11"])


# ---------------------------------------------------------------------------
# Part 2: the type checker
# ---------------------------------------------------------------------------

def let(name, typ, value, line=1):
    return Let(name, value, annotation=typ, line=line, col=1)


class Part2Checker(unittest.TestCase):

    def assertTypeError(self, program_or_expr, *must_contain, tenv=None):
        """The check raises LangTypeError whose message contains every given piece."""
        with self.assertRaises(LangTypeError) as caught:
            if isinstance(program_or_expr, Program):
                check(program_or_expr)
            else:
                check_expr(program_or_expr, tenv or Environment())
        text = str(caught.exception)
        for piece in must_contain:
            self.assertIn(piece, text, f"the error message {text!r} must contain {piece!r}")
        return text

    def test_07_literals(self):
        """Num is Num, Str is Str, BoolLit is Bool."""
        with todo(self):
            tenv = Environment()
            self.assertEqual(check_expr(Num(42), tenv), NUM)
            self.assertEqual(check_expr(Str("hi"), tenv), STR)
            self.assertEqual(check_expr(BoolLit(True), tenv), BOOL)

    def test_08_variables_use_the_scope_table(self):
        """A let binds its type in the Part 1 Environment; a Var looks it up; unknown is None."""
        with todo(self):
            tenv = Environment()
            check_stmt(let("x", NUM, Num(1)), tenv)
            self.assertEqual(tenv._bindings, {"x": NUM}, "the scope table holds the declared type")
            self.assertEqual(check_expr(Var("x"), tenv), NUM)
            inner = Environment(parent=tenv)
            check_stmt(let("x", STR, Str("inner")), inner)
            self.assertEqual(check_expr(Var("x"), inner), STR, "the inner x is a Str")
            self.assertEqual(check_expr(Var("x"), tenv), NUM, "the outer x is still a Num")
            self.assertIsNone(check_expr(Var("y"), tenv),
                              "an undeclared name has the unknown type None, not an error")
            self.assertTypeError(Program([let("x", NUM, Str("five"))]), "Num", "Str")

    def test_09_arithmetic(self):
        """+ - * / need two Nums and give Num; the error names both types and the position."""
        with todo(self):
            for op in ("+", "-", "*", "/"):
                self.assertEqual(check_expr(BinOp(op, Num(1), Num(2)), Environment()), NUM, op)
            text = self.assertTypeError(
                BinOp("+", Num(1, 1, 14), BoolLit(True, 1, 18), 1, 16), "'+'", "Num", "Bool")
            self.assertTrue(text.startswith("Type error at line 1, col 16"),
                            f"the error must sit at the operator's position, got {text!r}")
            self.assertEqual(check_expr(BinOp("*", Var("y"), Num(2)), Environment()), NUM,
                             "an unknown operand skips the check")

    def test_10_comparison_and_equality(self):
        """< <= > >= need two Nums and give Bool; == != need equal types and give Bool."""
        with todo(self):
            for op in ("<", "<=", ">", ">="):
                self.assertEqual(check_expr(BinOp(op, Num(1), Num(2)), Environment()), BOOL, op)
            self.assertTypeError(BinOp("<", Str("a"), Str("b"), 5, 13), "'<'", "Str", "line 5, col 13")
            self.assertEqual(check_expr(BinOp("==", Str("a"), Str("b")), Environment()), BOOL,
                             "two Strs may be compared with ==")
            self.assertTypeError(BinOp("!=", Num(1), Str("a"), 6, 13), "'!='", "Num", "Str")
            self.assertEqual(check_expr(BinOp("==", Var("y"), Num(1)), Environment()), BOOL,
                             "an unknown operand skips the check")

    def test_11_conditions(self):
        """The condition of an if or a while must be Bool."""
        with todo(self):
            body = Block([Print(Var("x"))])
            check(Program([let("x", NUM, Num(0)),
                           While(BinOp("<", Var("x"), Num(3)), body),
                           If(BoolLit(True), body, body)]))           # well typed: no error
            self.assertTypeError(Program([While(Num(1, 2, 7), body)]),
                                 "while", "Num", "line 2, col 7")
            self.assertTypeError(Program([If(Str("yes", 3, 4), body)]), "if", "Str")
            check(Program([If(Var("never_declared"), body)]))         # unknown: no error


# ---------------------------------------------------------------------------
# Step 1.4: the three-nested-block trace program, one call per numbered step.
# Run with:  python3 test_scope_lab.py --trace
# ---------------------------------------------------------------------------

PROGRAM = [
    "let x = 1;", "let y = 10;",
    "{", "let x = 2;", "y = y + x;",
    "{", "x = x * 10;", "let z = y;",
    "{", "let y = 0;", "z = z + x;", "print y;", "}",
    "print x;", "print z;", "}",
    "print x;", "}",
    "print x;", "print y;",
]


def _chain(env, names):
    parts = []
    while env is not None:
        bindings = ", ".join(f"{k}={v}" for k, v in env._bindings.items())
        parts.append(f"{names.get(id(env), '?')}{{{bindings}}}")
        env = env._parent
    return " -> ".join(parts)


def _value(env, text):
    """Evaluate a tiny expression: operands (names or integers) joined by + - * ."""
    words = text.split()
    total = _operand(env, words[0])
    for op, rhs in zip(words[1::2], words[2::2]):
        right = _operand(env, rhs)
        total = total + right if op == "+" else total - right if op == "-" else total * right
    return total


def _operand(env, word):
    return int(word) if word.lstrip("-").isdigit() else env.lookup(word)


def run_trace():
    """Run PROGRAM through your Environment, printing the chain and result at each step."""
    names, block_names = {}, iter("ABC")
    chain = [Environment()]
    names[id(chain[0])] = "top"
    printed = []
    print("Step 1.4 trace program:")
    for step, line in enumerate(PROGRAM, start=1):
        text = line.rstrip(";").strip()
        if text == "{":
            chain.append(Environment(parent=chain[-1]))
            names[id(chain[-1])] = next(block_names)
            result = f"enter {names[id(chain[-1])]}"
        elif text == "}":
            left = chain.pop()
            result = f"leave {names[id(left)]}"
        elif text.startswith("print "):
            value = chain[-1].lookup(text[6:].strip())
            printed.append(value)
            result = f"prints {value}"
        else:
            target, expr = (part.strip() for part in text.split("=", 1))
            value = _value(chain[-1], expr)
            if target.startswith("let "):
                chain[-1].define(target[4:].strip(), value)
                result = f"define {target[4:].strip()}={value}"
            else:
                chain[-1].assign(target, value)
                result = f"assign {target}={value}"
        print(f"step {step:>2}  {line:<12} {_chain(chain[-1], names):<46} {result}")
    print()
    print("The six printed values, in order:")
    for value in printed:
        print(value)


if __name__ == "__main__":
    want_trace = "--trace" in sys.argv
    argv = [arg for arg in sys.argv if arg != "--trace"]
    result = unittest.main(argv=argv, exit=False, verbosity=2).result
    if want_trace:
        print()
        part1_broken = any(test.id().split(".")[1] == "Part1Environment"
                           for test, _ in result.failures + result.errors)
        if not part1_broken:
            run_trace()
        else:
            print("Finish Part 1 (tests 1 to 6) before running the trace program.")
    sys.exit(0 if result.wasSuccessful() else 1)
