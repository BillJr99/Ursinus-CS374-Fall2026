---
layout: assignment
permalink: /Assignments/BNFWorkshop
title: "CS374: Principles of Programming Languages - Lab: BNF Workshop"

info:
  coursenum: CS374
  purpose: "To get early practice writing grammars while the stakes are still low: EBNF grammars for two small languages, a Chomsky-level classification, and a design-criteria argument.  Grammar writing is the skill the Parser stretch of the course leans on hardest."
  tilt:
    task: "With a partner, write EBNF grammars for two toy languages, classify a set of sample languages by Chomsky level, and argue one syntax design choice against the readability, writability, and reliability criteria."
    criteria: "I grade your work on correct and complete EBNF grammars, correct Chomsky classifications with reasons, and a design argument grounded in the course criteria, weighted 50/30/20 across the three parts.  See the rubric below for the full breakdown."
  points: 15
  goals:
    - To write EBNF grammars for small formal languages
    - To classify languages by Chomsky hierarchy level and justify each classification
    - To evaluate a syntax design choice against the readability, writability, and reliability criteria
  rubric:
    - weight: 10
      description: "Part 0: Before You Start - Syntax, BNF/EBNF, and Grammars"
      preemerging: No grammar of your own is drafted and no derivation is attempted
      beginning: A BNF grammar is drafted but it is not extended to EBNF, or no derivation is produced
      progressing: A BNF grammar is drafted and extended to EBNF and a derivation is given, but the write-up does not say what EBNF made shorter, or does not justify the non-generated string
      proficient: A BNF grammar of your own is drafted and extended to EBNF with a note on exactly what the EBNF notation bought you; a leftmost derivation of a generated string is shown; and a string the grammar cannot generate is given with an argument for how you know
    - weight: 45
      description: "EBNF Grammars (Goal 1)"
      preemerging: Grammars are missing or do not use BNF/EBNF notation
      beginning: One grammar is attempted but accepts clearly invalid strings or rejects clearly valid ones
      progressing: Both grammars are written and mostly correct, but one has an undefined nonterminal or accepts an edge case it should reject (or vice versa)
      proficient: Both grammars are complete and correct EBNF; every nonterminal is defined, repetition and optionality use EBNF operators rather than prose, and each grammar comes with three strings it accepts and two it rejects, verified by hand against the productions
    - weight: 27
      description: "Chomsky Classification (Goal 2)"
      preemerging: No classifications, or levels are assigned without reasons
      beginning: Some classifications are correct but reasons restate the level name rather than the structural property
      progressing: All classifications are correct but one or two reasons miss the structural property that forces the level (e.g., nesting requiring a stack)
      proficient: Every sample language is classified correctly with a one-sentence reason naming the structural property that forces its level (finite memory suffices; matching/nesting needs a stack; cross-serial constraints need more), and the write-up names which level the class language's tokens and its full syntax will each need
    - weight: 18
      description: "Design-Criteria Argument (Goal 3)"
      preemerging: No argument, or the argument does not reference the course criteria
      beginning: The argument names a criterion but does not connect the syntax choice to a concrete consequence for programmers
      progressing: The argument connects the choice to two criteria with concrete consequences but does not acknowledge the tradeoff
      proficient: The argument evaluates the choice against at least two of readability, writability, and reliability with concrete programmer-facing consequences, states the tradeoff plainly, and takes a defensible position
  readings:
    - rtitle: "Syntax and BNF/EBNF Activity"
      rlink: "Activities/liascript-syntaxbnf.md"
      liapage: true
    - rtitle: "Grammars and the Chomsky Hierarchy Activity"
      rlink: "Activities/liascript-grammars.md"
      liapage: true
    - rtitle: "Evaluating Languages Activity"
      rlink: "Activities/liascript-languageevaluation.md"
      liapage: true

tags:
  - grammars
  - syntax
  - theory
  - languages
  - lab

---

This **lab** is your first practice at writing grammars, done while the stakes are low.  You write two small EBNF grammars, classify five sample languages by Chomsky level, and make one design argument.  Grammar writing is the skill the Parser assignment leans on hardest, and the Grammar and Derivations Workshop later asks you to write a grammar for the real class language.  This lab is the warm-up on toy examples.  You do it on paper or in a Markdown file, and you do it with a partner.

