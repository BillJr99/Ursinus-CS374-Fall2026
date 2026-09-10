---
layout: assignment
permalink: /Assignments/LambdaCalculusLab
title: "CS374: Principles of Programming Languages - Lab: Lambda Calculus"

info:
  coursenum: CS374
  purpose: "To evaluate lambda calculus expressions by hand with a partner, working beta reduction with capture-avoiding substitution and Church encodings of booleans and numerals, which are the theory floor beneath functional programming."
  tilt:
    task: "With a partner, carry out step-by-step beta reductions including a capture-avoidance case, and verify Church-encoded booleans and numerals by reduction."
    criteria: "I assess your work on correct, fully-shown reduction sequences and correct Church-encoding verifications, weighted 55/45 across the two parts.  Please read the rubric below for the details."
  points: 15
  goals:
    - To perform beta reduction step by step, identifying redexes and applying capture-avoiding substitution
    - To verify Church encodings of booleans and numerals by reduction
    - To connect lambda calculus to the closures and higher-order functions of the surrounding course
  rubric:
    - weight: 10
      description: "Part 0: Before You Start - Beta Reduction and Church Encodings"
      preemerging: No reductions are attempted
      beginning: A reduction is attempted but the steps are not shown individually
      progressing: Both reductions are carried out step by step, but the non-terminating case is not explained, or the SUCC ZERO verification is incomplete
      proficient: (lambda x. lambda y. x) a b is beta-reduced to normal form with every step written out; the self-application case is reduced far enough to show why it never terminates, and that is explained; SUCC ZERO is verified by reduction to behave like ONE; and the step you were least confident was legal is marked
    - weight: 50
      description: "Beta Reduction (Goal 1)"
      preemerging: Reductions are missing or skip directly to claimed answers with no steps
      beginning: Simple reductions are correct but the capture-avoidance case substitutes blindly, capturing the free variable
      progressing: All reductions are correct including the alpha-renaming, but redexes are not marked or one sequence skips steps
      proficient: Every reduction is shown one beta-step at a time with the redex underlined or bracketed at each step, the capture case is handled by explicit alpha-renaming with a sentence explaining why, and the normal-order vs. applicative-order question is answered with the divergence example
    - weight: 40
      description: "Church Encodings (Goals 2, 3)"
      preemerging: Encodings are stated but never verified by reduction
      beginning: The boolean verifications are shown but the numeral ones are missing or incorrect
      progressing: All verifications are shown with one reduction error, or the connection question is unanswered
      proficient: TRUE/FALSE/AND and successor-of-one are all verified by complete reduction sequences, and the closing question connects Church encoding to a concrete higher-order-function idiom from the Functional Programming sessions
  readings:
    - rtitle: "Lambda Calculus I Activity"
      rlink: "Activities/liascript-lambdacalculus1.md"
      liapage: true
    - rtitle: "Lambda Calculus II Activity"
      rlink: "Activities/liascript-lambdacalculus2.md"
      liapage: true
    - rtitle: "Supplemental Tutorial: Build a Lambda Calculus Reducer"
      rlink: "../Tutorials/LambdaCalculusReducer"

tags:
  - lambda-calculus
  - functional
  - theory
  - lab

---

In this lab you and a partner evaluate lambda calculus expressions by hand, the way the Lambda Calculus class sessions do at the board.  It is entirely on paper.  You leave with a page of reductions you carried out one step at a time, a capture case you handled by renaming a bound variable, and Church-encoded booleans and numerals you verified by reduction rather than by trust.  No later assignment imports this lab, so it stands alone, but it prepares you for two things.  The first is the Functional Programming assignment's Direction C, Church encodings in code, where the reductions you write here become the test cases your reducer has to reproduce.  The second is the closures material, where "a function that captures a variable" stops being mysterious once you have alpha-renamed by hand.  Give yourself enough time to work the reductions slowly.  Rushing them defeats the purpose.

**Pair policy.**  You may do this lab in pairs.  Reduce independently, then reconcile line by line; the disagreements are where the learning is.  Hand in one document between you, each naming the other, and you both receive the same grade.  You may also do this alone.

Five terms come up throughout, so here they are in one place:

