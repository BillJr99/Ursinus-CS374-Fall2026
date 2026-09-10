---
layout: assignment
permalink: /Assignments/GrammarWorkshop
title: "CS374: Principles of Programming Languages - Lab: Grammar and Derivations Workshop"

info:
  coursenum: CS374
  purpose: "To complete the Parser assignment's grammar work with a partner: write a full EBNF grammar for the class language, derive programs that prove it produces what you expect, and settle precedence decisions you can defend."
  tilt:
    task: "With a partner, write the EBNF grammar the Parser assignment's Part 1 requires, produce leftmost derivations and parse trees for two worked programs, and show how the grammar's shape enforces precedence and associativity."
    criteria: "I grade this on a complete and correct EBNF grammar, correct derivations with matching parse trees, and a demonstrated precedence and ambiguity analysis, weighted 50/25/25 across the three parts.  The rubric below has the details."
  points: 15
  goals:
    - To write a complete EBNF grammar for the class language's expressions and statements
    - To construct leftmost derivations and parse trees that verify the grammar against concrete programs
    - To explain how grammar structure (the expression ladder) enforces precedence and associativity and eliminates ambiguity
  rubric:
    - weight: 10
      description: "Part 0: Before You Start - Derivations, Ambiguity, and Precedence"
      preemerging: No parse trees are drawn
      beginning: One parse tree is drawn, so the ambiguity is asserted rather than shown
      progressing: Two distinct parse trees are drawn for one string, but the grammar is not rewritten to remove the ambiguity, or the associativity trees are missing
      proficient: Two distinct parse trees are drawn for one string of an ambiguous grammar; the grammar is rewritten so only one survives, with the place marked where encoding precedence made a rule harder to read; and both the left- and right-associative trees for 2 - 3 - 4 are drawn, with your language's actual choice confirmed in a REPL
    - weight: 45
      description: "EBNF Grammar (Goal 1)"
      preemerging: The grammar is missing most constructs or does not use EBNF notation
      beginning: The grammar covers expressions or statements but not both, or several productions reference undefined nonterminals
      progressing: The grammar is complete but flat, with no precedence levels, so it is ambiguous for arithmetic
      proficient: The grammar covers every expression and statement form of the class language in correct EBNF, with a tiered expression ladder (one production per precedence level) and no undefined nonterminals
    - weight: 23
      description: "Derivations and Parse Trees (Goal 2)"
      preemerging: No derivation is attempted, or the derivations do not follow the submitted grammar
      beginning: One program is derived but with skipped steps, or the parse tree does not match the derivation
      progressing: Both programs are derived with matching trees, but one derivation has a misapplied production
      proficient: Both worked programs have complete leftmost derivations, every step citing the production applied, with parse trees that match the derivations exactly
    - weight: 22
      description: "Precedence and Ambiguity Analysis (Goal 3)"
      preemerging: No analysis, or the analysis restates notes without using the submitted grammar
      beginning: The analysis asserts precedence works but shows no derivation-level evidence
      progressing: The analysis shows the correct tree for the precedence example but does not explain which grammar feature forces it
      proficient: The analysis derives the precedence example, names the exact productions that force multiplication to bind tighter than addition and subtraction to associate left, and shows what a flat one-level grammar would have permitted instead
  readings:
    - rtitle: "Recursive Descent Parsing Activity"
      rlink: "Activities/liascript-recursivedescent.md"
      liapage: true
    - rtitle: "Parsing Expressions Activity"
      rlink: "Activities/liascript-parsingexpressions.md"
      liapage: true

tags:
  - grammars
  - parsing
  - languages
  - lab

---

This **lab** is the Parser assignment's Part 1, done early and with a partner.  You write the EBNF grammar that your recursive-descent parser will transcribe function by function, and then you prove the grammar does what you think it does by deriving two real programs from it and drawing their parse trees.  Getting the grammar right on paper first pays off more than anything else you do in the Parser assignment, because every parsing function you write there is one production from this document.  The lab is due mid-assignment, before the parsing code gets serious.  You leave with one file, `grammar.md`, that goes straight into the [Parser assignment]({{ site.baseurl }}/Assignments/Parser).