A grammar is a set of rules that says which strings belong to a language.  BNF (Backus-Naur Form) is a notation for writing those rules.  EBNF (Extended BNF) adds operators for repetition, optional parts, and grouping, so the same rules take fewer lines.

**Pair policy.**  You may do this lab in pairs.  One partner proposes a production (a single grammar rule), and the other tries to break it with a string the rule handles wrongly.  Submit one document between you, with each of you naming the other, and you both earn the same grade.  Working alone is fine too.

See the course schedule for the assigned and due dates.  Derivation trees and ambiguity get their own treatment later, in class and in the Grammar and Derivations Workshop.  Here the job is to write grammars that draw the right boundary between strings that belong to the language and strings that do not.

---

## Getting Started

### What You Need

There is nothing to install and nothing to run for this lab.  You need:

- The three activities listed under Readings above.  Skim them before you start, and keep the grammar activity open while you work:
  - [Syntax and BNF/EBNF]({{ site.lia_viewer_url }}{{ site.raw_pages_url }}Activities/liascript-syntaxbnf.md)
  - [Grammars and the Chomsky Hierarchy]({{ site.lia_viewer_url }}{{ site.raw_pages_url }}Activities/liascript-grammars.md)
  - [Evaluating Languages]({{ site.lia_viewer_url }}{{ site.raw_pages_url }}Activities/liascript-languageevaluation.md)
- Pencil and paper, or any text editor for a Markdown file.  If you want VS Code set up the way the rest of the course uses it, the [dev environment page]({{ site.baseurl }}/Tutorials/DevEnvironment) walks through it, and the [shell primer]({{ site.baseurl }}/Tutorials/ShellForLanguageDev) covers making a folder and opening a file from the terminal.  Neither is required for this lab.
- A partner, if you want one.

> **Time budget.**  Plan on about two hours of grammar work plus the write-up: fifteen minutes for Part 0, about an hour for Part 1 (the configuration language takes longer than the phone directory), and twenty to thirty minutes each for Parts 2 and 3.  These are my estimates; the last reflection prompt asks how long it actually took.

### Your First 15 Minutes

Get one production written and attacked before you try to write a whole grammar:

1.  Read the EBNF reference and the worked grammar below.  Follow the leftmost derivation with your finger, one line at a time, until you can say which production each step used.
2.  Pick your Part 0 language (signed decimal numbers, or boolean expressions with `and`, `or`, and `not`) and write its first production on paper.  Start with the whole thing: `<number> ::= ...` or `<expr> ::= ...`.
3.  Hand the rule to your partner (or play both roles).  Find one string the rule accepts that it should not, or rejects that it should not.  Fix the rule.
4.  Create `grammars.md` from the skeleton in the submission section below, and copy that first rule into the Part 0 section.

That loop (write a rule, attack it with a string, fix the rule) is the whole workflow of this lab.  Once it works for one production, the rest repeat the same cycle.

### EBNF Notation Reference

A production has a nonterminal on the left, `::=` in the middle, and a sequence of symbols on the right.  A nonterminal is a name in angle brackets that has its own production, such as `<digit>`.  A terminal is a symbol that appears in the string itself, and you write it in quotes, such as `"-"`.  BNF gives you sequence, alternation, and recursion.  EBNF adds three operators on top of those.  Each one below is shown with a one-line comment and a one-line example.

```ebnf
(* Sequence: symbols on the right side must appear in this order. *)
<entry>  ::= <name> ":" <number>

(* Alternation: | separates choices; exactly one is used. *)
<sign>   ::= "+" | "-"

(* Repetition: { X } means zero or more copies of X. *)
<digits> ::= <digit> { <digit> }

(* Optionality: [ X ] means X appears once or not at all. *)
<number> ::= [ <sign> ] <digits>

(* Grouping: ( X | Y ) treats the alternatives as one unit inside a larger rule. *)
<pair>   ::= <number> ( "," | ";" ) <number>
```