- A *redex* is a subterm ready to reduce: a lambda applied to an argument, such as $$(\lambda x.\, x)\ y$$.
- *Beta reduction* contracts a redex by substituting the argument for the bound variable in the body.  One contraction is one beta-step.
- A term is in *normal form* when it contains no redexes.
- *Capture* happens when a free variable in the argument becomes bound by accident after substitution.
- *Alpha-renaming* changes a bound variable's name (with all its uses) to avoid capture.  It does not change the term's meaning.

---

## Before You Start

There is nothing to install for this lab.  You need pencil and paper, and one file (or one photo) to hand in at the end.

- Work through the Lambda Calculus I and Lambda Calculus II activities listed under Readings above.  Every encoding this lab uses comes from them.
- Have pencil, paper, and an eraser.  A second pen color is handy for underlining redexes.
- If you type your submission, use VS Code or any plain-text editor.  The [dev environment page]({{ site.baseurl }}/Tutorials/DevEnvironment) walks through installing one.  You do not need the terminal for this lab; if you want to make your folder from the command line anyway, the [shell primer]({{ site.baseurl }}/Tutorials/ShellForLanguageDev) covers the two commands below.
- The [Build a Lambda Calculus Reducer tutorial]({{ site.baseurl }}/Tutorials/LambdaCalculusReducer) is optional.  This lab does not need it.

### Step 0.1: Set Up the Deliverable

You may hand in either a typed Markdown file or a clear scan or photo of handwritten work; both are acceptable, as long as the handwritten version is legible.  Decide now, because the typed route needs a file and the handwritten route needs a camera.

> **Do this.**
> 1. Create a folder named `cs374-lambda` for this lab.  In VS Code, use File, Open Folder, and make a new folder there; from the terminal, run the two commands below.
> 2. **Typed route:** create a file named `reductions.md` inside `cs374-lambda`, and paste the skeleton in the `text` fence below into it.  Put both partners' names on the first line.
> 3. **Handwritten route:** write both partners' names at the top of the first sheet, and label every section and item number exactly as the skeleton does, so that I can find item 4 of Part 1 without hunting.  When you are done, photograph each page in good light with the page filling the frame, and confirm every symbol is readable on the photo before you submit.  Hand in one PDF named `reductions.pdf` with the pages in order, or images named `reductions-1.jpg`, `reductions-2.jpg`, and so on.

```bash
mkdir cs374-lambda
cd cs374-lambda
```

```text
Partners: <name one> and <name two>

## Part 0
### Item 1
### Item 2
### Least-confident step

## Part 1
### Item 1
### Item 2
### Item 3
### Item 4 (capture case)
### Item 5 (omega and evaluation order)

## Part 2
### Item 1
### Item 2
### Item 3
### Item 4 (closing question)
```

### Step 0.2: How to Type a Term

If you type, write every lambda term in display math so it renders on the page.  Open with `$$`, type the term, and close with `$$`.  Put each beta-step on its own line.  The pieces you need:

| What you want | Type this inside `$$...$$` |
|---------------|----------------------------|
| The symbol $$\lambda$$ | `\lambda` |
| A binder and its body, $$\lambda x.\, x$$ | `\lambda x.\, x` (the `\,` adds a small space after the dot) |
| Application, $$f\ x$$ | `f\ x` (a backslash-space keeps the gap) |
| An underlined redex | `\underline{...}` around the redex |
| A beta-step arrow, $$\to_\beta$$ | `\to_\beta` |
| An alpha-renaming arrow, $$\to_\alpha$$ | `\to_\alpha` |
| A name like $$\text{TRUE}$$ | `\text{TRUE}` |

For example, the line

```text
$$\underline{(\lambda x.\, x)\ y} \to_\beta y$$
```

renders as

$$\underline{(\lambda x.\, x)\ y} \to_\beta y$$

> **Watch out.**  Use `$$` on both sides every time.  A single `$` does not render on this site, and a term that does not render is a term I cannot grade.

> **Time budget.**  About two to three hours, most of it in one sitting with your partner.  Part 0 takes about half an hour, Part 1 about an hour, Part 2 about an hour, and the reconciliation with your partner fits inside those.

---

## Notation and a Worked Reduction

Read this section before Part 0.  It shows one reduction the way I want to see yours, and it collects the Church encodings you use in Part 2.

