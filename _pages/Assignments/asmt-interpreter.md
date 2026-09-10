---
layout: assignment
permalink: /Assignments/Interpreter
title: "CS374: Principles of Programming Languages - The Interpreter"

info:
  coursenum: CS374
  purpose: "To complete your language pipeline with a tree-walking evaluator that has nested scopes, strong dynamic typing, a small static type checker, a REPL, and a precise semantics document.  This is the capstone component your team project extends."
  tilt:
    task: "Define AST node dataclasses with visitor dispatch, build a tree-walking evaluator with environments and short-circuit logic, add a REPL and file runner, implement a small static type checker over annotated declarations, and complete Part 5 in your choice of direction: Error Messages and SEMANTICS.md, or full Hindley-Milner Type Inference, or the Intcode VM."
    criteria: "I grade this on a correct evaluator with well-behaved scopes and short-circuit logic, a recoverable REPL and file runner, a working small static type checker that runs as its own stage before evaluation, and a complete Part 5 in your chosen direction (Error Messages and SEMANTICS.md, or full Hindley-Milner Type Inference, or the Intcode VM), weighted 25/30/15/15/15 across the five parts.  The Part 5 rubric applies equivalently to every direction.  See the rubric below for the full breakdown."
  points: 100
  goals:
    - To define a complete set of AST node dataclasses covering every language construct
    - To implement a tree-walking evaluator over the AST with strong dynamic typing
    - To implement nested scopes with an Environment class distinguishing definition from assignment
    - To verify semantic invariants (determinism, scope restoration, short-circuit non-evaluation) with property-based testing using Hypothesis and a generated program space
    - To build a REPL and file-runner with stage-identified error messages
    - To implement a small static type checker over annotated declarations (literal, variable, operator, and call-site checks) that runs as its own pipeline stage between parsing and evaluation
    - To make the language's semantics precise, by documenting the dynamic rules exhaustively in SEMANTICS.md, by extending the required checker to full Hindley-Milner type inference, or by implementing and precisely specifying a contrasting opcode-based execution model (the Intcode VM), in your choice of direction
  rubric:
    - weight: 25
      description: "AST Node Dataclasses (Goal 1: define a complete set of AST node dataclasses covering every language construct)"
      preemerging: Fewer than half the required node types are defined, or the dataclass structure does not match the parser's output
      beginning: All required node types exist but several are missing fields, have incorrect types, or lack documented field meanings
      progressing: All required node types are defined with correct fields and a useful __repr__, but source-position information is missing from most nodes
      proficient: All required node types are defined as dataclasses with every field documented and source-position (line/col) stored where it aids error reporting, meeting Goal 1 with a complete, parser-consistent node hierarchy and a visitor dispatch table or isinstance chain ready for the evaluator
    - weight: 30
      description: "Tree-Walking Evaluator (Goals 2-3: implement a tree-walking evaluator with strong dynamic typing and an Environment class for nested scopes)"
      preemerging: The evaluator fails to run or fails most provided programs because of major structural errors such as missing cases or infinite loops
      beginning: The evaluator runs but fails on several programs, e.g., nested scopes leak, type errors are not raised, or short-circuit logic always evaluates both branches
      progressing: The evaluator passes the provided programs but fails on hidden edge cases, e.g., a scope is not discarded after a block, or division by zero crashes Python instead of raising a language error
      proficient: A correct evaluator passes all provided and hidden programs; nested scopes behave per documented semantics, type errors name both operand types, short-circuit logic is verified by a non-evaluation test, and all runtime errors are raised at the language level with stage and position; the required Hypothesis invariant tests (Step 2e; determinism, scope restoration, short-circuit non-evaluation, and at least one more) pass over the generated program space, with one shrunk counterexample reported or a reasoned all-clear; and the control-flow theory questions are answered in the readme with the bomb test used as evidence, showing that Goals 2 and 3 are met
    - weight: 15
      description: "REPL and File Runner (Goal 4: build a REPL and file-runner with stage-identified error messages)"
      preemerging: Neither the REPL nor the file runner exists, or both crash on the first error
      beginning: One of the two exists but dies on any error, or the REPL does not maintain state between inputs
      progressing: Both exist and survive most errors, but one error class (e.g., type errors) still crashes the REPL, or the file runner does not identify the stage in its error messages
      proficient: Both the REPL and file runner work; the REPL maintains a persistent environment across inputs and recovers from all error classes, the file runner identifies stage and position in every error message, and a transcript demonstrates each error class and recovery, meeting Goal 4 end-to-end
    - weight: 15
      description: "The Small Static Type Checker (Goal 5: implement a static type checker over annotated declarations that runs as its own pipeline stage between parsing and evaluation)"
      preemerging: "No checker exists, or it never rejects an ill-typed program"
      beginning: "The checker rejects some ill-typed programs but misses operator mismatches or call-site errors, or it runs interleaved with evaluation rather than as its own stage"
      progressing: "The checker catches literal, variable, operator, and call-site errors as a separate stage, but error messages lack positions or do not name both conflicting types, or one construct (e.g., function return types) is unchecked"
      proficient: "The checker runs as its own stage between parsing and evaluation and rejects every ill-typed test program before any code runs; every type error is reported as \"Type error at line L, col C\" naming both conflicting types; annotated declarations, operator uses, call-site arity and argument types, and return types are all checked; and the file runner's staged output shows the Type stage firing before the Run stage"
    - weight: 15
      description: "Part 5, in the chosen direction: Staged Errors with SEMANTICS.md, full Hindley-Milner Type Inference, or the Intcode VM with a precise operational semantics (Goal 6: make the language's semantics precise, by documenting the dynamic rules exhaustively, extending the required checker to whole-program inference, or specifying and implementing a contrasting opcode-based execution model)"
      preemerging: "Dynamic-errors direction: errors are unhandled Python exceptions with no stage identification. Typing direction: no checker exists, or unification fails on basic cases. Intcode direction: the VM fails the Day 2 sample, or opcodes are not documented as transition rules"
      beginning: "Dynamic-errors direction: errors are caught but the stage (lexical vs. syntax vs. runtime) is not identified, or the position is absent. Typing direction: unification handles trivial cases but the checker fails on function application or let, or type errors carry no position. Intcode direction: the VM runs the Day 2 sample but parameter modes are wrong or INTCODE.md is incomplete"
      progressing: "Dynamic-errors direction: most error classes are caught with stage and position, but one class (e.g., type errors) is missing position or stage identification. Typing direction: the checker infers correct types for most programs with a defect in one case (e.g., a missing occurs check, or an incorrect constraint for one operator), and most type errors are positioned. Intcode direction: the VM passes the Day 2 and Day 5 checkpoints and most opcodes have transition rules, but position/immediate mode has a defect or the differential test against the tree-walker is missing"
      proficient: "Dynamic-errors direction: every error class (LexError, ParseError, NameError, TypeError, ZeroDivisionError) is caught at the appropriate stage and reported with a message of the form \"Stage error at line L, col C: description\"; SEMANTICS.md includes one example program that triggers each error class with the expected message shown. Typing direction: unification (with the occurs check) and Algorithm-W-style inference are correct for every construct the checker covers; the checker runs as its own stage before evaluation; every type error names both conflicting types with line and context; and TYPES.md states the typing rule per construct with one accepted and one rejected program each. Intcode direction: the VM passes every cited AoC checkpoint, illegal opcodes raise staged positioned errors, INTCODE.md gives a precise transition rule for every opcode and parameter mode, and the required differential test shows the VM and tree-walker agree on shared arithmetic. Any direction meets Goal 6 by providing a complete semantics reference"
  readings:
    - rtitle: "Tree-Walking Interpretation Activity"
      rlink: "Activities/liascript-interpretation.md"
      liapage: true
    - rtitle: "Environments Activity"
      rlink: "Activities/liascript-environments.md"
      liapage: true
    - rtitle: "Control Flow Semantics Activity"
      rlink: "Activities/liascript-controlflowsemantics.md"
      liapage: true
    - rtitle: "Property-Based Testing Your Language with Hypothesis (Tutorial)"
      rlink: "../Tutorials/PropertyBasedTesting"
    - rtitle: "Advent of Code 2019, Day 2: Intcode (Part 5 Intcode direction)"
      rlink: "https://adventofcode.com/2019/day/2"