Two habits keep grammars honest.  First, every nonterminal that appears on a right side must have its own production somewhere; an undefined nonterminal is the most common lost point in Part 1.  Second, "one or more" is `<x> { <x> }`, not `{ <x> }`; the second form also accepts nothing at all.

### A Worked Grammar to Pattern On

Here is a small language written in BNF, rewritten in EBNF, and then used for a leftmost derivation.  The language is a bracketed list of one or more unsigned integers, such as `[7]` or `[12,3]`.  Part 0 asks you to do exactly this sequence for a language of your own, so pattern on it.

The BNF version uses recursion for "one or more":

```ebnf
<list>   ::= "[" <items> "]"
<items>  ::= <int> | <int> "," <items>
<int>    ::= <digit> | <digit> <int>
<digit>  ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

The EBNF version replaces both recursive rules with `{ }`.  That is what the notation buys you: two productions disappear, and "one or more" reads as one line.

```ebnf
<list>   ::= "[" <int> { "," <int> } "]"
<int>    ::= <digit> { <digit> }
<digit>  ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

A leftmost derivation starts from the start symbol and, at each step, replaces the leftmost nonterminal using one production.  Derivations are easiest on the BNF form, because each step applies exactly one choice.  Here is `[12,3]`:

```text
<list>
=> [ <items> ]                    the only rule for <list>
=> [ <int> , <items> ]            second choice for <items>
=> [ <digit> <int> , <items> ]    second choice for <int>
=> [ 1 <int> , <items> ]          <digit> -> 1
=> [ 1 <digit> , <items> ]        first choice for <int>
=> [ 1 2 , <items> ]              <digit> -> 2
=> [ 1 2 , <int> ]                first choice for <items>
=> [ 1 2 , <digit> ]              first choice for <int>
=> [ 1 2 , 3 ]                    <digit> -> 3
```

Verification by hand, in the form Part 1 asks for.  Accepts: `[7]` (one item, one digit), `[12,3]` (derived above), `[0,0,0]` (repetition runs twice).  Rejects: `[]` (the `<items>` rule requires at least one `<int>`, so nothing can produce an empty inside), `[1,]` (after `,` the second choice for `<items>` demands another `<items>`, and no production yields the empty string).  Notice that each rejection names the production that blocks the string.  That is the argument Part 0 step 4 and Part 1 step 3 want.

The worked grammar says nothing about spaces, so `[12, 3]` with a space is not in its language.  Your Part 1 languages do contain spaces (`NAME: (610) 555-0123`), so decide how you treat them and say so in one line: either write them into the productions where they occur, or state that spaces between tokens are ignored.

### How to Prepare and Submit Your Writeup

You submit one file for the whole lab.  Name it `grammars.md`.  If you worked on paper, scan or photograph the pages into a single PDF named `grammars.pdf` instead, in the same section order, with both names on the first page.  Either way, put one `## Part N` heading per part so I can find each deliverable, and put every grammar and derivation inside a fenced code block (three backticks on their own line before and after).  Outside a code block, Markdown treats `<name>` as an HTML tag and `*` as italics, and your grammar vanishes from the rendered page.

Start `grammars.md` from this skeleton:

````text
# CS374 Lab: BNF Workshop

Partners: <your name> and <partner name>   (or: worked alone)

## Part 0: Syntax, BNF/EBNF, and Grammars

### BNF grammar (language: ...)
```
<grammar here>
```

### EBNF grammar and what got shorter
```
<grammar here>
```
One sentence on what the EBNF made shorter.

### Leftmost derivation (grammar from the reading: ...)
```
<derivation here, one step per line>
```

### A string the grammar cannot generate
The string, and how you know.

### Rule I am least sure about
Name the rule.

## Part 1: EBNF Grammars

### Phone directory entries
### Configuration language

## Part 2: Chomsky Classification

## Part 3: Design-Criteria Argument

## Reflection
````

The `> **Paste into your submission.**` box at the end of each part lists exactly what goes under that heading.

---

## Part 0: Before You Start - Syntax, BNF/EBNF, and Grammars (10%)

Do this part first, before the rest of the lab.  Fifteen minutes and a pencil will do it.  You may do this part alone even though the rest of this lab is pair work.