**Pair policy.**  You may do this lab in pairs.  Grammar design benefits from argument: one partner proposes a production (a single grammar rule), and the other tries to break it with a program the rule derives wrongly.  Turn in the same document, each of you naming the other, and you will both get the same grade.  Working alone is allowed.  The Parser assignment remains individual work: you may both build on this shared grammar, but your parsers are your own.

---

## Before You Start

This is a paper lab.  The deliverable is one Markdown file, and the only program you run is a one-line REPL check in Part 0.  You need:

- The two activities linked at the top of this page (Recursive Descent Parsing and Parsing Expressions), read closely enough that the words production, nonterminal, terminal, and derivation are familiar.  The worked example below reviews them.
- A text editor that saves plain text.  VS Code or any editor works.
- Python 3.10 or newer for the REPL check.  If your machine isn't set up yet, follow the [dev environment page]({{ site.baseurl }}/Tutorials/DevEnvironment), and if the terminal is new to you, read the [shell primer]({{ site.baseurl }}/Tutorials/ShellForLanguageDev) first.

The [reference lexer]({{ site.baseurl }}/files/reference/reference-lexer.zip) is released with the Parser assignment, so it is available during this lab.  You don't need it for the paper work here.  If you want to confirm which tokens a program produces before you derive it, unzip it and run it on your two programs.  The usage policy is one line: any submission that builds on a reference component says so in its README, at no penalty.

### Create the Deliverable

Make a folder for this lab and create the file inside it.  Every part of the lab goes into this one file.

```bash
mkdir -p cs374-grammar
cd cs374-grammar
```

Now create `grammar.md` in that folder with your editor and start it with this outline.  The headings match the parts below, so I can find each piece when I grade it.

```text
# CS374 Lab: Grammar and Derivations Workshop

Partners: <your name>, <partner's name>   (or: worked alone)

## Part 0: Derivations, Ambiguity, and Precedence

## Part 1: EBNF Grammar

## Part 2: Derivations and Parse Trees

## Part 3: Precedence and Ambiguity Analysis
```

Two formatting rules that save you points.  Put every grammar in a fence labeled `ebnf` and every derivation and parse tree in a fence labeled `text` (three backticks, the label, your content, three backticks).  A tree drawn outside a fence collapses into a single line when Markdown renders it, and a collapsed tree is not a tree I can grade.  Open your file in your editor's Markdown preview before you submit and confirm the trees still look like trees.

Confirm Python is available for the Part 0 check:

```bash
python3 --version
```

```text
Python 3.11.4
```

Any version 3.10 or newer is fine; the exact number will differ from mine.

> **Time budget.**  Plan on about three hours in two sittings.  Part 0 takes under an hour and you can do it alone.  Parts 1 through 3 take one working session of about two hours with your partner, most of it on Part 1.

### Your First 15 Minutes

Start by making one derivation of your own, on a grammar smaller than the one you'll write, so the mechanics are settled before the real work.

1.  Read the worked example below once with a pencil, checking at every line that the nonterminal being rewritten is the leftmost one.
2.  Copy the three-line grammar from the example into a scratch section at the bottom of `grammar.md` (delete it before you submit).
3.  Derive a different string, `2 * 3 + 4`, step by step in the same format, and draw its tree.
4.  Compare with the example.  The `STAR` should sit under its own `term`, and the `PLUS` should be at the top of the tree, just as before, even though the multiplication now comes first in the input.

If step 4 came out that way, you understand precedence-by-grammar-shape and Parts 2 and 3 are the same move on a bigger grammar.  If it didn't, reread the example's note on how to apply a production with a `( ... )*` group, because that is where derivations usually go wrong.

### Suggested Pacing