### A Worked Beta Reduction

Two conventions from the readings do most of the work.  Application associates to the left, so $$f\ a\ b$$ means $$(f\ a)\ b$$.  The body of a lambda extends as far right as it can, so $$\lambda x.\, x\ y$$ means $$\lambda x.\, (x\ y)$$.  With those in hand, here is a term that reduces to normal form in three steps.  The redex contracted at each step is underlined, and the justification follows each line.

$$\underline{(\lambda x.\, \lambda y.\, y\ x)\ a}\ (\lambda z.\, z)$$

Start: application is left-associative, so the only redex is the underlined one on the left.  The rightmost $$(\lambda z.\, z)$$ is a lambda with nothing applied to it, so it is not a redex.

$$\to_\beta \quad \underline{(\lambda y.\, y\ a)\ (\lambda z.\, z)}$$

Step 1: substitute $$a$$ for $$x$$ in the body $$\lambda y.\, y\ x$$.  No capture, because the argument $$a$$ contains no free $$y$$.

$$\to_\beta \quad \underline{(\lambda z.\, z)\ a}$$

Step 2: substitute $$(\lambda z.\, z)$$ for $$y$$ in the body $$y\ a$$.  No capture, because the body binds nothing.

$$\to_\beta \quad a$$

Step 3: substitute $$a$$ for $$z$$ in the body $$z$$.  The result $$a$$ has no redexes, so it is in normal form.

That is the whole format: one term per line, the redex underlined, the arrow labeled, and one phrase saying what was substituted for what and why no capture occurred.  When a capture would occur, you add an alpha step first, written like this on a term of its own (this one is not from the lab):

$$\lambda y.\, y\ w \quad \to_\alpha \quad \lambda v.\, v\ w$$

Alpha-renaming changes the bound $$y$$ and every use of it to a fresh name $$v$$, and leaves the free $$w$$ alone.  The term means the same thing before and after.

### Church Booleans

A Church encoding represents a value such as a boolean or a number as a lambda term, so that the calculus needs no built-in data at all.  A boolean is a function that chooses one of its two arguments:

$$\text{TRUE} = \lambda t.\, \lambda f.\, t$$

$$\text{FALSE} = \lambda t.\, \lambda f.\, f$$

$$\text{AND} = \lambda p.\, \lambda q.\, p\ q\ p$$

### Church Numerals

A numeral $$n$$ is a function that applies its first argument $$n$$ times to its second:

$$\text{ZERO} = \lambda f.\, \lambda x.\, x$$

$$\text{ONE} = \lambda f.\, \lambda x.\, f\ x$$

$$\text{TWO} = \lambda f.\, \lambda x.\, f\ (f\ x)$$

$$\text{SUCC} = \lambda n.\, \lambda f.\, \lambda x.\, f\ (n\ f\ x)$$

When a lab item names one of these, substitute its definition in full as your first line, then reduce.  A name is an abbreviation, not a redex.

---

## Your First 15 Minutes

Get one reduction into the right shape before you touch the graded items.

> **Do this.**
> 1. Read the worked reduction above once, start to finish, without writing anything.
> 2. Cover it.  On paper, reduce $$(\lambda x.\, \lambda y.\, y\ x)\ a\ (\lambda z.\, z)$$ yourself: one beta-step per line, the redex underlined on every line, and a phrase after each line saying what you substituted for what.
> 3. Uncover the worked version and compare line by line.
> 4. Open `reductions.md` (or your first sheet), find the `## Part 0` heading, and start Part 0 item 1.  It has the same shape as the term you just reduced.

> **Checkpoint.**  Your redo should match the worked trace step for step: three beta-steps, ending at $$a$$.  If you ended somewhere else, the usual cause is reading $$f\ a\ b$$ as $$f\ (a\ b)$$; reread the left-associativity convention and try again before you move on.

---

## Part 0: Before You Start - Beta Reduction and Church Encodings (10%)

Do this part first, before the rest of the lab.  Use pencil and paper, and write every step down.

Beta reduction is a rewriting rule.  You learn it by applying it slowly and recording each step.  Two reductions will do: one that reaches a normal form, and one that never will.  The second is why the lambda calculus is worth a unit of this course.