You can follow a grammar on a page without being able to write one.  Writing even a tiny grammar forces the decisions the reading makes look obvious: what counts as a terminal (a symbol that appears in the string itself), where the recursion goes, and what the notation is buying you.

### Step 0.1: Write a BNF Grammar for a Language You Choose

> **Do this.**
> 1. Pick a small language.  Signed decimal numbers works; so does a boolean expression with `and`, `or`, and `not`.
> 2. List the terminals first: the digits, the `.` and `-`, or the words `and`, `or`, `not` and the operand names.
> 3. Write one production per nonterminal using BNF only: sequence, `|`, and recursion.  No `{ }` or `[ ]` yet.
> 4. Write two strings the language should contain and check each one against your rules by hand, the way the worked derivation does.

### Step 0.2: Extend the Grammar to EBNF

> **Do this.**
> 1. Rewrite the grammar with `{ }` for repetition, `[ ]` for optional parts, and `( )` for grouping, wherever one of them replaces a recursive or duplicated rule.
> 2. Note in one sentence exactly what the EBNF made shorter.  Name the rule that disappeared or the choice that collapsed.

### Step 0.3: Produce a Leftmost Derivation

Take a short grammar from the reading and produce a leftmost derivation of one string it generates.  A leftmost derivation starts from the start symbol and, at each step, replaces the leftmost nonterminal (a symbol that still has a rule to apply) using one production.

> **Do this.**
> 1. Choose a grammar from the Syntax and BNF/EBNF or Grammars activity and say which one.
> 2. Choose a string it generates that is three to six symbols long.  Longer strings add lines without adding insight.
> 3. Write the derivation one step per line, always expanding the leftmost nonterminal, and label each line with the production you used, as in the worked example.

### Step 0.4: Give a String the Grammar Cannot Generate

> **Do this.**
> 1. Write a string that looks close to the language but is not in it (a near miss is more convincing than random characters).
> 2. Explain how you know.  Name the production that would have to produce the offending symbol, and say why no production can.

> **Bring to class.**  Bring the grammar you drafted, and mark the rule you are least sure about.  Rough edges are expected.  That uncertain rule is usually the best discussion of the day.

> **Paste into your submission.**  Under `## Part 0` in `grammars.md`:
> 1. Your BNF grammar in a fenced code block, with the language named.
> 2. Your EBNF grammar in a fenced code block, followed by the one-sentence note on what got shorter.
> 3. The leftmost derivation, one step per line, and which grammar from the reading you used.
> 4. The string the grammar cannot generate, with your argument.
> 5. The name of the rule you are least sure about.

---

## Part 1: Two EBNF Grammars (45%)

Write a complete EBNF grammar for each language below in `grammars.md`.  Then verify each grammar by hand with three strings it accepts and two it rejects.  Use EBNF's operators for repetition (`{ }`), optionality (`[ ]`), and grouping.  The point of the exercise is to express shape in the notation rather than in prose.

### Step 1.1: Phone Directory Entries

Lines of the form `NAME: (610) 555-0123` or `NAME: 555-0123`, where a name is one or more capitalized words.  The area code is optional; the punctuation is not.  For example, both of these lines belong to the language:

```text
Ada Lovelace: (610) 555-0123
Grace Hopper: 555-0123
```

> **Do this.**
> 1. Start from the whole line: `<entry> ::= <name> ":" ...` and work downward.
> 2. Define `<name>` as one or more capitalized words.  "One or more" needs `{ }` next to a required first copy.
> 3. Make the area code optional with `[ ]`, and keep its parentheses and the hyphen required.
> 4. Define every nonterminal you used, down to terminals: `<word>`, `<capital>`, `<letter>`, `<digit>`.
> 5. Decide how spaces are handled (in the productions, or ignored between tokens) and write that down in one line.

> **Watch out.**  A `<name>` rule written as `{ <word> }` accepts an entry with no name at all.  Write `<word> { <word> }` for one or more.

### Step 1.2: A Tiny Configuration Language