See the course schedule for the assigned and due dates.  This lab lands inside the Parser assignment's window, and its due date is that assignment's first checkpoint.

| Checkpoint | You should have |
|------------|-----------------|
| On assignment | Part 0 done alone; partner chosen |
| Midpoint | Part 1 grammar drafted and attacked by your partner at least once |
| Due date | Parts 2 and 3 written; `grammar.md` previewed and submitted |

---

## Worked Example: One Derivation and Its Parse Tree

A derivation starts from the grammar's start symbol and rewrites one nonterminal per step until only terminals (tokens) remain.  A leftmost derivation always rewrites the leftmost nonterminal, which makes it unique for an unambiguous grammar and easy to check.  A parse tree is the same information drawn as a tree: each nonterminal becomes a node whose children are the right-hand side you chose for it.

Here is a three-production grammar for sums and products of integers.  Terminals are token names from your Lexer, in all caps.

```ebnf
expr    ::= term ( PLUS term )*
term    ::= factor ( STAR factor )*
factor  ::= INT | LPAREN expr RPAREN
```

One convention makes derivations over EBNF clean.  When you apply a production that contains a `( ... )*` group, you decide how many times the group repeats and write out every copy in that one step.  Cite the production and the repetition count.  Here is the leftmost derivation of `2 + 3 * 4`:

```text
Input:  2 + 3 * 4
Tokens: INT(2) PLUS INT(3) STAR INT(4)

expr
=> term PLUS term                  expr:    ( PLUS term )* used once
=> factor PLUS term                term:    ( STAR factor )* used zero times
=> INT PLUS term                   factor:  INT                (this INT is 2)
=> INT PLUS factor STAR factor     term:    ( STAR factor )* used once
=> INT PLUS INT STAR factor        factor:  INT                (this INT is 3)
=> INT PLUS INT STAR INT           factor:  INT                (this INT is 4)
```

Check the leftmost rule at line four: the sentential form was `INT PLUS term`, the only nonterminal left was `term`, so `term` is what got rewritten.  The last line is exactly the program's token sequence, which is how you know the derivation is finished.

The matching parse tree records the same six choices as nodes.  Drawn in ASCII, it looks like this:

```text
                    expr
              ________|________
             /        |        \
           term      PLUS      term
            |              _____|_____
            |             /     |     \
          factor       factor  STAR  factor
            |             |             |
          INT(2)        INT(3)        INT(4)
```

Read the tree from the bottom.  `3 * 4` sits under its own `term` node, one level below the `PLUS`, so the multiplication is grouped before the addition happens.  No rule anywhere says "multiplication first."  The shape of the ladder says it: `PLUS` lives in `expr`, `STAR` lives in `term`, and `expr` is built from `term`s, so a `STAR` can never sit above a `PLUS`.  Part 3 asks you to make this argument for your own grammar and to show what goes wrong without the ladder.

---

## Part 0: Before You Start - Derivations, Ambiguity, and Precedence (10%)

Do this part first, before the rest of the lab.  You may do it alone even though the rest of this lab is pair work.

A grammar is ambiguous when one string has two different parse trees.  Precedence says which operator binds tighter; associativity says how a chain of the same operator groups.  Ambiguity stops being subtle the moment you have drawn it twice.  Draw both trees, then rewrite the grammar until only one drawing survives.  That rewrite is the whole technique, and doing it once by hand teaches more than reading three descriptions of it.

### Step 0.1: Show That a Flat Grammar Is Ambiguous

Show that a given expression grammar is ambiguous by drawing two distinct parse trees for one string.  Use this flat grammar unless the class discussion handed you a different one:

```ebnf
expr ::= expr PLUS expr
       | expr MINUS expr
       | expr STAR expr
       | INT
```

