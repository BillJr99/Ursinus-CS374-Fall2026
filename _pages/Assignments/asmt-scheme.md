---
layout: assignment
permalink: /Assignments/Scheme
title: "CS374: Principles of Programming Languages - Functional Programming with Scheme"
info:
  coursenum: CS374
  purpose: "To get a Scheme environment running on your own machine and then write, from scratch, the list recursion, functional composition, and closures that the functional paradigm is actually made of, ending with an evaluator for arithmetic expressions written as nested lists."
  tilt:
    task: "Rewrite one of your own loops in a functional style, install Scheme (or open a browser REPL), work the four guided examples, then write the exercises and an evaluator for nested-list arithmetic expressions, submitting real transcripts of each running."
    criteria: "I grade this on a defended functional rewrite of a loop you wrote, a working environment with evidence, correct recursive list functions with their empty-list cases handled, correct use of functions as values including a closure, and a working expression evaluator that handles an unknown operator and is explained, weighted 10/18/32/18/22 across the five parts. The rubric below breaks it down in full."
  points: 100
  goals:
    - To rewrite a loop you already know how to write into map, filter, and reduce, and to say honestly which version reads better and why
    - To install and run a Scheme implementation, or run one in a browser, and to read its error messages
    - To write recursive functions over lists using car, cdr, cons, and a base case, since Scheme has no loop
    - To compose functions and pass them as values, including building a fold that takes its operator as a parameter
    - To write a closure and explain what it captured
    - To read and write let, association lists, and assq before you need them in the evaluator
    - To write a recursive evaluator over a nested-list expression tree, the same structure the parser you write later in this course produces
  rubric:
    - weight: 10
      description: "Part 0: The Functional Rewrite (Goal 1)"
      preemerging: "No rewrite is submitted, or the original loop is not shown"
      beginning: "A rewrite is submitted but it does not run, or it still uses an explicit loop"
      progressing: "The rewrite runs and is equivalent to the original, but the write-up asserts a preference without arguing for it"
      proficient: "Both versions are shown and run; the rewrite uses map, filter, and reduce appropriately; and the write-up argues which is more readable and separates what is about the code from what is about your own habits"
    - weight: 18
      description: "Setup and the Guided Examples (Goal 2)"
      preemerging: "No environment is running and no transcript is submitted"
      beginning: "A REPL is running but the transcripts are retyped by hand rather than captured, or several examples were not run"
      progressing: "All four guided examples run and are captured, but the write-up does not say which route was used or what went wrong along the way"
      proficient: "Every guided example is captured as a real transcript, the write-up names the route taken (local install or browser) with its version, and it reports at least one error you hit and how you read the message"
    - weight: 32
      description: "List Recursion (Goal 3)"
      preemerging: "The recursive functions are missing, or none returns a correct answer on a nonempty list"
      beginning: "Some functions work on typical lists but every one of them errors or loops forever on the empty list"
      progressing: "All functions are correct on nonempty lists and most handle the empty list, but at least one empty-list decision is undocumented or inconsistent with the others"
      proficient: "czr, reverse, count, and the improved largest are all correct; every one has a documented, defended answer for the empty list using pair? or null?; and the improvement to largest is explained in terms of how many recursive calls it makes rather than asserted"
    - weight: 18
      description: "Functions as Values (Goals 4, 5)"
      preemerging: "No function takes or returns another function"
      beginning: "The operator fold works for addition only, or the counter is written with a global rather than a captured binding"
      progressing: "The fold works for several operators and the counter increments, but two counters share state or the write-up does not say what was captured"
      proficient: "The fold takes its operator as a parameter and is demonstrated on at least three operators including one you define yourself; two independently created counters count independently; and the write-up names exactly what each closure captured and where it lives"
    - weight: 22
      description: "The Expression Evaluator (Goal 6)"
      preemerging: "No evaluator is submitted, or it does not run"
      beginning: "The evaluator handles a flat expression such as (+ 1 2) but fails on a nested one, or the operator symbol is never resolved to a procedure"
      progressing: "The evaluator is correct on all the required test cases but does not detect an unknown operator, or the required extension is missing"
      proficient: "The evaluator is correct on every required test case including the three-deep nesting and the division case; an unknown operator is reported rather than crashing; one of the two extensions works; and the write-up answers all three questions, including where the recursion bottoms out and why it terminates"
  readings:
    - rtitle: "Programming Paradigms, Evaluating Languages, and an Introduction to Functional Programming Activity"
      rlink: Activities/liascript-languageevaluation.md
      liapage: true
    - rtitle: "Functional Programming in Scheme, Part 2 Activity"
      rlink: Activities/liascript-scheme.md
      liapage: true
    - rtitle: "Functional Programming and Higher-Order Functions Activity"
      rlink: Activities/liascript-functional.md
      liapage: true
    - rtitle: "Scheme Essentials for the Programming Languages Course"
      rlink: ../Tutorials/SchemeEssentials
    - rtitle: "The Scheme Programming Language (Dybvig)"
      rlink: https://www.scheme.com/tspl3/