> **Do this.**
> 1. Beta-reduce $$(\lambda x.\, \lambda y.\, x)\ a\ b$$ to normal form, showing each step.  Then try $$(\lambda x.\, x\ x)\ (\lambda x.\, x\ x)$$ and explain what happens.
> 2. Using the Church encodings from the reading, verify by reduction that $$\text{SUCC}\ \text{ZERO}$$ behaves like $$\text{ONE}$$.  Begin by writing out both definitions in full, then reduce until the result matches $$\text{ONE}$$ up to the names of bound variables.
> 3. Go back over your steps and mark the one you were least confident was legal.  Circle it on paper, or write `<-- least confident` after it in the file, and add one sentence saying what made you unsure.

> **Paste into your submission.**  Under `## Part 0`: the full step-by-step reduction of item 1's first term to normal form; enough steps of the second term to show why it never terminates, with your explanation; the $$\text{SUCC}\ \text{ZERO}$$ verification under item 2; and the marked least-confident step with its sentence.

> **Bring to class.**  The reduction step you were least confident was legal.  Those are the steps we work through at the board, and capture-avoiding substitution (Part 1) is usually the reason one felt wrong.

---

## Part 1: Beta Reduction (50%)

In `reductions.md`, reduce each expression below to normal form.  Write one beta-step per line, and mark the redex you contract at each step by underlining or bracketing it.  Before each step, ask whether the substitution would capture a free variable; if it would, alpha-rename first.

> **Do this.**  Under `## Part 1`, one item per heading:
> 1. Reduce $$(\lambda x.\, x)\ y$$.
> 2. Reduce $$(\lambda x.\, \lambda y.\, x)\ a\ b$$.
> 3. Reduce $$(\lambda f.\, \lambda x.\, f\ (f\ x))\ (\lambda z.\, z + 1)\ 0$$.  Treat $$+$$ and the numerals as constants: they are not redexes, and $$0 + 1$$ stays written as $$0 + 1$$ (or you may simplify the arithmetic at the end, after the last beta-step).
> 4. **The capture case:** reduce $$(\lambda x.\, \lambda y.\, x)\ y$$.  Blind substitution captures the free $$y$$.  Alpha-rename first, show the renaming as its own $$\to_\alpha$$ line, and add one sentence explaining what would have gone wrong without it.
> 5. Reduce $$(\lambda x.\, x\ x)\ (\lambda x.\, x\ x)$$ three steps, then state what this term tells you about termination.  Then answer: given $$(\lambda x.\, z)\ ((\lambda x.\, x\ x)\ (\lambda x.\, x\ x))$$, which evaluation order (normal or applicative) terminates, and what does that imply about lazy evaluation?

For item 5, normal order reduces the leftmost outermost redex first, and applicative order reduces arguments before applying the function.  Work the term both ways on paper, a few steps each, before you write the answer.

> **Watch out.**  Item 4 is the one place in this lab where the obvious move is wrong.  Before you substitute, look at the argument's free variables and at the binder you are about to substitute under.  If a name appears in both places, rename the binder first.  The rubric row for this part turns on whether you renamed or captured.

> **Paste into your submission.**  Under `## Part 1`: five reduction sequences, one beta-step per line with the redex marked on every line; the $$\to_\alpha$$ line and its explanatory sentence under item 4; the three steps and the termination statement under item 5; and the normal-order versus applicative-order answer with the divergence example, under item 5 as well.

Remember from this part: every reduction is a sequence of single steps, each with its redex marked, and the capture case is the one place you must rename before you substitute.

---

## Part 2: Church Encodings (40%)

A Church encoding represents a value such as a boolean or a number as a lambda term, so that the calculus needs no built-in data at all.  Use the definitions from the Notation section above: $$\text{TRUE} = \lambda t.\, \lambda f.\, t$$, $$\text{FALSE} = \lambda t.\, \lambda f.\, f$$, $$\text{AND} = \lambda p.\, \lambda q.\, p\ q\ p$$, and the numerals $$\text{ZERO} = \lambda f.\, \lambda x.\, x$$, $$\text{ONE} = \lambda f.\, \lambda x.\, f\ x$$, $$\text{SUCC} = \lambda n.\, \lambda f.\, \lambda x.\, f\ (n\ f\ x)$$.