> **Do this.**
> 1. Pick a string with at least three operands and two different operators, for example one that mixes `-` and `*`.  Do not reuse the `a + b * c` string that Part 3 draws for you.
> 2. Draw the first parse tree for it in a `text` fence under Part 0 in `grammar.md`.
> 3. Draw a second tree for the same string that groups the operators differently.  Both trees must follow the grammar above exactly: every node's children must be one of its four right-hand sides.
> 4. Under each tree, write the parenthesized expression it stands for and the value it computes.  If the two values differ, you have shown the ambiguity has a cost.

> **You should see.**  Two trees with the same leaves, in the same left-to-right order, with different internal shapes.  If you can only find one tree, your string probably has a single operator; add a second, different operator.

### Step 0.2: Rewrite the Grammar So Only One Tree Survives

Rewrite the grammar to encode precedence and associativity so the ambiguity is gone.  Mark the place where encoding precedence made a rule harder to read.  That cost is real, and Part 3 will ask you to defend paying it.

> **Do this.**
> 1. Write the rewritten grammar in an `ebnf` fence.  The worked example's ladder is the shape to imitate: one production per precedence level, each built from the level below it.
> 2. Redraw your Step 0.1 string under the new grammar.  Try to draw the second tree again and write one sentence saying which production now forbids it.
> 3. Mark the rule that got harder to read.  Add a comment on that line (EBNF comments are `//` to the end of the line, as the Parser assignment uses) that says what it used to say and why it changed.

> **Watch out.**  A rewrite that still has `expr` on both ends of a right-hand side, such as `expr ::= expr PLUS expr`, is still ambiguous no matter how many levels you add.  Each level should mention only itself (at most on one side) and the level below it.

### Step 0.3: Draw Both Associativities for 2 - 3 - 4

Take `2 - 3 - 4` and draw the parse tree that makes subtraction left-associative, then the one that makes it right-associative.  Which does your favorite language use?  Confirm it in a REPL rather than guessing.

> **Do this.**
> 1. Draw the left-associative tree, the one that groups `(2 - 3) - 4`, in a `text` fence.
> 2. Draw the right-associative tree, the one that groups `2 - (3 - 4)`, in a second `text` fence.
> 3. Compute both by hand and write the two values under the trees.
> 4. Ask your favorite language.  For Python, run the line below from the `cs374-grammar` folder.  For another language, evaluate the same expression in that language's REPL (for JavaScript, `node -e "console.log(2 - 3 - 4)"`).
>
> ```bash
> python3 -c "print(2 - 3 - 4)"
> ```

> **You should see.**  A single number.  `-5` means the language grouped left, `(2 - 3) - 4`.  `3` means it grouped right, `2 - (3 - 4)`.  Write down which tree the language agreed with and paste the command and its output into Part 0.

> **Paste into your submission.**  Under `## Part 0` in `grammar.md`: the two trees from Step 0.1 with their values; the rewritten grammar from Step 0.2 with the harder-to-read rule marked; the two `2 - 3 - 4` trees from Step 0.3; and the REPL command with its output and one sentence naming the associativity your language uses.

If the rewrite fell apart on you, bring it anyway.  Where it fell apart is what the discussion is for.

---

## Part 1: The EBNF Grammar (45%)

Write the complete EBNF grammar for the class language used across the Lexer, Parser, and Interpreter assignments.  Cover these constructs:

- `let`, assignment, and `print` statements
- `if`/`else`
- `while` with blocks
- expressions over numbers, strings, booleans, identifiers, calls, and the arithmetic, comparison, and logical operators

Structure the expression productions as a ladder: one production per precedence level, from `or` at the top down through `and`, comparison, additive, multiplicative, unary, and primary.  This is exactly the shape the Parser assignment's Part 2 transcribes into functions.

EBNF notation, for reference: `*` means zero or more, `+` means one or more, `?` means zero or one, `|` separates alternatives, and `( )` groups.  Terminals are your Lexer's token names in all caps.  A nonterminal is a rule you define; if a name appears on a right-hand side, it must appear on a left-hand side somewhere in the grammar.

### Step 1.1: Write the Statement Productions

Statements are the easier half, and finishing them first gives you a `program` production to hang everything else on.