Zero or more lines of `key = value;`, where a key is an identifier, and a value is an integer, a quoted string, or a bracketed comma-separated list of values.  Lists nest.  For example:

```text
port = 8080;
name = "server one";
themes = ["dark", ["contrast", "high"]];
```

> **Do this.**
> 1. Start at the top: `<config> ::= { <line> }`, since zero lines is a legal configuration.
> 2. Define `<line>` as a key, `=`, a value, and the required `;`.
> 3. Define `<key>` as an identifier: a letter or underscore, then any mix of letters, digits, and underscores.
> 4. Define `<value>` with three alternatives: integer, quoted string, and list.
> 5. Define the list alternative in terms of `<value>` again.  That recursion is what makes `["dark", ["contrast", "high"]]` legal.
> 6. Decide whether an empty list `[]` is legal and make the grammar say so with `[ ]` around the item sequence, or leave it out on purpose.
> 7. Define every remaining nonterminal down to terminals, and note your spacing decision as in Step 1.1.

> **Watch out.**  A `<value>` rule that lists only integers and strings accepts `themes = ["dark"];` and then fails on the sample line.  Trace the sample line through your productions before you call the grammar done.

### Step 1.3: Verify Each Grammar by Hand

> **Do this.**
> 1. For each grammar, choose three strings it should accept.  Make at least one of them hit a boundary: an optional part absent, or a repetition used zero times or many times.
> 2. Choose two strings it should reject.  Near misses (a missing `;`, a lowercase name, an unclosed bracket) are the useful ones.
> 3. For each accepted string, walk the productions and note the path in a few words.  For each rejected string, name the production that blocks it, as in the worked example.

> **Checkpoint.**  Before moving on, scan each right-hand side and confirm every nonterminal there has its own production, and every `{ }` and `[ ]` you wrote means what you intended.

> **Paste into your submission.**  Under `## Part 1`, with a `###` heading per language:
> 1. The phone directory grammar in a fenced code block.
> 2. Three accepted and two rejected strings for it, each with a one-line reason.
> 3. The configuration language grammar in a fenced code block.
> 4. Three accepted and two rejected strings for it, each with a one-line reason.
> 5. One line on how each grammar treats spaces.

---

## Part 2: Chomsky Classification (27%)

The Chomsky hierarchy ranks languages by how much memory a machine needs to recognize them.  Regular languages need only finite memory.  Context-free languages need a stack, because they match or nest symbols.  Languages with cross-serial constraints, such as equal counts in three separate places, need more than a stack.

### Step 2.1: Classify the Five Sample Languages

For each language below, name the lowest Chomsky level that can describe it.  Give a one-sentence reason that names the structural property forcing that level.

1.  Binary strings with an even number of 1s.
2.  Balanced parentheses.
3.  Your Part 1 configuration language (careful: the values nest).
4.  Identifiers matching `[A-Za-z_][A-Za-z0-9_]*`.
5.  Strings of the form `a^n b^n c^n` (equal counts of all three).

> **Do this.**
> 1. Make a table with three columns: Language, Lowest level, Reason.
> 2. For each language, ask what a recognizer must remember while reading the string.  A fixed amount of information (a parity bit, "have I seen the first character yet") means regular.  A count or a nesting that can grow without bound, but only needs to be unwound in reverse order, means context-free.  Constraints that link separate counts, so a stack cannot serve, mean higher than context-free.
> 3. Write the reason as the structural property, in one sentence.

> **Watch out.**  "It is context-free because it is a context-free language" restates the level name.  "Balanced parentheses need a stack to match each `)` to its `(`" names the property.  The rubric rewards the second form.

### Step 2.2: Tokens Versus Syntax in the Class Language

Close with one sentence for each of these three questions.  Which level do the class language's tokens need?  Which level does its full syntax need?  What does that split tell you about why compilers have both a lexer and a parser?

> **Do this.**
> 1. Think about what a token looks like (an identifier, a number, a keyword) and which level from Step 2.1 describes shapes like that.
> 2. Think about what a whole program looks like (nested expressions, blocks inside blocks) and which level that needs.
> 3. Write the three sentences.  The third should connect the first two.