tags:
  - functional
  - scheme
  - paradigms
---

This assignment is the written half of our work in the functional paradigm. Everything in it was worked at the board or in the activity decks, so nothing here should be a surprise; what is new is that you write it yourself, with a real interpreter telling you when you are wrong.

Work it in order. Part 0 is a short warmup in a language you already know, and you should do it before you start Part 1. Part 1 gets Scheme running and walks four examples with you. Parts 2 and 3 are exercises built directly on those examples. Before Part 4, there is a short primer on four forms the evaluator needs that we have not yet used as heavily in class: `let`, association lists, `assq`, and a second look at `map` and `apply`. Part 4 is the expression evaluator itself, and it is the part I most want to read.

**This is individual work.** Talk to each other about ideas and error messages as much as you like; the code and the write-up are yours.

---

## Part 0: Before You Start — The Functional Rewrite (10 points)

Do this one first, in **Python or whatever language you reach for by default**, not in Scheme. It takes about twenty minutes, and its whole purpose is to make you notice your own habits before a new language starts rearranging them.

Find a loop you have actually written: something from a previous course, a script, anything with a `for` in it that does real work. Rewrite it using `map`, `filter`, and `reduce` (in Python, `functools.reduce`, and comprehensions count as `map`/`filter` if you say so).

Then, in `part0.md`, put:

1. **Both versions**, the original loop and the rewrite, and the output of each showing they agree.
2. **Which one you find more readable**, in two or three sentences.
3. **The honest part**: how much of your answer to (2) is about the code, and how much is about which one you have seen more often? The first time most people do this, the functional version reads *worse* to them, and that reaction is the interesting data, not a wrong answer.

If your loop refuses to translate cleanly, that is the best possible outcome here. Say where it broke. A loop that carries two accumulators, mutates something outside itself, or breaks early is exactly the case where the paradigms genuinely diverge, and naming why is worth more than a smooth rewrite.

> **Note:** you will write a closure in Part 3 (`make-counter`, exercise 9) and trace what it captured there. Do not do that twice; this part is only the loop.

---

## Part 1: Getting Scheme Running (18 points)

### Pick a route

You need a Scheme prompt. Any of these gives you one, and the first three need no new install at all:

- **The course dev container**: if you set up the [course container]({{ site.baseurl }}/Tutorials/DevEnvironment) in the Overview assignment, a Scheme is already installed and you are done: run `guile` for a REPL, or `guile your_file.scm` to run a file. `mit-scheme` is in there too, on the CPU architectures Debian builds it for. Report whichever one you use, and its version, in the write-up.
- **[try.scheme.org](https://try.scheme.org)**: a full Scheme REPL in a browser tab. Nothing to set up, and the fastest way to be typing in thirty seconds.
- **The course's own runner**: the [Scheme warmup exercise]({{ site.baseurl }}/Modules/Scheme/Warmup/Exercise) runs Scheme directly in the page and checks your answer. Do that one first; it takes two minutes and confirms your browser is not the problem.
- **A Python Scheme, no package manager needed**: `git clone https://github.com/BillJr99/scheme-interpreter.git` gives you a `scheme.py` you run as `python scheme.py <your scheme file>`.
- **A real local install**, which is what I would like you to end up with:
  * **Cygwin (Windows):** install `guile` from the Cygwin installer
  * **Ubuntu (Linux):** `sudo apt install mit-scheme`
  * **Mac:** `brew install mit-scheme`, provided you have installed [homebrew](https://brew.sh/)

Whichever you pick, get to the point where you can run a file rather than only type at a prompt. Every exercise below wants a file you can hand in.

> **Watch out!** Forgetting the quote before a list literal is the most common beginner error in this language. `(1 2 3)` tells Scheme to call the function named `1` with arguments `2` and `3`, and since `1` is not a function you get `application: not a procedure` or similar. Write `'(1 2 3)` when you mean data. Trigger this error on purpose once and read the message; the write-up asks you about it.

### The four guided examples

Type each of these, run it, and **capture the transcript**. Then change one thing and run it again. These are the worked examples the exercises build on, so do not skip ahead.

**Example 1: lists, and `define` as binding.**

```scheme
(define L (list 'a 'b 'c))
(car L)                      ; a
(cdr L)                      ; (b c)
(cons 'z L)                  ; (z a b c)

(define x (+ 3 2))
(+ x 5)                      ; 10

(define add +)
(add 3 2)                    ; 5
```

`car` is the first element, `cdr` is everything after it, and `cons` puts one element back on the front. Those three are the whole engine. `(define add +)` is not a typo: `+` is an ordinary value, and `define` binds names to values of any kind, functions included.

**Example 2: `lambda`, `if`, and recursion.**

```scheme
(define square
  (lambda (n)
    (* n n)))

(define pow
  (lambda (n k)
    (if (= k 0)
        1
        (* n (pow n (- k 1))))))

(square (pow 5 3))           ; 15625
```

Every recursion in this assignment has that shape: a base case that answers directly, and a recursive case that does a little work and asks a smaller version of itself.

**Example 3: recursion over a list.**

```scheme
(define sumlist
  (lambda (L)
    (if (null? (cdr L))
        (car L)
        (+ (car L) (sumlist (cdr L))))))

(sumlist (list 1 2 3))       ; 6
```

Note where this one stops: at the *last element*, not at the empty list. That means `(sumlist '())` is an error. Whether that is a bug is Part 2's first question.

**Example 4: `cond`, `map`, and `apply`.**

```scheme
(define classify
  (lambda (n)
    (cond ((< n 0) 'negative)
          ((= n 0) 'zero)
          (else    'positive))))

(map classify '(-3 0 7))     ; (negative zero positive)

(define L1 '(1 2 3))
(define L2 '(4 5 6))
(map - L1 L2)                ; (-3 -3 -3)
(apply + '(1 2 3))           ; 6
```

`cond` is `if` with more than two branches. `map` takes a *function* as its first argument and applies it across a list. `apply` does the opposite: it takes one function and one list, and spreads the list out as that function's arguments, so `(apply + '(1 2 3))` is `(+ 1 2 3)`.

We will come back to both `map` and `apply` in the primer before Part 4, so do not worry yet about using them fluently; for now, just get the transcript above running and matching the comments.

### What to write up

In `setup.md`: which route you used and its version, the four captured transcripts, and one error you hit along the way with the message it printed and what it turned out to mean. If nothing went wrong, go trigger the unquoted-list error deliberately and write that one up.

---

## Part 2: List Recursion (32 points)

Put these in `recursion.scm`, with a test call after each one. Every function here must have a documented answer for the empty list; use `null?` or `pair?` (which returns `#t` for a nonempty list) to guard it, and say in a comment what you decided and why.

1. **`czr`**: return the last element of a list. Model it on `sumlist`, but notice that nothing has to happen on the way back up: the answer is just whatever the deepest call found.
2. **`count`**: return how many items are in a list. Use `czr` as a guide to traversing the list. Its base case cannot look at `(car L)` at all, which is the hint you need.
3. **`reverse-list`**: reverse a list using only `car`, `cdr`, and `cons`. (Name it `reverse-list` so you do not collide with the built-in `reverse`; compare against the built-in when you are done.) Then answer: how many `cons` calls does yours make for a list of length `n`?
4. **`largest`**: return the largest element. Start from the version below, which is correct but wasteful, and improve it.

```scheme
(define largest
  (lambda (L)
    (if (null? (cdr L))
        (car L)
        (if (>= (car L) (largest (cdr L)))
            (car L)
            (largest (cdr L))))))
```

Look closely at that second branch: `(largest (cdr L))` appears **twice**, once in the `if` test and once again if the test fails. Scheme does not remember the answer from the first call; it walks all the way to the end of the list and back a second time, from scratch, just to get a value it already computed once. The improvement is not a style preference. Count the recursive calls each version makes on `'(1 2 3 4 5 6 7 8)`, where the largest element is last, and report both numbers. Your write-up should explain the difference in terms of what gets recomputed, not in terms of which one looks nicer.

As a hint, if you could add a statement to the lambda that is `(let ((X y)) ...)`, where `X` is a variable name and `y` is an expression, what expression would you bind to `X` so that it only gets computed once? The primer below, right before Part 4, introduces `let` if you have not used it much yet; skim it now if this hint does not click.

5. **The empty-list question**: `sumlist` from Part 1 errors on `'()`. Fix it so it returns 0, and then argue in two or three sentences whether that was a bug in `sumlist` or a deliberate choice about what summing nothing should mean. There is a defensible answer either way; I am grading the argument.

---

## Part 3: Functions as Values (18 points)

Put these in `higher_order.scm`.

6. **`y` and a projectile**: write the linear equation as a function of three parameters, then use it and `square` together.

```scheme
(define y
  (lambda (m x b)
    (+ (* x m) b)))

(y 5 6 7)                    ; 37
```

Now do the same for projectile motion. With `v0` the initial velocity, `t` the time, and `a` the acceleration, the distance is `v0*t + 0.5*a*t^2`. Write it twice: once with `(* t t)` written out, and once with your `square` from Part 1 substituted in. Confirm the two agree, then say in one sentence what substituting `square` bought you, given that it did not change the answer. Finally, use `map` to compute the distance at `t` values `'(1 2 3 4 5)`; you will need a one-argument lambda that closes over `v0` and `a`.

7. **`plusminus`**: given two numbers, return a two-element list of their sum and their difference, using an anonymous `lambda` applied immediately:

```scheme
(define plusminus
  (lambda (a b)
    ((lambda (x y) (list (+ x y) (- x y)))
     a b)))

(plusminus 6 2)              ; (8 4)
```

Run it, then draw (on paper, and describe in your write-up) how `a` and `b` bind to `x` and `y` in that inner lambda.

8. **`oplist`**: write a function that accepts a list *and an operator* as parameters. Apply that operator to the whole list recursively: if the operator is `+`, return the sum; if it is `*`, return the product. Demonstrate it on at least three operators, one of which is a function you define yourself. Then compare your result against `(apply * (list 2 4 6))` and say when the two would disagree.

9. **`make-counter`**: write a function that returns a counter function. Each call to the returned function gives the next number, and two counters made separately must count independently.

```scheme
(define (make-counter)
  (let ((count 0))
    (lambda ()
      (set! count (+ count 1))
      count)))
```

Run it with two counters interleaved. Then answer in your write-up: what exactly did each returned function capture, and where does that captured value live once `make-counter` has returned? Compare a closure with an object in two or three sentences.

That `(let ((count 0)) ...)` at the top of `make-counter` is the same `let` the primer below covers in more depth: it is what gives this counter a private variable that nothing outside the function can see or reset. If you have not written `let` before this exercise, read the primer first and come back.

---

## Tools You'll Need First: `let`, Association Lists, `assq`, and a Second Look at `map` and `apply`

Part 4 assembles an evaluator out of four ingredients: `let` to name a value once, an association list to store lookups, `assq` to search that list, and `map`/`apply` to spread work across a list. We used `map` and `apply` once already in Part 1's Example 4, and `let` once already in `make-counter` above, but this section slows each one down, gives it a worked example, and gives you a one-line practice step to run at your REPL before you meet it again, wired together, in the evaluator. **These practice steps are ungraded**, the same as the Scheme warmup exercise in Part 1; nothing here goes in a deliverable, but running each one is the fastest way to make sure Part 4 does not stall on syntax you have not typed yet.

### `let`: naming a value once

Every expression you have written so far names things only two ways: as a function parameter, or with a top-level `define`. `let` gives you a third way, a name that exists only for the extent of one expression, which is exactly what you need when a value is used more than once inside a function body and you do not want to compute it twice.

The shape is `(let ((name expression)) body)`. It evaluates `expression` once, binds it to `name`, and then evaluates `body` with that binding visible.

```scheme
(let ((x (+ 2 3)))
  (* x x))                   ; 25
```

Read that as: compute `(+ 2 3)`, call the result `x`, then compute `(* x x)` using that `x`. The parentheses nest more deeply than you are used to, so build it from the inside out: `(x (+ 2 3))` is one binding pair, `((x (+ 2 3)))` is a list of one binding pair, and the whole `let` wraps that list around a body.

You can bind more than one name in the same `let` by adding more pairs:

```scheme
(let ((a 3)
      (b 4))
  (+ (* a a) (* b b)))       ; 25
```

Both `a` and `b` are computed from the *outside* environment, not from each other; if you need one binding to depend on another, that is `let*`, which we are not using here, so keep every binding in a single `let` independent of the others in this assignment.

> **Watch out!** A common typo is writing `(let (x (+ 2 3)) ...)` with one pair of parentheses missing. `let` always wants a *list of bindings*, so even a single binding needs its own extra parentheses: `((x (+ 2 3)))`, not `(x (+ 2 3))`. If Scheme complains that `x` is not a procedure, this is almost always why.

**Practice (ungraded):** at your REPL, bind a single name to `(* 6 7)` with `let` and use it twice in the body, once to print it and once to compare it against `42` with `=`. If you have already written `make-counter` in Part 3, you have already used `let` for real; this is just isolating it so the syntax is automatic before Part 4.

### Association lists: a list of pairs

An **association list**, usually just called an *alist*, is Scheme's simplest lookup table: a list where each element is a pair, `(key . value)`, built with `cons`.

```scheme
(define ops (list (cons '+ +) (cons '- -)))
```

`(cons '+ +)` builds the pair `(+ . #<procedure:+>)`, a symbol on the left and the actual addition procedure on the right; `car` of that pair gets you the symbol back, `cdr` gets you the procedure back. `ops` is then a list of two such pairs. Nothing here is a new data type: it is exactly the `list`, `cons`, `car`, and `cdr` from Part 1's Example 1, just arranged so that each element is itself a two-part `key . value` record.

**Practice (ungraded):** build a two-entry alist pairing the symbols `'red` and `'blue` with the strings `"stop"` and `"go"`. Use `car` and `cdr` on the first entry by hand to confirm you get `red` and `"stop"` back.

### `assq`: searching an alist

Writing `car`/`cdr` chains to search an alist by hand works, but Scheme gives you `assq` to do it directly. `(assq key alist)` walks the list looking for a pair whose `car` is `eq?` to `key`, and returns that whole pair if found, or `#f` if not.

```scheme
(define ops (list (cons '+ +) (cons '- -)))
(assq '+ ops)                ; (+ . #<procedure:+>)
(assq '* ops)                ; #f
```

Notice that `assq` gives you back the **pair**, not just the value; you still need `cdr` to pull the value out once you have found it:

```scheme
(cdr (assq '+ ops))          ; #<procedure:+>
```

That is the whole trick Way B below (and the evaluator's variable extension, if you choose it) relies on: look up a symbol with `assq`, then `cdr` the result to get the value that symbol was paired with. If the symbol is not in the list, `assq` returns `#f`, and your code needs to decide what to do about that. A common pattern is:

```scheme
(let ((found (assq '* ops)))
  (if found
      (cdr found)
      (error "not found:" '*)))
```

That `let` is doing exactly the job from the section above: `(assq '* ops)` only gets called once, its result is named `found`, and both the `if` test and the `error` branch reuse that name instead of calling `assq` a second time.

**`assq` versus `assoc`, and why this assignment uses `assq`.** Scheme actually gives you two searching functions, `assq` and `assoc`, and they differ in exactly one way: `assq` compares keys with `eq?`, an identity comparison, while `assoc` compares keys with `equal?`, a structural comparison. For symbol keys like `'+`, `'-`, or a variable name like `'x`, the two never disagree, because the reader interns every symbol it reads, so two occurrences of `'+` are already the same object in memory; `assq` is the correct and cheaper tool whenever your keys are symbols. `assoc` earns its keep once your keys are lists, strings, or other structured data, where two values can be `equal?` (same contents) without being `eq?` (same object):

```scheme
(define points (list (cons '(0 . 0) "origin")))

(assq  '(0 . 0) points)      ; #f  -- eq? sees two DIFFERENT list objects
(assoc '(0 . 0) points)      ; ((0 . 0) . "origin")  -- equal? compares structure
```

Every lookup table you build in this assignment, both `ops` here and the variable bindings in Part 4's optional extension, uses symbol keys, so `assq` is the right and sufficient choice throughout; you should not need `assoc` anywhere in this assignment, but it is worth knowing the difference exists so a future lookup table with list or string keys does not silently miss every match the way `assq` would.

**Practice (ungraded):** using the `'red`/`'blue` alist you built above, call `assq` for `'red` and confirm you get the pair back, then call it for a key that is not in the list and confirm you get `#f`.

### `map`, once more

You have already seen `map` twice, once in Part 1's Example 4 and once in the `plusminus`/projectile work in Part 3. The one habit worth locking in before Part 4: `map`'s first argument is always a *function*, never a function call. `(map square '(1 2 3))` passes the function `square` itself into `map`, which then calls it once per element; `(map (square 1) '(1 2 3))` would try to call `square` first, get back a number, and then try to use that number as if it were a function, which fails.

```scheme
(map square '(1 2 3))        ; (1 4 9)
```

`map` always returns a list the same length as its input, with each element replaced by the function's result on that element. When the elements of that input list are themselves further expressions, `map` will call your function once per expression, and if that function happens to be one that can handle a nested expression itself, the nesting gets handled automatically, one layer at a time. That is the exact role `map` plays in Part 4's Step 2.

**Practice (ungraded):** call `(map square '(2 (+ 1 2) 4))` and read the error carefully; `square` only knows how to multiply a number by itself, so it cannot handle the middle element, which is a list, not a number. Keep that error in mind; Part 4's evaluator is built specifically so that the function you `map` over a list of sub-expressions knows how to handle *both* numbers and nested lists, which is why `evaluate` mapping over itself will not hit this error the way `square` just did.

### `apply`, once more

`apply` takes a function and a list, and calls the function with the list's elements spread out as separate arguments, rather than as one list argument.

```scheme
(apply + '(1 2 3))           ; same as (+ 1 2 3), which is 6
(+ '(1 2 3))                 ; error: + does not want a list as an argument
```

That second line is worth trying on purpose: `+` wants numbers, not a list of numbers, so calling it directly on a list fails, and `apply` is exactly the tool that unpacks the list into individual arguments first. This matters for Part 4 because after `map` evaluates every operand down to a plain number, you are left holding a procedure and a list of numbers, precisely the two things `apply` wants.

**Practice (ungraded):** call `(apply * '(2 3 4))` and confirm you get `24`, then call `(* '(2 3 4))` directly and read the error it produces.

### Putting the four together

Here is a small, complete example that uses all four forms from this section at once, entirely separate from the evaluator, so you can see them cooperate before Part 4 asks you to write something similar:

```scheme
(define ops (list (cons '+ +) (cons '- -) (cons '* *) (cons '/ /)))

(define lookup
  (lambda (sym)
    (let ((found (assq sym ops)))
      (if found
          (cdr found)
          (error "not found:" sym)))))

(apply (lookup '*) (map square '(2 3 4)))   ; (* 4 9 16) = 576
```

Walk that last line from the inside out: `map` squares each element of `'(2 3 4)`, giving `(4 9 16)`; `lookup` searches `ops` with `assq` for the symbol `'*`, using a `let` so `assq` is only called once, and returns the multiplication procedure; `apply` then calls that procedure with the three squared numbers spread out as arguments. That is, in miniature, exactly the three-step shape Part 4 asks you to build, just with a fixed operator and a fixed list instead of a nested expression tree.

**Practice (ungraded):** run the block above as written, then change `'*` to `'+` and confirm the result changes to `29`. If both run correctly, you have every piece Part 4 needs.

---

## Part 4: An Expression Evaluator (22 points)

Write this one in `evaluate.scm`. It is about fifteen lines, and it is the oldest program in this language's history: John McCarthy's 1960 paper defined Lisp by writing an evaluator for Lisp in Lisp, and every interpreter you have ever used is a descendant of that idea. You are going to write the arithmetic-sized version of it in your first week.

### The representation

An arithmetic expression is a **nested list**, written exactly the way Scheme writes its own code. The `car` is the operator symbol; the `cdr` is the list of operands. A number is a leaf and stands for itself.

So `(* (+ 2 3) 4)` is this list:

```
'(* (+ 2 3) 4)              *
 ├─ car:  *                / \
 └─ cdr: ((+ 2 3) 4)      +   4
                         / \
                        2   3
```

That picture on the right is a **syntax tree**, and it is worth knowing now that you will meet it again. Later in this course, the Parser assignment's entire job is to build that same tree out of the flat text `(2 + 3) * 4`. Scheme hands it to you for free, because Scheme's source code *is* the tree. That is the trade the language made, and it is why the evaluator fits in fifteen lines here and does not there.

### The shape of the solution

Every recursion in Part 2 had the same two-case shape, and so does this one:

```scheme
(define evaluate
  (lambda (expr)
    (if (number? expr)
        expr                     ; base case: a number evaluates to itself
        ...)))                   ; recursive case: expr is a list
```

The recursive case has three steps. Work them in this order, and notice that each step reaches directly for one of the tools from the primer above.

**Step 1: get the operator — and read this part twice.**

```scheme
(car '(+ 1 2))                   ; +
```

That looks like it gave you addition. It did not. It gave you the **symbol** `+`, which is a name, not the procedure that adds. Try `((car '(+ 1 2)) 1 2)` in your REPL and read the error; this is the single place everyone loses twenty minutes on this assignment, and you may as well lose it on purpose now.

You need to turn the symbol into the procedure. Two ways, and you should understand both; both were previewed in the primer above.

```scheme
; Way A: dispatch with cond
(define lookup-op
  (lambda (sym)
    (cond ((eq? sym '+) +)
          ((eq? sym '-) -)
          ((eq? sym '*) *)
          ((eq? sym '/) /)
          (else (error "unknown operator:" sym)))))

; Way B: an association list, searched with assq
(define ops (list (cons '+ +) (cons '- -) (cons '* *) (cons '/ /)))

(define lookup-op
  (lambda (sym)
    (let ((found (assq sym ops)))
      (if found
          (cdr found)
          (error "unknown operator:" sym)))))
```

Way B is precisely the `ops`/`lookup` pattern from the "putting the four together" example in the primer, with the error message reworded to name the operator. Look at what Way B is: a list whose values *are procedures*. That is Part 3's "functions as values" doing load-bearing work rather than sitting in an exercise. Either way is acceptable; say in your write-up which you chose. If you choose Way B, the `let` inside `lookup-op` is there for the same reason it was in Part 2's `largest`: `(assq sym ops)` is used twice, once in the `if` test and once in the `cdr`, so it is computed once and named, not called twice.

**Step 2: evaluate the operands.** Each operand may itself be a whole expression, so each one needs the same treatment, which is to say, `evaluate` calls itself:

```scheme
(map evaluate (cdr expr))        ; ((+ 2 3) 4)  =>  (5 4)
```

This is the same `map` from Part 1's Example 4 and from the primer above, except the function you are passing it is `evaluate` itself, the very function you are in the middle of writing. Compare this against the practice step in the primer where `(map square '(2 (+ 1 2) 4))` failed: `square` did not know what to do with a list. `evaluate` is written specifically so that it *does* know what to do with a list, because that is exactly its recursive case, which is why mapping `evaluate` over a mix of numbers and sub-expressions works where mapping `square` did not.

**Step 3: apply.** You now hold a procedure and a list of numbers, which is exactly what `apply` takes:

```scheme
(apply + '(5 4))                 ; 9
```

This is the same `apply` from the primer's `(apply * '(2 3 4))` practice step, just with the procedure coming from `lookup-op` instead of being written literally.

Assemble those three steps and you are done:

```scheme
(define evaluate
  (lambda (expr)
    (if (number? expr)
        expr
        (apply (lookup-op (car expr))
               (map evaluate (cdr expr))))))
```

### Required test cases

Run all of these and capture the output:

```scheme
(evaluate '(+ 1 2))                        ; 3
(evaluate '(* (+ 2 3) 4))                  ; 20
(evaluate '(- (* 6 7) (/ 10 2)))           ; 37
(evaluate '(+ 1 (* 2 (- 10 (/ 8 4)))))     ; 17   <- nested three deep
(evaluate 42)                              ; 42   <- the base case, on its own
```

Then add **one edge case you chose deliberately**, and say in your write-up why you picked it and what it told you.

### Required: the unknown operator

What should `(evaluate '(+ 1 (& 2 3)))` do? Your evaluator must **detect the unknown operator and report it**, naming the offending symbol, rather than crashing with whatever Scheme says by default. `error` is the procedure you want, and `lookup-op`'s `else` branch (Way A) or its `if found ... (error ...)` branch (Way B) is where that detection lives. This is your first error message as a language implementer, and the standard it has to meet is the one you will be held to in the Lexer and Parser assignments: say what was wrong, and say which thing was wrong.

### Required: one extension, your choice of two

Pick **one** and make it work:

- **Any number of arguments.** Make `(evaluate '(+ 1 2 3 4))` return `10`. If you built Step 3 with `apply`, check whether this already works, and if it does, say why in one sentence rather than changing code. Hint: `apply` spreads however many elements are in the list you give it, whether that is two or five.
- **Variables.** Give `evaluate` a second parameter, an association list of bindings, so that `(evaluate '(+ x 1) '((x . 5)))` returns `6`. Look symbols up with `assq`, the same way `lookup-op` does, and decide what happens when a variable is not bound. Be warned that you are building an *environment* here, the same structure the Interpreter assignment builds later, and the same one the Environments and Scope lab makes you get right. Your recursive call to `evaluate` will need to pass the same `env` along every time, which means the one-argument function you hand to `map` will need to be a `lambda` that closes over `env`, the same closure idea from `make-counter` in Part 3.

### What to write up

In `writeup.md`:

- How many lines is your `evaluate`? Count them.
- What is `(map evaluate (cdr expr))` doing that a `for` loop over the operands would not? Answer in terms of the nesting, not in terms of style.
- Where does the recursion bottom out, and how do you know it terminates on every well-formed expression?
- If you used `let` or `assq` anywhere in `evaluate.scm` or `lookup-op`, say where and why; if you did not use them at all, say what you used instead.

---

## Deliverables

Submit a ZIP containing `part0.md` (both loop versions, their output, and your readability argument), `setup.md` (route, version, four transcripts, one error), `recursion.scm`, `higher_order.scm`, `evaluate.scm`, and a `writeup.md` answering the questions raised in Parts 2, 3, and 4. Include the output of each `.scm` file, either captured in a comment at the bottom of the file or pasted into the write-up. The primer's practice steps are ungraded and do not need to be submitted.

## Grading Breakdown

| Component                       | Points  |
| -------------------------------- | ------- |
| Part 0: The Functional Rewrite   | 10      |
| Part 1: Getting Scheme Running   | 18      |
| Part 2: List Recursion           | 32      |
| Part 3: Functions as Values      | 18      |
| Part 4: An Expression Evaluator  | 22      |
| **Total**                        | **100** |

## Reflection Prompts

- Which was harder: getting Scheme installed, or getting your first recursion to terminate? What does your answer suggest about where the real cost of a new language sits?
- Name one thing that was genuinely easier here than it would have been in Python, and one thing that was genuinely harder.
- Your `evaluate` walks a syntax tree in about fifteen lines. Later in this course you will write a parser whose only job is to *build* that tree from flat text. Before you write it: how much code do you think that will take, and what exactly is the parser doing that Scheme did for you here? I will ask you to look back at your answer.
- Of `let`, `assq`, `map`, and `apply`, which one took the longest to feel natural, and what finally made it click?
- AI disclosure: list any generative-AI tools you used, for what, and how you verified the results (or state 'none').
- Approximately how many hours it took you to finish this (I will not judge you for this at all; I am simply using it to gauge if the assignments are too easy or hard)?

## Submission

In your submission, please include answers to any questions asked on the assignment page, as well as the questions listed below, in your README file. **If you wrote code as part of this assignment, please describe your design, approach, and implementation in a separate document prepared using a word processor or typesetting program such as LaTeX. This document should include specific instructions on how to build and run your code, and a description of each code module or function that you created suitable for re-use by a colleague.** In your README, please include answers to the following questions:

- Describe what you did, how you did it, what challenges you encountered, and how you solved them.
- Please answer any questions found throughout the narrative of this assignment.
- If collaboration with a buddy was permitted, did you work with a buddy on this assignment? If so, who? If not, do you certify that this submission represents your own original work?
- Please identify any and all portions of your submission that were not originally written by you (for example, code originally written by your buddy, or anything taken or adapted from a non-classroom resource). It is always OK to use your textbook and instructor notes; however, you are certifying that any portions not designated as coming from an outside person or source are your own original work.
- Approximately how many hours it took you to finish this assignment (I will not judge you for this at all...I am simply using it to gauge if the assignments are too easy or hard)?
- Your overall impression of the assignment. Did you love it, hate it, or were you neutral? One word answers are fine, but if you have any suggestions for the future let me know.
- **Using the grading specifications on this page, discuss briefly the grade you would give yourself and why. Discuss each item in the grading specification.**
- Any other concerns that you have. For instance, if you have a bug that you were unable to solve but you made progress, write that here. The more you articulate the problem the more partial credit you will receive (it is fine to leave this blank).

Please refer to the [Style Guide](https://www.billmongan.com/Ursinus-CS173/Style-Guide) for code quality examples and guidelines.