> **Do this.**  Under `## Part 2`, one item per heading:
> 1. Verify that $$\text{AND}\ \text{TRUE}\ \text{FALSE}$$ reduces to $$\text{FALSE}$$, showing every step.  Your first line expands all three names to their definitions.
> 2. Verify that $$\text{AND}\ \text{TRUE}\ \text{TRUE}$$ reduces to $$\text{TRUE}$$.
> 3. Verify that $$\text{SUCC}\ \text{ONE}$$ reduces to a term alpha-equivalent to $$\text{TWO} = \lambda f.\, \lambda x.\, f\ (f\ x)$$.
> 4. Close with a short answer: a Church numeral *is* a higher-order function, "apply $$f$$, $$n$$ times."  Name the Python or Scheme idiom from the Functional Programming sessions that does exactly this, and one place your team language or interpreter could use the same trick.

Two terms are alpha-equivalent when they differ only in the names of bound variables, so item 3 succeeds when your result matches $$\text{TWO}$$ after renaming.  If your final term has different binder names from $$\text{TWO}$$, add one $$\to_\alpha$$ line that renames them and ends exactly at $$\text{TWO}$$.

> **Paste into your submission.**  Under `## Part 2`: three complete reduction sequences, each starting from the expanded definitions and ending at the expected term (with a final $$\to_\alpha$$ line under item 3 if you needed one), and a short paragraph under item 4 naming the idiom and the place in your team language or interpreter where it applies.

Remember from this part: a verification is a complete reduction sequence that ends at the expected term, not a claim that it would.

---

## Deliverables

Submit `reductions.md` (or a scanned/photographed handwritten equivalent, legible) containing both parts, with both partners named at the top.

| File or artifact | What it shows | Rubric row |
|------------------|---------------|------------|
| `## Part 0` section of `reductions.md` (or `reductions.pdf`) | Both Part 0 reductions step by step, the non-terminating case explained, $$\text{SUCC}\ \text{ZERO}$$ verified, and the least-confident step marked | Part 0: Before You Start |
| `## Part 1` section | Five reductions, one beta-step per line with the redex marked, the capture case alpha-renamed with a sentence, and the evaluation-order answer with the divergence example | Beta Reduction (Goal 1) |
| `## Part 2` section | Three complete verifications ending at the expected term, and the closing answer connecting Church numerals to a higher-order-function idiom | Church Encodings (Goals 2, 3) |
| Partner names on the first line | Who did the work; both partners receive the same grade | All rows |

---

## Self-Check Before You Submit

- [ ] Both partners are named at the top (or "worked alone" is written there).
- [ ] Every reduction is one beta-step per line, with no two steps folded into one.
- [ ] The redex is underlined or bracketed on every line, not only the first.
- [ ] Part 1 item 4 has a $$\to_\alpha$$ line before the substitution, plus one sentence saying what capture would have done.
- [ ] Part 1 item 5 says which evaluation order terminates on the divergence example and what that implies about lazy evaluation.
- [ ] Every Part 2 verification starts from the expanded definitions and ends at the expected term, with a renaming line under item 3 if the binder names differ from $$\text{TWO}$$.
- [ ] Part 2 item 4 names a specific idiom from the Functional Programming sessions and a specific place in your team language or interpreter.
- [ ] The least-confident step from Part 0 is marked, and, if handwritten, every photo is readable.

---

## Grading Breakdown

This lab is worth 15 points, as the course schedule states.  Each part's weight below is a percentage of those 15 points, and the rubric rows use the same percentages.

| Component | Weight |
|-----------|--------|
| Part 0: Beta Reduction and Church Encodings | 10% |
| Part 1: Beta Reduction | 50% |
| Part 2: Church Encodings | 40% |
| **Total** | **100% (15 points)** |

---

## Reflection Prompts

- Which reduction did you and your partner disagree on, and what settled it?
- If you worked in a pair, who did what.  If you worked alone, note that instead.
- AI disclosure: list any generative-AI tools you used, for what, and how you verified the results (or state 'none').
- Approximately how many hours it took you to finish this lab (I will not judge you for this at all; I am simply using it to gauge if the labs are too easy or hard)?