tags:
  - interpreter
  - languages
  - pipeline
  - property-based-testing
  - virtual-machine

---

This assignment completes your pipeline with a tree-walking evaluator: a program that walks the abstract syntax tree (AST) your parser built and runs each node.  Your language gets real scopes, real types, a REPL (a read-eval-print loop, the interactive prompt), a static type checker, and a semantics document.  This is the component your team project extends, and the semantics document matters as much as the code does.  Build in the order below, since each part depends on the one before it.

---

## Before You Start

You need:

- Python 3.10 or newer.
- Your completed Lexer and Parser: `lexer.py`, `parser.py`, `ast_nodes.py`, and `token_spec.json`.  Import them unchanged, and note any bug fixes in your readme.
- The [Hypothesis]({{ site.baseurl }}/Tutorials/PropertyBasedTesting) library for Step 2e.
- A terminal and an editor.  If either is new to you, read the [dev environment page]({{ site.baseurl }}/Tutorials/DevEnvironment) and the [shell primer]({{ site.baseurl }}/Tutorials/ShellForLanguageDev) first.

**Reference parser and AST.**  The [reference parser and AST]({{ site.baseurl }}/files/reference/reference-parser.zip) are released with this assignment, and the zip also contains the reference lexer, so unzipping it gives you a complete pipeline up to parsing.  You may build on the reference parser or lexer instead of your own by declaring it in one line in your readme ("This submission uses the reference parser"); there is no penalty, and your Parser assignment grade stands unchanged.  The point of this assignment is the evaluator, and everyone deserves a solid tree to walk.

> **Do this.**
> 1. Create a project folder named `cs374-interpreter` and copy `lexer.py`, `parser.py`, `ast_nodes.py`, and `token_spec.json` into it (or unzip the reference parser there).
> 2. Create the deliverable files up front, so each part has a home:
>
> ```text
> interpreter.py        # evaluator, Environment, error hierarchy
> mylang.py             # entry point: file runner and REPL (Part 3)
> typechecker.py        # the small static type checker (Part 4)
> SEMANTICS.md          # the semantics document (Part 5)
> test_interpreter.py   # the test suite
> ```
>
> 3. From inside the folder, confirm your Python version and install Hypothesis:
>
> ```bash
> python3 --version
> pip install hypothesis
> ```
>
> 4. Confirm the pipeline is connected before you evaluate anything:
>
> ```bash
> python3 -c "from parser import parse; print(parse('print 1 + 2;'))"
> ```

> **You should see.** One line that is a `Program` tree.  With the reference parser it is exactly this; your own parser's field names may differ slightly.

```text
Program(stmts=[Print(value=BinOp(op='+', left=Num(value=1, line=1, col=7), right=Num(value=2, line=1, col=11), line=1, col=9), line=1)])
```

> **If it fails.**
> - `ModuleNotFoundError: No module named 'parser'`: you are not running from inside the project folder, or `parser.py` is not there.
> - `ImportError: cannot import name 'parse'`: your parser's entry point has a different name.  Use that name here and in `mylang.py`.
> - A `LexError` or `ParseError` on this one-line program: fix that stage first, or swap in the reference component.

> **Watch out.** If you import the reference `ast_nodes.py`, its nodes already carry both `line` and `col`.  Reconcile Step 1a against it rather than retyping it, and keep one set of node classes in the project; the evaluator dispatches on the exact classes the parser produced.

> **Time budget.** This is the longest assignment in the pipeline, and the course window matches it.  Plan steady work across every checkpoint in the pacing table rather than a final-week push.  Two pair labs land inside the window, each scoped to about two to three hours, and they finish pieces of Step 2c and Part 4 for you.

---

## Getting Started

### Your First 30 Minutes

Build the dispatch skeleton before any evaluation logic.  Once one statement flows through the entire pipeline on day one, the rest of Part 2 is filling in branches one at a time.

> **Do this.**
> 1. Copy the node dataclasses from Step 1a into `ast_nodes.py`, reconciling them with your parser's existing nodes.
> 2. In `interpreter.py`, write the `Interpreter` class with an `eval_node` method that has one branch per node type (Step 1b).  Make each branch raise `NotImplementedError` for now.
> 3. Check that the wiring works with this snippet at the bottom of `interpreter.py`, then run `python3 interpreter.py`:

```python
interp = Interpreter()
try:
    interp.eval_node(Num(42))
except NotImplementedError:
    print("dispatch reached the Num branch")   # good: the wiring works
```

> **You should see.** `dispatch reached the Num branch`.

Then fill in only the `Num` branch (`return node.value`) and the `Print` branch, and run `print 42;` end to end through your lexer, parser, and evaluator:

```bash
python3 -c "from parser import parse; from interpreter import Interpreter; Interpreter().eval_node(parse('print 42;'))"
```

> **You should see.** `42`.  The `Program` branch walks its statements, the `Print` branch evaluates its expression, and the `Num` branch returns the value.

### Suggested Pacing

See the course schedule for the assigned and due dates.  This is the longest assignment in the pipeline, with a window to match.  Two pair labs land inside it and complete pieces of it for you.  The **Environments and Scope lab** (due mid-assignment) builds the `Environment` machinery of Step 2c, and the **Type Checker Starter lab** (due later in the window) builds the core of Part 4's checker.  Part 2 is the steepest section; the sequence below climbs it in small steps rather than one leap:

| Checkpoint | You should have |
|------------|----------------|
| On assignment | Part 1 complete: all node dataclasses and the dispatch skeleton (Steps 1a-1b) |
| Checkpoint 1 | Expression evaluation and short-circuit logic with the bomb test passing (Steps 2a-2b) |
| Environments lab due | `Environment` and statement evaluation (grown from the lab); shadowing program prints `51` then `2` (Step 2c) |
| Checkpoint 2 | Break/continue signals and the file runner with staged errors (Step 2d, Step 3a) |
| Type Checker lab due | REPL with persistent environment and recovery; the checker core in place from the lab (Step 3b, Part 4) |
| Checkpoint 3 | Checker complete across all constructs; error hierarchy in place (Part 4, Step 5a) |
| Due date | `SEMANTICS.md`, differential programs, REPL transcript; ZIP submitted (Steps 5b-5c) |

---

## Part 1: AST Node Dataclasses (25 points)

A Python `dataclass` writes `__init__`, `__repr__`, and optional `__eq__` for you.  Clean node types make the evaluator's `isinstance` dispatch readable, and `__repr__` makes test failures self-documenting: a failing test prints the exact tree it was handed.

### Step 1a: Define the Node Types

Define the node types below as `@dataclass` classes in `ast_nodes.py`.  Every field must have a type annotation and a one-line comment explaining its meaning.  Store source positions (line, col) on nodes where they aid error reporting, at minimum on `Var`, `BinOp`, `UnaryOp`, `Let`, and `Assign`.  The three sub-steps group the nodes by family; the code is one file.