> **Do this.**
> 1. Under `## Part 1` in `grammar.md`, open an `ebnf` fence and start from this skeleton.  Replace every `TODO` with a real right-hand side.
> 2. For each statement form, write down a two-line program that uses it and read your production against it token by token.  If your Lexer would produce a token that your production doesn't mention, the production is wrong.

```ebnf
program     ::= stmt* EOF

stmt        ::= let_stmt
              | assign_stmt
              | print_stmt
              | if_stmt
              | while_stmt
              | block

let_stmt    ::= TODO   // LET, a name, EQ, an expression, SEMICOLON
assign_stmt ::= TODO
print_stmt  ::= TODO
if_stmt     ::= TODO   // decide how an optional ELSE attaches, and to what
while_stmt  ::= TODO   // WHILE, a condition, then a block
block       ::= TODO   // LBRACE ... RBRACE
```

### Step 1.2: Write the Expression Ladder

The ladder is the part your parser transcribes one function per production, so its shape matters more than its length.  Each level is built out of the level below it and mentions only its own operators.

> **Do this.**
> 1. Continue the same `ebnf` fence with the ladder below, replacing each `TODO`.  `or_expr` is filled in to show the pattern; every binary level down to `multiplicative` has the same shape with different operator tokens.
> 2. Put calls where they belong.  A call such as `f(x, 1)` is a primary followed by an argument list in parentheses; you may give it its own level between `unary` and `primary` or fold it into `primary`, but say which in a comment.
> 3. When you're done, read every right-hand side and confirm every name in it is defined.  An undefined nonterminal is the most common way to lose points on this part.

```ebnf
expr           ::= or_expr
or_expr        ::= and_expr ( OR and_expr )*
and_expr       ::= TODO   // same shape, one level down
comparison     ::= TODO   // LT, LE, GT, GE, EQEQ, NEQ; decide whether chaining is allowed
additive       ::= TODO   // PLUS, MINUS
multiplicative ::= TODO   // STAR, SLASH
unary          ::= TODO   // prefix MINUS and NOT, then the level below
primary        ::= TODO   // literals, IDENT, and a parenthesized expr
```

> **Checkpoint.**  Hand the grammar to your partner and have them write a five-token program that the grammar derives wrongly or can't derive at all.  Every production that survives a real attempt at breaking it is one you won't have to reopen during the Parser assignment.  The first Reflection Prompt asks which production took the most rounds, so keep a tally.

> **Paste into your submission.**  Under `## Part 1`: the complete grammar in one `ebnf` fence, statements first and then the ladder, with a one-line comment on any production where you made a design decision (the `else` attachment, where calls live, whether comparisons chain).

---

## Part 2: Derivations and Parse Trees (23%)

Produce a leftmost derivation and the matching parse tree for each of these two programs.  Cite the production applied at every step of each derivation.

1. `let x = 1 + 2 * 3;`
2. `while x < 10 { x = x + 1; }`

These derivations use your Part 1 grammar, not the worked example's.  They are the proof that the grammar produces what you expect.  A derivation that does not follow the submitted grammar earns nothing, so if a step needs a production you don't have, fix the grammar in Part 1 and note that you did.

### Step 2.1: Write Down the Tokens

A derivation ends when the sentential form equals the program's token sequence, so you need that sequence before you start.

> **Do this.**
> 1. Under `## Part 2`, write each program in a `text` fence with its token sequence on the line below it, using your Lexer's token names (`LET IDENT EQ INT PLUS INT STAR INT SEMICOLON` is the shape for program 1).
> 2. Count the tokens.  Your derivation's final line must have exactly that many terminals, in that order.

### Step 2.2: Derive Program 1 and Draw Its Tree