> **Paste into your submission.**  Under `## Part 2`:
> 1. The classification table: five rows, each with a level and a one-sentence structural reason.
> 2. The three closing sentences on tokens, full syntax, and why compilers have both a lexer and a parser.

---

## Part 3: Design-Criteria Argument (18%)

The configuration language's designer proposes making the trailing `;` optional.  Write one paragraph that evaluates the proposal against at least two of the readability, writability, and reliability criteria from the Evaluating Languages session.  For each criterion, give a concrete consequence: what a programmer gains or loses.  State the tradeoff, and take a position.

### Step 3.1: Write the Argument

> **Do this.**
> 1. Pick at least two of readability, writability, and reliability.
> 2. For each one, write one concrete consequence for a person using the language: what they gain or lose when `;` becomes optional.  Think about a line that continues onto the next, a missing `;` that used to be an error, or a file someone else has to read.
> 3. State the tradeoff in one sentence: what the proposal gives up to get what it gains.
> 4. Take a position, for or against, and say why it follows from the consequences you named.

> **Watch out.**  "Readability improves" is a criterion name, not an argument.  The rubric wants the consequence: what specifically becomes easier or harder to read, and for whom.

> **Paste into your submission.**  Under `## Part 3`: the one paragraph, naming each criterion you used so I can find it.

---

## Deliverables

Submit `grammars.md` (or `grammars.pdf` if you worked on paper) containing all four parts, Part 0 through Part 3, with both partners named at the top.  Working alone, write "worked alone" instead.

| File or artifact | What it shows | Rubric row |
|------------------|---------------|------------|
| `## Part 0` section | Your BNF and EBNF grammar, the note on what got shorter, a leftmost derivation, and a non-generated string with an argument | Part 0 (10%) |
| `## Part 1` section | Two complete EBNF grammars, each with three accepted and two rejected strings verified by hand | EBNF Grammars (45%) |
| `## Part 2` section | Five classifications with structural reasons, plus the three sentences on tokens, syntax, and the lexer/parser split | Chomsky Classification (27%) |
| `## Part 3` section | One paragraph evaluating the optional `;` against at least two criteria, with the tradeoff and a position | Design-Criteria Argument (18%) |
| `## Reflection` section | Your answers to the Reflection Prompts below | Not weighted; I read them |

## Self-Check Before You Submit

- [ ] Both partners are named at the top of the file, or the file says "worked alone".
- [ ] Part 0 has a BNF grammar, its EBNF version, one sentence on what got shorter, a leftmost derivation with each step labeled, and a non-generated string with an argument.
- [ ] In every grammar, every nonterminal that appears on a right-hand side has its own production.
- [ ] Repetition and optionality are written with `{ }` and `[ ]`, not with words like "one or more".
- [ ] Each Part 1 grammar has three accepted and two rejected strings, each checked against the productions by hand, and the configuration grammar accepts the nested sample line.
- [ ] Every Part 2 reason names a structural property (finite memory, a stack, cross-serial constraints), and the three tokens-versus-syntax sentences are present.
- [ ] The Part 3 paragraph uses at least two criteria, gives a concrete consequence for each, states the tradeoff, and takes a position.
- [ ] The Reflection Prompts are answered, including the AI disclosure and the hours estimate.

## Grading Breakdown

This lab is worth 15 points, as the course schedule states.  Each part's weight below is a percentage of those 15 points, and the rubric rows use the same percentages.

| Component | Weight |
|-----------|--------|
| Part 0: Syntax, BNF/EBNF, and Grammars | 10% |
| Part 1: EBNF Grammars | 45% |
| Part 2: Chomsky Classification | 27% |
| Part 3: Design-Criteria Argument | 18% |
| **Total** | **100% (15 points)** |

## Reflection Prompts

- Which string broke your first draft of a grammar, and what production fixed it?
- If you worked in a pair, who did what, and name one thing your partner caught that you would have missed.  If you worked alone, note that instead.
- AI disclosure: list any generative-AI tools you used, for what, and how you verified the results (or state 'none').
- Approximately how many hours it took you to finish this lab (I will not judge you for this at all; I am simply using it to gauge if the labs are too easy or hard)?