> **Do this.**
> 1. Open `ast_nodes.py`.  If your parser already defines these nodes, compare each one against the definitions below and reconcile field names, since the evaluator dispatches on exactly these classes.
> 2. Put the imports at the top of the file once, then add the three node families in order.
> 3. Check the file loads and that `__repr__` is doing its job:
>
> ```bash
> python3 -c "from ast_nodes import Num, BinOp; print(BinOp('+', Num(1), Num(2)))"
> ```

> **You should see.** `BinOp(op='+', left=Num(value=1, line=0), right=Num(value=2, line=0), line=0)`.  If you see an `AttributeError` or a `TypeError` about positional arguments, a field is missing or out of order.

#### Step 1a.1: Literals and variables

These are the leaves of the tree.  `Var` carries a line because an undefined name is the first runtime error you will report with a position.

```python
from dataclasses import dataclass, field
from typing import Any, List, Optional

@dataclass
class Num:
    value: float          # the numeric value (already parsed)
    line: int = 0

@dataclass
class Str:
    value: str            # decoded string value (escapes resolved)
    line: int = 0

@dataclass
class BoolLit:
    value: bool           # True or False
    line: int = 0

@dataclass
class Var:
    name: str             # variable name as it appears in source
    line: int = 0
```

#### Step 1a.2: Expressions

These nodes combine values.  `LogicOp` is a separate class from `BinOp` because `and` and `or` must short-circuit (Step 2b), and a shared branch would evaluate both sides.

```python
@dataclass
class BinOp:
    op: str               # one of: + - * / < <= > >= == !=
    left: Any
    right: Any
    line: int = 0

@dataclass
class UnaryOp:
    op: str               # one of: - not
    operand: Any
    line: int = 0

@dataclass
class LogicOp:
    op: str               # "and" or "or"; separate from BinOp for short-circuit
    left: Any
    right: Any
    line: int = 0
```

#### Step 1a.3: Statements

Statements run for their effect and return no value.  `Let` and `Assign` are separate nodes because defining a name and updating one are different operations on the environment (Step 2c), and `Program` is the root your file runner hands to the evaluator.

```python
@dataclass
class Let:
    name: str             # variable name being defined
    value: Any            # initializer expression
    line: int = 0

@dataclass
class Assign:
    name: str             # variable name being updated (must already exist)
    value: Any
    line: int = 0

@dataclass
class Print:
    value: Any            # expression to evaluate and print

@dataclass
class Block:
    stmts: List[Any] = field(default_factory=list)

@dataclass
class If:
    condition: Any
    then_branch: Any      # always a Block
    else_branch: Any      # Block, If, or None

@dataclass
class While:
    condition: Any
    body: Any             # always a Block

@dataclass
class Break:
    line: int = 0

@dataclass
class Continue:
    line: int = 0

@dataclass
class Program:
    stmts: List[Any] = field(default_factory=list)
```

### Step 1b: Build the Visitor Dispatch

Write an `Interpreter` class with one `eval_node(node)` method.  The method dispatches on node type using `isinstance`: it checks which class the node belongs to and runs the matching branch.  Every node type in Step 1a must have its own branch.  An `else` branch raises `InterpreterError("Unknown node type: ...")`.

> **Do this.**
> 1. Create `interpreter.py` in the project folder.
> 2. Paste the skeleton below and add one `elif` branch per remaining node type, each raising `NotImplementedError` for now.  The `env` parameter arrives in Step 2c; leave the default in place until then.
> 3. Run the worked example from Your First 30 Minutes with `python3 interpreter.py`.

```python
from ast_nodes import *

class InterpreterError(Exception):
    pass

class Interpreter:
    def eval_node(self, node, env=None):
        if isinstance(node, Num):
            raise NotImplementedError("Num")
        elif isinstance(node, Str):
            raise NotImplementedError("Str")
        elif isinstance(node, Program):
            raise NotImplementedError("Program")
        # TODO: one elif branch per remaining node type from Step 1a
        else:
            raise InterpreterError(f"Unknown node type: {type(node).__name__}")
```

> **You should see.** `dispatch reached the Num branch`.  Before you implement any evaluation logic, confirm that `eval_node(Num(42))` raises `NotImplementedError` (or returns a placeholder), and that every node type reaches its own branch rather than the `else`.  A quick way to check: construct one instance of each class and confirm the `NotImplementedError` message names that class.

---

## Part 2: Tree-Walking Evaluator (30 points)

### Step 2a: Evaluate Expressions

Implement evaluation for the expression nodes.  Return Python values: numbers as `float` or `int`, strings as `str`, booleans as `bool`.

- `Num`: return `node.value`.
- `Str`: return `node.value` (already decoded).
- `BoolLit`: return `node.value`.
- `Var`: call `env.lookup(node.name)`, raising a `LangNameError` if the name is not found.  Include the variable name and source line in the error.
- `UnaryOp("-")`: evaluate the operand.  If it is not a number, raise `LangTypeError("unary minus requires a number, got <type>")`.
- `BinOp`: evaluate both operands, then apply the operator.  The **type rules** are:
  - `+`, `-`, `*`, `/` require both operands to be numbers (otherwise raise `LangTypeError` naming both types).
  - `+` on two strings concatenates (if you support this, document your decision).
  - `/` by zero raises `LangZeroDivisionError` with the position.
  - `<`, `<=`, `>`, `>=` require numbers; `==`, `!=` compare any same-type pair (cross-type raises or returns False; document which and why).

The error classes (`LangNameError`, `LangTypeError`, `LangZeroDivisionError`) are defined in Step 5a.  Define them now at the top of `interpreter.py` and grow them later; Step 5a is required in every Part 5 direction.

> **Do this.**
> 1. In `interpreter.py`, replace the `NotImplementedError` in each expression branch with the rule above.
> 2. Run an arithmetic program through the whole pipeline:
>
> ```bash
> python3 -c "from parser import parse; from interpreter import Interpreter; Interpreter().eval_node(parse('print 1 + 2;'))"
> ```

> **You should see.** `3` (or `3.0` if your parser stores numbers as floats).  Then try the type-error program below and confirm the error names both types.

Worked example, type error:

```text
let x = "hello";
let y = x + 1;      # LangTypeError at line 2, col 11: + requires numbers, got str and int
```

### Step 2b: Implement Short-Circuit Logic

Short-circuit logic means the evaluator stops as soon as the left operand decides the answer.

- `LogicOp("and")`: evaluate left; if falsy, return it without evaluating right.  Otherwise return right.
- `LogicOp("or")`: evaluate left; if truthy, return it without evaluating right.  Otherwise return right.
- `UnaryOp("not")`: evaluate the operand, apply truthiness, and return the boolean complement.

Truthiness policy (document it in SEMANTICS.md): which values count as false in your language?  At minimum: `false`, `0`, `0.0`, and `""`.  Everything else is truthy.

**Bomb test**: include this program in your test suite and verify that it does not raise an error:

```text
let safe = true or (1 / 0);   # right side must NOT be evaluated
```

> **Do this.**
> 1. Create `test_interpreter.py` and add the bomb test as its first test:
>
> ```python
> from parser import parse
> from interpreter import Interpreter
>
> def test_bomb():
>     # must not raise: the right side of `or` is never evaluated
>     Interpreter().eval_node(parse('let safe = true or (1 / 0);'))
> ```
>
> 2. Run the suite:
>
> ```bash
> python3 -m pytest test_interpreter.py
> ```

> **You should see.** `1 passed`.  If you see `LangZeroDivisionError` in the traceback, your `or` branch evaluates the right operand before checking the left.

Control-flow theory questions (in your readme, required in every Part 5 direction), from the Control Flow and Statement Semantics session:

1.  Explain why short-circuiting is a *semantic commitment* rather than an optimization, using the bomb test as evidence.  What observable behavior changes if both sides evaluate?
2.  Your `and`/`or` return an *operand*, not a boolean.  Name one language that does this and one that coerces to boolean, and state one concrete program whose result differs between the two designs.
3.  Pick one truthiness rule you adopted and one you rejected, and defend the pair against a reliability argument from the Evaluating Languages criteria.

### Step 2c: Build the Environment and Evaluate Statements

An environment is the table that maps variable names to their current values.  Each block gets its own environment with a link to its parent, which is how nested scopes work.  The Environments and Scope lab builds this machinery with a partner; bring your lab code here.  The `Environment` class:

```python
class Environment:
    def __init__(self, parent=None):
        self._bindings = {}
        self._parent = parent

    def define(self, name: str, value):
        """Create a new binding in THIS scope (used by Let)."""
        self._bindings[name] = value

    def lookup(self, name: str):
        """Search this scope then parent scopes; raise LangNameError if not found."""
        if name in self._bindings:
            return self._bindings[name]
        if self._parent:
            return self._parent.lookup(name)
        raise LangNameError(f"Undefined variable '{name}'")

    def assign(self, name: str, value):
        """Update an existing binding wherever it lives; raise LangNameError if not found."""
        if name in self._bindings:
            self._bindings[name] = value
        elif self._parent:
            self._parent.assign(name, value)
        else:
            raise LangNameError(f"Cannot assign to undefined variable '{name}'")
```

Then implement the statements:

- `Let`: evaluate the initializer, then call `env.define(node.name, value)`.
- `Assign`: evaluate the value, then call `env.assign(node.name, value)`.  This updates the binding wherever it lives; it does *not* create a new one.
- `Print`: evaluate the expression and print the result to stdout.  Booleans print as `true`/`false`, not `True`/`False`.
- `Block`: create a child environment `child_env = Environment(parent=env)`, then evaluate each statement in the block using `child_env`.  When the block finishes, discard `child_env` (it goes out of scope naturally).
- `If`: evaluate the condition and convert it to a boolean with your truthiness rule.  Execute `then_branch` if truthy, and `else_branch` (if present) otherwise.
- `While`: evaluate the condition and execute the body while it is truthy.  Document whether the loop body creates a per-iteration scope (both choices are valid; pick one and write it in SEMANTICS.md).  Catch `BreakSignal` to exit early; catch `ContinueSignal` to restart the loop.

> **Do this.**
> 1. Add the `Environment` class to `interpreter.py`, above `Interpreter`.
> 2. Give `Interpreter` a global environment (`self.globals = Environment()` in `__init__`), and have `eval_node` use it when `env` is `None`.  Pass `env` through every recursive call so blocks can hand their child environment down.
> 3. Fill in the statement branches, then save the **shadowing program** as `shadow.ml` and run it through the pipeline:
>
> ```text
> let x = 2;
> {
>     let x = 51;
>     print x;       # prints 51
> }
> print x;           # prints 2
> ```
>
> ```bash
> python3 -c "from parser import parse; from interpreter import Interpreter; Interpreter().eval_node(parse(open('shadow.ml').read()))"
> ```

> **You should see.** `51` on one line and `2` on the next.  Add this program to `test_interpreter.py` as well.

> **If it fails.**
> - Both lines print `51`: your `Block` branch evaluated its statements in the parent environment instead of a child, or `Let` called `assign` instead of `define`.
> - `Undefined variable 'x'` after the block: your `Block` branch replaced `self.globals` with the child environment instead of passing the child down.

### Step 2d: Implement Break and Continue

Implement `break` and `continue` with signal exception classes:

```python
class BreakSignal(Exception): pass
class ContinueSignal(Exception): pass
```

`Break` and `Continue` nodes raise these signals, and the `While` evaluator catches them.  If a `BreakSignal` or `ContinueSignal` escapes a `While` body and reaches the top level, the error handler (Step 3a) catches it and reports it as a `LangRuntimeError("break outside loop")` or similar.

> **Do this.**
> 1. Add the two signal classes to `interpreter.py`.
> 2. Make the `Break` and `Continue` branches raise them, and wrap the body evaluation inside your `While` branch in `try`/`except` for both.
> 3. Add a test with a `while` loop that counts to 10 and breaks at 5, and confirm it prints `1` through `5` only.

> **You should see.** Five lines of output, then the program ends.  A `BreakSignal` traceback means the `While` branch is not catching it; an infinite loop means `continue` skipped the counter update, which is a semantics decision worth a line in SEMANTICS.md.

### Step 2e: Verify Invariants with Hypothesis