> **Do this.**
> 1. Start from `program` and derive `let x = 1 + 2 * 3;` in a `text` fence, one `=>` line per step, in the format of the worked example.
> 2. At each step rewrite the leftmost nonterminal only, and write the production you applied at the right of the line, including how many times any `( ... )*` group was used.
> 3. Walk the ladder honestly.  Getting from `expr` down to the `INT` at the bottom passes through every level in between, even the ones with no operator at this input, and each pass is one cited step.
> 4. Draw the parse tree in a second `text` fence.  Every internal node is a nonterminal from your derivation; every leaf is a token.

> **You should see.**  A derivation whose last line is the nine-token sequence from Step 2.1, and a tree whose leaves read left to right as that same sequence.  Expect the derivation to run somewhat over a dozen lines because of the ladder; that length is correct, not a sign you did something wrong.

### Step 2.3: Derive Program 2 and Draw Its Tree

> **Do this.**
> 1. Derive `while x < 10 { x = x + 1; }` the same way.  This one exercises `while_stmt`, `block`, `assign_stmt`, and the `comparison` level.
> 2. When you rewrite `block`, decide how many statements the `stmt*` group produces (here, one) and cite it.
> 3. Draw the tree.  It will be wider than program 1's, so leave room and check it in the Markdown preview.

> **If it fails.**  The three usual problems:
> - The derivation skipped a ladder level.  Every level between `expr` and the leaf must appear, even when it has no operator at this input.
> - The tree has a node the derivation never produced, or is missing one it did.  They must match exactly.
> - The final line has the wrong number of terminals.  That almost always means a `SEMICOLON` or a brace was dropped.

> **Paste into your submission.**  Under `## Part 2`: for each program, its token sequence, its leftmost derivation with a production cited on every line, and its parse tree, all in `text` fences.

---

## Part 3: Precedence and Ambiguity (22%)

Using your derivation of program 1, explain which productions force `*` to bind tighter than `+`.  Show the wrong second tree that a flat single-level expression grammar would also permit.  Then state how your grammar makes `1 - 2 - 3` associate left, and verify with a three-line derivation sketch.

Here is what ambiguity looks like, so the "wrong second tree" you're asked for has a model.  Under this flat grammar, the string `a + b * c` has two parse trees:

```ebnf
expr ::= expr PLUS expr
       | expr STAR expr
       | IDENT
```

```text
   Tree A: a + (b * c)                    Tree B: (a + b) * c

               expr                                  expr
          _____/|\_____                         _____/|\_____
         /      |      \                       /      |      \
       expr    PLUS    expr                  expr    STAR    expr
        |          ____/|\____           ____/|\____          |
        |         /     |     \         /     |     \         |
    IDENT(a)    expr   STAR   expr    expr   PLUS   expr   IDENT(c)
                 |             |       |             |
             IDENT(b)      IDENT(c)  IDENT(a)    IDENT(b)
```

Same string, same grammar, two trees, two meanings.  Nothing in the flat grammar prefers Tree A, so a parser built from it has no basis for choosing, and that is what ambiguous means.  Your ladder is the fix: with `STAR` confined to a lower level than `PLUS`, Tree B has no derivation at all, because no production ever puts a `STAR` node above a `PLUS` node.

### Step 3.1: Name the Productions That Force Precedence

> **Do this.**
> 1. Go back to your Part 2 derivation of program 1 and find the step where `1 + 2 * 3` split at the `PLUS`, and the later step where `2 * 3` split at the `STAR`.
> 2. Write a short paragraph naming those two productions by name and explaining why the `STAR` step had to happen below the `PLUS` step: which production contains `PLUS`, which contains `STAR`, and which one is built from the other.

### Step 3.2: Draw the Wrong Tree a Flat Grammar Permits

> **Do this.**
> 1. Write a flat one-level grammar for `1 + 2 * 3` (the Part 0 or the example grammar above will do; say which).
> 2. Draw the tree that groups `(1 + 2) * 3` in a `text` fence and write its value next to the correct tree's value.
> 3. State in one sentence which production of your ladder makes this tree impossible.

### Step 3.3: Show That 1 - 2 - 3 Associates Left