In the Parser assignment you used [Hypothesis](https://hypothesis.readthedocs.io/) to check a *syntactic* law (round-trip).  Here you check *semantic* laws: properties that must hold for every program, not only the ones in your test file.  These invariants are where scoping and short-circuit bugs hide, because they surface only on inputs you did not think to write.  This step is required.  Reuse the recursive AST generator you built for the parser, restricted to the expression and small-statement nodes your evaluator supports.

Encode **at least three** of the following invariants as `@given` tests.  The first two are required; pick at least one more:

1.  Determinism.  Evaluating the same AST twice in fresh environments produces identical output and result.  `eval(tree)` has no hidden state that leaks between runs.
2.  Scope restoration.  For any generated expression `e` and a fresh variable name `v` not free in `e`, evaluating a block that binds `v` with `let` and then evaluates `e` leaves the outer environment without `v` afterward: the inner `let` does not leak.  (Generate `e`; wrap it; assert the outer env is unchanged.)
3.  Short-circuit non-evaluation.  Give `and`/`or` a right operand with an observable side effect (for example, a call to a tool that appends to a list, or a subexpression that divides by zero).  Assert that when the left operand determines the result (`false and X`, `true or X`), the right operand's side effect never fires.  Hypothesis will hunt for the operand shape that sneaks past your short-circuit.
4.  Arithmetic agreement (metamorphic).  For generated integer-only expressions using `+ - *`, your evaluator's result equals Python's evaluation of the same expression.  This is a cheap oracle that catches precedence and associativity bugs that slipped through the parser into evaluation.

> **Do this.**
> 1. Copy your AST generator from the Parser assignment into `test_interpreter.py` (or import it) and restrict it to the nodes your evaluator supports.
> 2. Add one `@given` test per invariant, starting from this skeleton:
>
> ```python
> from hypothesis import given
> from hypothesis import strategies as st
> # TODO: import or paste your recursive AST generator, e.g. exprs()
>
> @given(tree=exprs())
> def test_determinism(tree):
>     # TODO: evaluate tree twice, each time with a fresh Interpreter()
>     # TODO: assert the two results (and any printed output) are identical
>     ...
>
> # TODO: test_scope_restoration, and at least one of
> #       test_short_circuit_non_evaluation or test_arithmetic_agreement
> ```
>
> 3. Run `python3 -m pytest test_interpreter.py` and read any shrunk counterexample Hypothesis prints.

> **You should see.** Each property test listed as passed, or a `Falsifying example` block showing the smallest program that breaks the invariant.  When a property fails, Hypothesis shrinks it to the minimal offending program.  In your `readme.md`, report one invariant that caught a real bug (or a reasoned all-clear, with the three properties and the generator shown).

> **Why this matters.** This step also feeds the Team Language Project: the same three invariants, generalized to your team's language, become the core of its property-based test suite, so write them to be reusable.

---

## Part 3: REPL and File Runner (15 points)

### Step 3a: Build the File Runner

`python3 mylang.py program.ml` should:

1.  Read the source file.
2.  Lex it, catching `LexError` -> print `"Lexical error at line L, col C: <message>"` and exit.
3.  Parse it, catching `ParseError` -> print `"Syntax error at line L, col C: expected X, found Y"` and exit.
4.  Evaluate it, catching `LangNameError`, `LangTypeError`, `LangZeroDivisionError`, and `LangRuntimeError` -> print `"Runtime error at line L: <message>"` and exit.

The stage label (`Lexical error`, `Syntax error`, `Runtime error`) must appear in every message.

> **Do this.**
> 1. Create `mylang.py` in the project folder, starting from this skeleton:
>
> ```python
> import sys
> from lexer import LexError          # TODO: match your lexer's error class name
> from parser import parse, ParseError
> from interpreter import Interpreter, LangError
>
> def run_file(path):
>     source = open(path).read()
>     # TODO: lex, catching LexError -> "Lexical error at line L, col C: ..."
>     # TODO: parse, catching ParseError -> "Syntax error at line L, col C: ..."
>     # TODO: evaluate, catching LangError subclasses -> "Runtime error at line L: ..."
>     # exit after printing any error
>
> def repl():
>     pass   # Step 3b
>
> if __name__ == "__main__":
>     if len(sys.argv) > 1:
>         run_file(sys.argv[1])
>     else:
>         repl()
> ```
>
> 2. Run the shadowing program through it, then a program with one error of each stage:
>
> ```bash
> python3 mylang.py shadow.ml
> ```

> **You should see.** `51` then `2`, with no traceback.  For a file containing `let y = 1 / 0;`, exactly one line: `Runtime error at line 1: division by zero` (your wording may differ; the stage label and line may not).

> **If it fails.**
> - A Python traceback instead of a staged message: the exception escaped the `try` for its stage.  Check that each stage's `except` names the right class.
> - `Runtime error` for a misspelled keyword: that is a lexical or syntax error and must be caught at its own stage, before evaluation begins.

### Step 3b: Build the REPL

`python3 mylang.py` with no arguments launches the REPL.  Requirements:

- Display a `>> ` prompt.
- Read one line (or detect a multi-line statement and keep prompting with `.. `; document your choice).
- Maintain a single `Environment` across all REPL inputs.
- On a successfully evaluated expression-statement, print the value.
- On any error (lexical, syntax, or runtime), print the error and return to the prompt without crashing.
- `quit` or `exit` (or EOF/Ctrl-D) exits cleanly.

> **Do this.**
> 1. Fill in `repl()` in `mylang.py`: create one `Interpreter` before the loop, and inside the loop read a line with `input(">> ")`, run it through the same three stages as `run_file`, and print any error instead of exiting.
> 2. Handle `EOFError` (Ctrl-D) and the words `quit` and `exit` by leaving the loop.
> 3. Launch it and reproduce the transcript below:
>
> ```bash
> python3 mylang.py
> ```

> **You should see.** This session, which you also save as `repl_transcript.txt` for your submission.  It demonstrates each error class and that the environment survives an error (`x` is still `15` at the end).

```text
>> let x = 10;
>> x = x + 5;
>> print x;
15
>> let y = x / 0;
Runtime error at line 1: division by zero
>> print undefined_var;
Runtime error at line 1: Undefined variable 'undefined_var'
>> @bad token
Lexical error at line 1, col 1: unexpected character '@'
>> print x;
15
>> quit
```

> **If it fails.**
> - `x` is gone after the division error: you created a new `Interpreter` (or a new `Environment`) inside the loop.
> - The REPL exits on the first error: an `except` is calling `sys.exit` the way `run_file` does.  In the REPL, print and continue.

---

## Part 4: The Small Static Type Checker (15 points)

Your evaluator enforces types *dynamically*: a type error surfaces only when the offending expression is actually evaluated.  Part 4 adds a small **static type checker** that catches a useful class of those errors before evaluation begins.  It runs as its own pipeline stage: lex -> parse -> check -> evaluate.  This is deliberately not full type inference.  The checker verifies only what is *declared*, and the Type Checker Starter lab builds its core with a partner before this part is due.

Keep the checker's scope contained: annotations are required at declarations, so there is no unification and no inference.  Where a type is unknown (an unannotated construct you choose not to cover), document the gap in your readme rather than guessing.  If you choose the full Hindley-Milner direction in Part 5, that direction grows this checker into whole-program inference.  Part 4 is its foundation, not a throwaway.

### Step 4a: Carry Type Annotations on Declarations

Your language's `define` statements and function definitions carry (or are extended to carry) type annotations: `let x: Num = 42;`, `fun f(a: Num, b: Str) -> Bool { ... }`.  The checker can only verify what the parser hands it, so the annotation has to survive lexing and parsing and land on the AST node.

> **Do this.**
> 1. Extend your lexer and parser so `let` accepts an optional `: Type` after the name (and so function definitions carry parameter and return annotations, if your language has functions).
> 2. Add the annotation to the node.  One way is an optional field on `Let`:
>
> ```python
> @dataclass
> class Let:
>     name: str                     # variable name being defined
>     value: Any                    # initializer expression
>     type_ann: Optional[str] = None  # declared type: "Num", "Str", "Bool", or None
>     line: int = 0
> ```
>
> 3. Confirm the annotation lands on the node:
>
> ```bash
> python3 -c "from parser import parse; print(parse('let x: Num = 42;'))"
> ```

> **You should see.** A `Program` whose `Let` node shows `type_ann='Num'`.  A `ParseError` means the parser is not consuming the colon and type name yet.

### Step 4b: Walk the AST with a Type Environment

The checker walks the AST once, maintaining a type environment that mirrors your `Environment` class (a table from names to declared types, with a parent link for nested blocks), and verifies three things:

- Literals and variables.  Every literal has its constant type; every variable use looks up the declared type; a `define` whose initializer's type disagrees with its annotation is an error.
- Operators.  Arithmetic operators require `Num` operands; comparison operators yield `Bool`; `and`/`or` require `Bool`; mixed-type operands are rejected naming *both* types.
- Call sites.  Every function call checks arity and each argument's type against the parameter annotations, and the call expression takes the declared return type; a function whose body cannot produce its declared return type is an error.

> **Do this.**
> 1. Create `typechecker.py`, starting from your Type Checker Starter lab code, and shape it around this skeleton:
>
> ```python
> from ast_nodes import *
> from interpreter import LangTypeError
>
> class TypeEnv:
>     """Mirrors Environment, but maps names to declared type names."""
>     def __init__(self, parent=None):
>         self._types = {}
>         self._parent = parent
>     # TODO: define(name, typ) and lookup(name), same shape as Environment
>
> def check(node, tenv=None):
>     """Return the type of an expression node; check a statement node and return None."""
>     if tenv is None:
>         tenv = TypeEnv()
>     if isinstance(node, Num):
>         return "Num"
>     # TODO: Str -> "Str", BoolLit -> "Bool", Var -> tenv.lookup(...)
>     # TODO: BinOp: arithmetic needs Num operands; comparisons yield Bool
>     # TODO: LogicOp and UnaryOp("not") need Bool
>     # TODO: Let: check the initializer against type_ann, then tenv.define
>     # TODO: Block: check statements in TypeEnv(parent=tenv)
>     # TODO: call sites: arity, argument types, declared return type
> ```
>
> 2. Write one ill-typed program per bullet above (three files) and one well-typed program, and add each to `test_interpreter.py`.

> **You should see.** `check(parse('let x: Num = 42;'))` returns without error, and `check(parse('let x: Num = "hi";'))` raises `LangTypeError`.

### Step 4c: Report Positioned Errors and Add the Stage

Report every rejection as `Type error at line L, col C: ...`, naming both conflicting types.  Your file runner gains a fourth stage label, and a program that fails the check never runs.

> **Do this.**
> 1. Make every `raise` in `typechecker.py` carry the node's line and col and name both types (declared vs. actual, or left vs. right operand).
> 2. In `mylang.py`, call `check(tree)` between parsing and evaluation in both `run_file` and `repl`, catching `LangTypeError` and printing `Type error at line L, col C: <message>`.
> 3. Run an ill-typed program:
>
> ```bash
> python3 mylang.py badtype.ml
> ```

> **You should see.** One `Type error at line L, col C: ...` line naming both types, and no program output at all, since the Type stage fires before the Run stage.  Keep this staged output; the rubric asks for it.

> **If it fails.**
> - The program prints output and then a type error: the check is running interleaved with evaluation.  It must finish over the whole tree before `eval_node` is called.
> - The message names only one type: carry both the expected and the actual type into the exception message.

---

## Part 5: Making the Semantics Precise (15 points), Choose Your Direction

Parts 1-4 give your language a working evaluator and a static checking stage.  Part 5 makes its semantics *precise*, in your choice of **direction**.  You complete one Part 5 and submit one deliverable, and the same 15-point rubric row applies equivalently to each.

| Direction | What you build | Pick this if |
|-----------|----------------|--------------|
| **Staged errors and SEMANTICS.md** (the core direction) | The language-level error hierarchy and a document stating every dynamic rule with an example, as Steps 5a-5c below scaffold it | You want the most direct path to a complete semantics reference for your team project |
| **Full type inference (Hindley-Milner)** | Part 4's annotation checker grown into whole-program *inference* that deduces types with no annotations at all, the way Haskell, OCaml, and Rust do.  See the [typing direction](#part-5-direction-full-type-inference-hindley-milner) | You enjoyed Part 4 and want the unification machinery behind modern type systems |
| **The Intcode VM** | A *virtual machine* that executes a flat list of numeric opcodes, the model behind CPython's bytecode, the JVM, and WebAssembly, implemented as the [Advent of Code 2019 Intcode](https://adventofcode.com/2019/day/2) machine and specified opcode by opcode.  See the [Intcode direction](#part-5-direction-a-contrasting-execution-model-the-intcode-vm) | You want to have built both dominant execution models and to say precisely how they differ |

In every direction, Step 5a's error hierarchy is required (lexical, syntax, and name errors still need staged reporting; in the Intcode direction, malformed programs and illegal opcodes are staged errors), and the control-flow theory questions from Step 2b go in your readme.  The two alternative directions replace Steps 5b and 5c (SEMANTICS.md and the differential programs) with their own sections below.  The typing direction replaces them with the inference engine; the Intcode direction replaces them with the VM, where the self-checking AoC inputs are your oracle and a required differential test pins your VM's arithmetic against your tree-walker's on shared operations.  Intcode's operational semantics is small enough to specify completely yet rich enough to be Turing-capable, and you make it precise by writing each opcode as a state-transition rule.  The total remains 100 points.

Whichever direction you choose, the goal is the same.  For every construct in your language (or VM), there is exactly one written answer to "what does this mean, and what happens when it is misused?", and your implementation agrees with it.

### Step 5a: Define the Error Class Hierarchy

Define a hierarchy of language-specific exceptions.  You started these in Step 2a; finish them here.

```python
class LangError(Exception):
    def __init__(self, message, line=0, col=0):
        self.message = message
        self.line = line
        self.col = col
    def __str__(self):
        return f"line {self.line}, col {self.col}: {self.message}"

class LangNameError(LangError): pass
class LangTypeError(LangError): pass
class LangZeroDivisionError(LangError): pass
class LangRuntimeError(LangError): pass
```

> **Do this.**
> 1. Put the hierarchy at the top of `interpreter.py`, replacing any placeholder classes from Step 2a.
> 2. Search `interpreter.py` for every `raise` and confirm each one uses one of these classes with a meaningful message that names the variables, types, or operators involved, and passes the node's line (and col where you store it).
> 3. Add one test per error class to `test_interpreter.py`, each asserting the class raised and that the message names the offending variable, type, or operator.

> **You should see.** Every error-class test passing, and `python3 mylang.py` reporting each one with its stage label and position, in the format Step 3a requires.

### Step 5b: Write SEMANTICS.md

Write `SEMANTICS.md` with one section per topic below.  Each section must include a statement of the rule, a code example in your language, and the expected output (or error message).

1.  **Truthiness**: what values are falsy?  What are truthy?  Show a `while` loop that relies on numeric truthiness.
2.  **Division by zero**: what error is raised?  What stage identifies it?  Show the exact error message format.
3.  **Scoping and shadowing**: where does `let` define?  Where does bare assignment update?  Show the shadowing program and its output.
4.  **Loop-variable persistence**: does the loop variable remain in scope after the loop body?  Show a program whose output depends on this decision.
5.  **Assignment vs. definition**: what error does assigning an undefined variable produce?  Show it.
6.  **Type strictness**: can you add an int to a float?  A string to a number?  Show both cases and their outcomes.
7.  **String concatenation**: is `"a" + "b"` legal?  What about `"a" + 1`?  State the rule and show examples.

> **Do this.**
> 1. Create `SEMANTICS.md` with seven `##` headings, one per topic, in the order above.
> 2. For each, write the rule in one or two sentences, then paste the example program and run it with `python3 mylang.py` to capture the real output.  Do not type the output from memory.

> **You should see.** Every pasted output produced by your own interpreter.  If the program and the prose disagree, one of them is wrong, and Step 5c is where you settle it.

### Step 5c: Run the Differential Programs

Five programs are provided whose outputs depend on your semantics decisions.

> **Do this.**
> 1. Run each program with `python3 mylang.py <program>` and record its output.
> 2. Confirm that each output matches your SEMANTICS.md documentation.  If it does not match, fix either the code or the documentation; they must agree.
> 3. Add the five programs and their recorded outputs to `test_interpreter.py`.

> **You should see.** Five outputs, each traceable to a specific rule in SEMANTICS.md.

---

## Part 5 Direction: Full Type Inference (Hindley-Milner)

{: #part-5-direction-full-type-inference-hindley-milner}

This direction replaces Steps 5b-5c.  You grow Part 4's annotation checker into whole-program *inference*: still its own pipeline stage after parsing and before evaluation, but now deducing types where no annotations exist at all.  It is the same machinery (unification and Algorithm-W-style inference) that lets Haskell, OCaml, and Rust deduce types without annotations, scoped here to your language's constructs.  Your Part 4 checker is the foundation.  Its type environment, its staged error reporting, and its operator rules all carry forward.  What changes is that unknown types become type *variables* to be solved rather than gaps to be documented.

> **What this direction requires.** `types.py` (T.1), `typecheck.py` (T.2), positioned type errors (T.3), and `TYPES.md` with its accepted and rejected test programs (T.4), in place of `SEMANTICS.md` and the differential programs.  Step 5a is still required.

### Background

A **type** is one of three things: a type variable `α, β, ...` (unknown, to be solved), a type constant (`Num`, `Bool`, `Str`), or, if your checker covers functions, a function type `τ₁ -> τ₂`.  A substitution maps type variables to types.  Unification of two types finds the most general substitution that makes them equal, or fails, and that failure *is* the type error.  The inference algorithm walks the AST, generates fresh type variables constrained by each node's structure, and unifies to solve them.

### Step T.1: Type Terms, Substitution, and Unification (`types.py`)

Define frozen dataclasses `TVar(name)` and `TCon(name)` (and `TFun(param, ret)` if you cover functions), with `apply(subst, typ)` and `free_vars(typ)` helpers.  Implement `unify(t1, t2, subst) -> subst`:

1.  Apply the current substitution to both types.  If they are now identical, return the substitution unchanged.
2.  If one is a type variable `α` that does not occur in the other, extend the substitution with `{α: other}`.  The **occurs check** (refusing to bind `α` to a type containing `α`) is what prevents infinite types.  Raise a `LangTypeError` naming both types if it fires.
3.  Recurse componentwise on matching constructors.  Otherwise raise a `LangTypeError` naming both conflicting types.

> **Do this.**
> 1. Create `types.py` in the project folder from this skeleton:
>
> ```python
> from dataclasses import dataclass
> from interpreter import LangTypeError
>
> @dataclass(frozen=True)
> class TVar:
>     name: str             # a type variable, e.g. "a"
>
> @dataclass(frozen=True)
> class TCon:
>     name: str             # a type constant: "Num", "Bool", or "Str"
>
> TNum, TBool, TStr = TCon("Num"), TCon("Bool"), TCon("Str")
>
> def apply(subst, typ):
>     # TODO: replace every TVar bound in subst, recursively
>     ...
>
> def free_vars(typ):
>     # TODO: the set of TVar names appearing in typ
>     ...
>
> def unify(t1, t2, subst):
>     # TODO: the three rules above; return the extended substitution
>     ...
> ```
>
> 2. Add these tests to `test_interpreter.py`, at minimum: `unify(TVar("a"), TNum, {})` binds `a`; unifying `TNum` with `TBool` raises; and an occurs-check case raises.

> **You should see.** The three unification tests passing.  If the occurs-check test passes only because unification never terminated, you have found the infinite type it exists to prevent; add the check before the bind.

### Step T.2: Inference over Your AST (`typecheck.py`)

Implement `infer(node, type_env, subst) -> (subst, type)` with one case per node type your evaluator handles:

- Literals return their constant type.
- `Var` looks up the type environment (undefined names remain `LangNameError`s).
- Arithmetic operators unify both operands with `Num` and return `Num`.
- Comparisons return `Bool`.
- `LogicOp` and `not` unify with `Bool`.
- `If` and `While` conditions must be `Bool`.  Note that this is *stricter* than your dynamic truthiness rule; see the reflection prompt.
- `Let` extends the type environment.
- `Assign` unifies the new value's type with the variable's existing type.
- `Block` checks its statements in a child type environment that mirrors your `Environment` scoping.

Thread the substitution through every case.

> **Do this.**
> 1. Create `typecheck.py` (it may grow out of Part 4's `typechecker.py`; keep whichever file name you document) with `infer` structured like `eval_node`: one `isinstance` branch per node, each returning the new substitution and the node's type.
> 2. Wire it into `mylang.py` as a stage: `python3 mylang.py --typed program.ml` (or make it the default; document your choice) lexes, parses, **type-checks**, and only then evaluates.  The stage label `Type error` joins the staged-error format of Part 3: `Type error at line L: <message>`.
> 3. Run a well-typed program and confirm it still evaluates as before:
>
> ```bash
> python3 mylang.py --typed shadow.ml
> ```

> **You should see.** `51` then `2`, exactly as without the checker.  A well-typed program must pass through the new stage unchanged.

### Step T.3: Positioned Type Errors

Every type error must name both conflicting types, cite the source line, and give a short context, in the spirit of:

```text
Type error at line 7: condition of 'if' must be Bool, got Num
Type error at line 12: '+' requires Num operands, got Str and Num
Type error at line 5: cannot unify Num with Bool (from assignment to 'result')
```

> **Do this.**
> 1. Give every `LangTypeError` raised from `unify` and `infer` the line of the node being checked and a context phrase naming the construct.
> 2. Write three programs, one per message above, and confirm each produces one positioned line and no program output.

> **You should see.** Three distinct `Type error at line L: ...` lines, each naming both types.

### Step T.4: TYPES.md and Test Programs

In place of SEMANTICS.md, write `TYPES.md`: one section per construct stating its typing rule in prose (or inference-rule notation), with one program the checker accepts and one it rejects, showing the exact error message.  Include at least five test programs total: three that the checker rejects with distinct positioned errors, and two that pass the checker and then run correctly, showing that well-typed programs still evaluate as before.

> **Do this.**
> 1. Create `TYPES.md` with one `##` section per construct your `infer` covers.
> 2. Under each, state the rule, then paste one accepted program and one rejected program with the checker's real output for each.
> 3. Add the five test programs to `test_interpreter.py`, asserting the three rejections by message and the two acceptances by evaluated output.

> **You should see.** Five tests passing, and a `TYPES.md` whose every error message was produced by your checker, not typed from memory.

**Depth (part of "proficient"):** if your language grows function values in the team project (or if you simply want the full Milner experience), implement let-polymorphism.  Generalize a let-bound name's type over the type variables not free in the environment, and instantiate fresh copies at each use, so a polymorphic identity function can be applied to both a `Num` and a `Bool` in the same scope.  Self-application (`f(f)`) must still be rejected: no finite type satisfies it, and your occurs check is what says so.

---

## Part 5 Direction: A Contrasting Execution Model, the Intcode VM

{: #part-5-direction-a-contrasting-execution-model-the-intcode-vm}

> **What this direction requires.** `INTCODE.md` with a transition rule per opcode (I.1), `intcode.py` (I.2), the AoC checkpoint outputs in your readme (I.3), and the tree-walker-vs-VM differential test in `test_interpreter.py` (I.4), in place of `SEMANTICS.md` and the differential programs.  Step 5a is still required.

### Background

A tree-walker is one way to run a program; a **virtual machine** is another.  Instead of recursing over an AST, a VM holds the program as a flat array of integers and steps a program counter through them, decoding one instruction at a time.  This is the model underneath CPython's bytecode, the JVM, and WebAssembly, and Advent of Code 2019's Intcode is the smallest complete instance of it worth studying.  If you choose this direction, you will have built the two dominant execution models in the same course and can say precisely how they differ.

Intcode's operational semantics is small enough to write down completely, which is what makes it a legitimate "make the semantics precise" direction.  Every opcode is one state-transition rule over the machine state `(memory, pc, input, output, relative_base)`.

### Step I.1: Write the Operational Semantics (`INTCODE.md`)

Before you write code, write `INTCODE.md`.  For each opcode, state its rule as a transition on the machine state.  For example, opcode 1 (add):

```text
add: with parameters a, b, c, set mem[c] <- value(a) + value(b), then pc <- pc + 4.
```

Cover opcodes `1` (add), `2` (multiply), `3` (input), `4` (output), `5` (jump-if-true), `6` (jump-if-false), `7` (less-than), `8` (equals), and `99` (halt), plus the **parameter modes** (0 = position, 1 = immediate, and, for the full machine, 2 = relative, with opcode `9` adjusting the relative base).  State what an unknown opcode does: it is a staged error (`LangRuntimeError`), not a crash.

> **Do this.**
> 1. Create `INTCODE.md` with a section on the machine state, a section per opcode with its transition rule in the form above, a section on parameter modes, and a section on illegal opcodes and out-of-range addresses.
> 2. Write the rules before `intcode.py` exists.  The document is the specification your VM must agree with, not a description written afterward.

> **You should see.** Nine opcode rules (ten with opcode `9`), each stating what is read, what is written, and how `pc` changes.

### Step I.2: Build the VM (`intcode.py`)

Implement `run(program, inputs) -> outputs` as an opcode dispatch loop.  Decode each instruction as `opcode = instr % 100` and the per-parameter modes from the higher digits.  Structure the dispatch so that adding an opcode is a localized change (a dict from opcode to a small handler, or a match statement), the same "one construct, one place" discipline as your tree-walker's visitor.  Illegal opcodes and out-of-range addresses raise your Step 5a error classes with a position (the `pc` at fault).

> **Do this.**
> 1. Create `intcode.py` in the project folder from this skeleton:
>
> ```python
> from interpreter import LangRuntimeError
>
> def run(program, inputs):
>     """Execute an Intcode program; return the list of outputs."""
>     mem = program                # the program is its own memory; run in place
>     pc = 0                       # (copy it first if you prefer, and say so in INTCODE.md)
>     outputs = []
>     inputs = list(inputs)
>     while True:
>         instr = mem[pc]
>         opcode = instr % 100
>         # TODO: decode parameter modes from instr // 100
>         # TODO: dispatch on opcode (dict of handlers or match statement)
>         # TODO: opcode 99 -> return outputs
>         # TODO: unknown opcode -> raise LangRuntimeError(f"illegal opcode {opcode}", line=pc)
>         ...
> ```
>
> 2. Run the Day 2 sample:
>
> ```bash
> python3 -c "from intcode import run; p=[1,9,10,3,2,3,11,0,99,30,40,50]; run(p, []); print(p[0])"
> ```

> **You should see.** `3500`: the sample program halts with that value in position 0.  If you see `1`, the program was never modified, so either the add handler is writing somewhere else or `run` is working on a copy without returning it.

### Step I.3: Check the VM against the AoC Oracle

Intcode is self-validating: the puzzle inputs come with known answers.  Include at least these checkpoints, each with the exact expected output in your `readme.md`:

- The Day 2 sample programs (e.g., `1,9,10,3,2,3,11,0,99,30,40,50` halts with `3500` in position 0).
- A Day 5 program exercising input, output, immediate mode, and a jump/comparison (e.g., "is the input equal to 8?").
- If you implement relative mode + opcode 9, the Day 9 quine (`104,1125899906842624,99`) which must output its own large constant.

> **Do this.**
> 1. Add one test per checkpoint to `test_interpreter.py`, asserting the exact expected output.
> 2. Record each checkpoint and its output in `readme.md`.
> 3. Add a test that an illegal opcode raises `LangRuntimeError` with the `pc` at fault.

> **You should see.** Each checkpoint passing, and the illegal-opcode test reporting a staged, positioned error rather than an `IndexError` or `KeyError`.

### Step I.4: Differential Test against Your Tree-Walker (Required)

The two execution models must agree where they overlap.

> **Do this.**
> 1. Write a differential test: for a handful of integer arithmetic expressions, evaluate each **both** with your Part 2 tree-walker and with an equivalent hand-assembled Intcode program, and assert that the results match.
> 2. In your readme, name one thing the VM makes easy that the tree-walker makes hard (or vice versa), e.g., self-modifying code, or explicit control over evaluation order.

> **You should see.** The differential test passing for every expression, with each Intcode program's assembly shown in the test so a reader can check the correspondence.

> **Scope note.** This direction is warm-up-scale by design.  The VM is a couple hundred lines and its correctness is externally checkable, so your effort goes into the *precise semantics* and the *model comparison*, which is what the 15-point Part 5 rubric rewards.

---

## Deliverables

Submit a ZIP containing:

| File or artifact | What it shows | Rubric row |
|------------------|---------------|------------|
| `interpreter.py` | The evaluator, Environment class, and error hierarchy (importing `lexer.py` and `parser.py` unchanged; note any fixes) | Parts 1, 2, 5 |
| `mylang.py` | The entry point: file runner and REPL (Part 3), with the Type stage from Part 4 | Parts 3, 4 |
| `typechecker.py` | The small static type checker | Part 4 |
| `SEMANTICS.md` | The language semantics document | Part 5 |
| `test_interpreter.py` | Test suite with the shadowing program, the bomb test, all error-class tests, the differential programs, and the required Step 2e Hypothesis invariant tests | Parts 2, 4, 5 |
| `repl_transcript.txt` | The REPL session showing each error class and recovery | Part 3 |
| `readme.md` | Approximately one page connecting the interpreter to the pipeline and the team project; the control-flow theory questions; the Step 2e report; any reference-component declaration; your Python version | Parts 2, 5 |

**Typing direction:** substitute `types.py`, `typecheck.py`, and `TYPES.md` (with its accepted/rejected test programs) for `SEMANTICS.md` and the differential programs.  Everything else on the list is unchanged, and the REPL transcript also demonstrates one positioned type error.

**Intcode direction:** substitute `intcode.py` and `INTCODE.md` (with the per-opcode transition rules) for `SEMANTICS.md` and the differential programs.  Add the AoC checkpoint outputs and the tree-walker-vs-VM differential test to `test_interpreter.py`.  Everything else on the list is unchanged.

Every direction includes the required Step 2e Hypothesis invariant tests in `test_interpreter.py`.

Ensure reproducibility by listing your Python version.

---

## Self-Check Before You Submit

- [ ] Every node type from Step 1a is a dataclass with annotated, commented fields, and `Var`, `BinOp`, `UnaryOp`, `Let`, and `Assign` carry positions.
- [ ] The shadowing program prints `51` then `2`, and the bomb test passes without evaluating its right side.
- [ ] Every runtime error is a Step 5a class raised at the language level with stage and position, and type errors name both operand types.
- [ ] At least three Hypothesis invariants (determinism, scope restoration, and one more) are in `test_interpreter.py`, and the readme reports a shrunk counterexample or a reasoned all-clear.
- [ ] The REPL keeps its environment across an error, and `repl_transcript.txt` shows every error class and recovery.
- [ ] The file runner prints a stage label (`Lexical`, `Syntax`, `Type`, `Runtime`) in every error message, and the Type stage fires before any code runs.
- [ ] The Part 5 deliverable for your direction is complete (`SEMANTICS.md` and the differential programs, or `types.py` + `typecheck.py` + `TYPES.md`, or `intcode.py` + `INTCODE.md` with the AoC checkpoints and the differential test), and the control-flow theory questions are answered in the readme.
- [ ] The readme lists your Python version and any reference component you used.

---

## Grading Breakdown

| Component | Points |
|-----------|--------|
| Part 1: AST Node Dataclasses | 25 |
| Part 2: Tree-Walking Evaluator | 30 |
| Part 3: REPL and File Runner | 15 |
| Part 4: The Small Static Type Checker | 15 |
| Part 5 (chosen direction): Error Messages and SEMANTICS.md, or full Hindley-Milner Type Inference, or the Intcode VM | 15 |
| **Total** | **100** |

---

## Reflection Prompts

- Which semantics decision did you change after testing revealed a consequence you had not foreseen?
- Point to the exact line in your `Environment` class that makes your language statically (lexically) scoped rather than dynamically scoped.
- Typing direction only: your dynamic truthiness rule accepts `while 1 { ... }`, but your type checker demands a `Bool` condition.  Where else did the static discipline reject a program your evaluator would have happily run, and which behavior do you consider correct for your language?
- The `BreakSignal`/`ContinueSignal` pattern uses exceptions for control flow, a technique the course calls "signal exceptions."  What property of exceptions makes them well suited for this, and what would you use instead if exceptions were not available?
- If collaboration with a buddy was permitted, did you work with a buddy on this assignment?  If so, who?  If not, do you certify that this submission represents your own original work?  Please identify any and all portions of your submission that were not originally written by you.
- AI disclosure: list any generative-AI tools you used, for what, and how you verified the results (or state 'none').
- Approximately how many hours it took you to finish this assignment (I will not judge you for this at all; I am simply using it to gauge if the assignments are too easy or hard)?