> **Do this.**
> 1. State in one or two sentences how your grammar makes `1 - 2 - 3` group as `(1 - 2) - 3`.
> 2. Verify it with a three-line derivation sketch in a `text` fence: start at your additive level, apply its production once to expose both `MINUS` tokens, and show where the left group forms.  Three lines means a sketch, not a full derivation down to tokens.

> **Watch out.**  A `( MINUS multiplicative )*` group produces a flat list of three operands at one level, and a flat list by itself does not say which two group first.  Decide where the left grouping comes from, and say so in your analysis.  It can come from the grammar's shape: the left-recursive form `additive ::= additive MINUS multiplicative | multiplicative` puts the grouping in the tree.  Or it can come from the parser's left-fold loop that the Parser assignment describes for the `*` form.  Either is a defensible answer.  An analysis that doesn't say which one it's relying on isn't finished.

> **Paste into your submission.**  Under `## Part 3`: the precedence paragraph naming both productions; the flat grammar and its wrong tree with both values; the associativity statement; and the three-line sketch.

---

## Deliverables

Submit `grammar.md` containing all three parts, with both partners named at the top.  Bring it to the Parser assignment: its Part 1 asks you to include (and refine, if the coding surfaces issues) exactly this grammar.

| File or artifact | What it shows | Rubric row |
|------------------|---------------|------------|
| `grammar.md`, `## Part 0` | Two trees for one string, the disambiguated rewrite with the marked rule, both `2 - 3 - 4` trees, and the REPL confirmation | Part 0 |
| `grammar.md`, `## Part 1` | The complete EBNF grammar with a tiered expression ladder and no undefined nonterminals | EBNF Grammar |
| `grammar.md`, `## Part 2` | Leftmost derivations of both programs, every step cited, with matching parse trees | Derivations and Parse Trees |
| `grammar.md`, `## Part 3` | The precedence argument, the flat grammar's wrong tree, and the `1 - 2 - 3` sketch | Precedence and Ambiguity Analysis |

---

## Self-Check Before You Submit

- [ ] Both partners are named at the top of `grammar.md`, or the top says you worked alone.
- [ ] Part 0 has two distinct trees for one string, a rewritten grammar with the harder-to-read rule marked, both `2 - 3 - 4` trees, and the REPL command with its output.
- [ ] Every nonterminal that appears on a right-hand side in Part 1 is defined on a left-hand side.
- [ ] The expression ladder has one production per precedence level, `or` through `primary`, and covers every statement form in the Part 1 list.
- [ ] Both Part 2 derivations rewrite the leftmost nonterminal at every step, cite a production on every line, and end in exactly the program's token sequence.
- [ ] Each parse tree matches its derivation node for node.
- [ ] Part 3 names the productions that force precedence, shows the flat grammar's wrong tree, and includes the three-line `1 - 2 - 3` sketch with a stated source of left grouping.
- [ ] Grammars are in `ebnf` fences, derivations and trees are in `text` fences, and the Markdown preview shows the trees intact.

---

## Grading Breakdown

This lab is worth 15 points, as the course schedule states.  Each part's weight below is a percentage of those 15 points, and the rubric rows use the same percentages.

| Component | Weight |
|-----------|--------|
| Part 0: Derivations, Ambiguity, and Precedence | 10% |
| Part 1: EBNF Grammar | 45% |
| Part 2: Derivations and Parse Trees | 23% |
| Part 3: Precedence and Ambiguity Analysis | 22% |
| **Total** | **100% (15 points)** |

---

## Reflection Prompts

- Which production went through the most revisions before your partner could no longer break it, and what broke it last?
- If you worked in a pair, who did what, and name one thing your partner caught that you would have missed.  If you worked alone, note that instead.
- AI disclosure: list any generative-AI tools you used, for what, and how you verified the results (or state 'none').
- Approximately how many hours it took you to finish this lab (I will not judge you for this at all; I am simply using it to gauge if the labs are too easy or hard)?
