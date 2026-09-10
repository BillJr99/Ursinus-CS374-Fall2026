---
layout: assignment
permalink: /Assignments/Regex
title: "CS374: Principles of Programming Languages - Regular Expressions"

info:
  coursenum: CS374
  purpose: "To build a working command of regular expressions by writing a tested pattern library, a finditer-based mini lexer, and a realistic log parser, and to learn the vocabulary you need to explain why a pattern behaves the way it does."
  tilt:
    task: "Work through four scaffolded parts: a ten-pattern library, a re.finditer mini lexer, a regex text transformer and log parser, and a written analysis of regex limits."
    criteria: "I grade this on the correctness of your patterns, mini lexer, and log parser, and on the depth of your greedy/lazy, anchors, and Chomsky-limits analysis.  Each part is worth 25 points, and the rubric below spells out each row."
  points: 100
  goals:
    - To write and test a library of regular expressions for real-world data patterns
    - To build a mini lexer using re.finditer and a TOKEN_SPEC ordered list
    - To apply regular expressions to realistic log-parsing and data-extraction tasks
    - To articulate the difference between greedy and lazy quantifiers, anchors, and capture groups
    - To explain the theoretical limits of regular languages and connect them to the Chomsky hierarchy
  rubric:
    - weight: 25
      description: "Pattern Library (Goal 1)"
      preemerging: Fewer than five patterns are provided, or most patterns match clearly wrong strings on the provided test cases
      beginning: Most patterns are provided, but several fail on edge cases (e.g., missing anchors allow partial matches, or character classes are too broad or too narrow)
      progressing: All ten patterns pass the provided positive and negative test cases, but two or more patterns have minor issues that would fail on hidden test inputs (e.g., permitting leading zeros in integers, or not anchoring a pattern that should be anchored)
      proficient: All ten patterns pass all provided and hidden test cases; every pattern is a raw string; each pattern is named, each non-trivial construct has a one-sentence explanation, and each pattern is tested with at least three positive and two negative cases through the check() harness
    - weight: 25
      description: "Mini Lexer with re.finditer (Goal 2)"
      preemerging: The mini lexer is not implemented, or it uses re.match in a loop rather than re.finditer with alternation
      beginning: The mini lexer uses finditer, but the TOKEN_SPEC ordering is wrong (e.g., keywords are not listed before identifiers), so some inputs get incorrect token types
      progressing: The mini lexer produces correct token types for most inputs, but one or more token types are misclassified, and gaps between matches (unrecognized characters) are not detected
      proficient: The mini lexer uses a single compiled alternation pattern with named groups; produces the correct token type and value for every input; detects and reports gaps (unrecognized characters) with their position; and handles the maximal-munch ordering correctly for all test cases
    - weight: 25
      description: "Text Transformer and Log Parser (Goals 1, 3)"
      preemerging: Neither the transformer nor the log parser is implemented, or both produce clearly wrong output
      beginning: One of the two is implemented but produces incorrect output on several provided inputs (e.g., the date conversion uses the wrong group references, or the log parser drops some records)
      progressing: Both are implemented and produce correct output on the provided inputs, but the log parser does not handle malformed lines, or the transformer does not handle edge cases (e.g., dates at the start or end of a string)
      proficient: Both the text transformer and the log parser work correctly on all provided and hidden inputs; malformed log lines are detected and reported with their line number; the configuration lives in a JSON file; and the errors.txt output is generated correctly
    - weight: 25
      description: "Pattern Analysis and Limits Discussion (Goals 4, 5)"
      preemerging: No analysis is provided, or the analysis restates the course notes without applying the concepts to the student's own patterns
      beginning: The analysis addresses greedy vs. lazy and anchors, but the explanations are superficial and the examples do not clearly show the difference
      progressing: The analysis covers greedy vs. lazy, anchors, and groups with working examples, but the Chomsky hierarchy discussion is missing or incorrect
      proficient: The analysis demonstrates greedy vs. lazy with a concrete input where the two produce different results, explains anchors with a pattern that fails without them, explains named groups with groupdict(), and includes a correct paragraph on why balanced parentheses require a context-free grammar, naming the Chomsky level and the pipeline component that handles it
  readings:
    - rtitle: "Regular Expressions Activity"
      rlink: "Activities/liascript-regex.md"
      liapage: true
    - rtitle: "Python re Documentation"
      rlink: "https://docs.python.org/3/library/re.html"

tags:
  - regex
  - languages

---

In this assignment you write regular expressions, test them, and use them to build a small lexer, a text transformer, and a log parser.  A regular expression (regex) is a pattern that describes a set of strings, and Python's `re` module matches text against such patterns.  You leave with a tested library of ten patterns, a working `re.finditer` lexer that you grow again in the Lexer assignment, and the vocabulary to explain why a pattern behaves the way it does.  The assignment has four parts worth 25 points each.  I test each part on its own, so complete them in order.  Write every pattern as a raw string (`r"..."`) so that backslashes reach the regex engine unchanged.  Part 4 is a written analysis, and it ends with a question about what regular expressions cannot do; answer it in your writeup.

---

## Getting Started

### Environment and Setup

Before you start, you need:

- Python 3.10 or newer.  The `re` and `json` modules are part of the standard library, so there is nothing to install.
- A text editor (VS Code or any editor you like) and a terminal.  If the terminal is new to you, read the [dev environment page]({{ site.baseurl }}/Tutorials/DevEnvironment) and the [shell primer]({{ site.baseurl }}/Tutorials/ShellForLanguageDev) first; both are short.
- Your files from the Regex Workshop lab, if you have started it.

Confirm your Python version from the terminal:

```bash
python3 --version
```

> **You should see.** One line naming a version, such as the one below.  Any version 3.10 or newer is fine.  If the terminal says `python3` is not found (common on Windows), use `python` in place of `python3` in every command on this page.

```text
Python 3.12.3
```

> **Do this.**
> 1. Make a project folder for this assignment and move into it.  Every command on this page runs from inside this folder.
> 2. Create the six files below so each part has a home.  You can create them in your editor (save each new file into `cs374-regex/`) or with the `touch` command shown, which works in the macOS and Linux shells and in Git Bash on Windows.
>
> ```bash
> mkdir cs374-regex
> cd cs374-regex
> touch patterns.py mini_lexer.py transformer.py log_parser.py config.json readme.md
> ```

```text
cs374-regex/
  patterns.py      # Part 1
  mini_lexer.py    # Part 2
  transformer.py   # Part 3a-3b
  log_parser.py    # Part 3c
  config.json      # Part 3c configuration
  readme.md        # Part 4 answers
```

> **Time budget.** The four parts carry 25 points each and are sized alike.  The Regex Workshop lab (two to three hours, and due mid-assignment) completes your first patterns and the mini lexer skeleton, so Parts 1 and 2 go faster once the lab is in.  Spread the rest across the assignment window using the pacing table below, and get the first pattern passing today.

### Your First 30 Minutes

Get one pattern passing before you write any others.

> **Do this.**
> 1. Open `patterns.py` and paste the `check()` harness from Step 1a at the top of the file.
> 2. Below the harness, add pattern P1, `COURSE_CODE`, and its test call (the code below).
> 3. Save the file, then run it from inside `cs374-regex/` with the command below.
>
> ```python
> COURSE_CODE = r"[A-Z]{2,4}-?\d{3}"
>
> check("COURSE_CODE", COURSE_CODE,
>       should_match=["CS374", "MATH111", "BIO-101"],
>       should_not_match=["cs374", "CS3741"])
> ```
>
> ```bash
> python3 patterns.py
> ```

> **You should see.** One `PASS` line.  The numbers in parentheses count the test cases you supplied.

```text
PASS COURSE_CODE (3 positive, 2 negative)
```

Now break the pattern on purpose so you know what a failure looks like.

> **Do this.**
> 1. Remove the `-?` from `COURSE_CODE` and save.
> 2. Run `python3 patterns.py` again.
> 3. Put the `-?` back and confirm the `PASS` line returns.

> **You should see.** A `FAIL` line, followed by one indented line for each string the pattern got wrong.

```text
FAIL COURSE_CODE:
  SHOULD match but did NOT: 'BIO-101'
```

> **Why this matters.** That loop (edit, run, read the failure) is the whole workflow for Part 1, and it carries through the rest of the assignment.  `check()` never tells you a pattern is right in general; it tells you exactly which string it got wrong, and that string is your next clue.  Once the loop works for one pattern, the other nine repeat the same cycle.  Parts 2 and 3 replace the `PASS` line with a printed token list or an output file, but the loop is the same: change one thing, run, read what changed.

This assignment goes out alongside the Regular Expressions class session and the Regex Workshop lab.  The lab is due mid-assignment, and it completes your first patterns and the mini lexer skeleton for you.  Bring your lab files straight into Parts 1 and 2: the lab is a head start on this assignment, not separate work.

### Suggested Pacing

See the course schedule for the assigned and due dates.  A suggested sequence:

| Checkpoint | You should have |
|------------|----------------|
| On assignment | `check()` harness working (from the Regex Workshop lab); patterns P1-P3 passing |
| Checkpoint 1 | Part 1 complete: all ten patterns with test cases |
| Lab due | Part 2 complete: mini lexer (grown from the lab's skeleton) passing the ordering table |
| Checkpoint 2 | Part 3 complete: transformer and log parser producing the sample output |
| Due date | Part 4 analysis written; deliverables assembled and submitted |

---

## Part 1: Pattern Library (25 points)

Part 1 asks for ten tested patterns.  You test each one with the `check()` harness below, which reports every string that matched when it should not have, and every string that failed to match when it should have.

### Step 1a: Add the check() Harness

The harness is the only test tool you need for Part 1.  Add it once, and every pattern you write reuses it.

> **Do this.**
> 1. Open `patterns.py`.
> 2. Paste the harness below at the top of the file, before any patterns.  (If you already did this in Your First 30 Minutes, skip to Step 1b.)
> 3. Run `python3 patterns.py` once to confirm the file has no syntax errors.

```python
import re

def check(name: str, pattern: str, should_match: list, should_not_match: list):
    """Run pattern against positive and negative test cases. Report all failures."""
    compiled = re.compile(pattern)
    failures = []
    for s in should_match:
        if not compiled.fullmatch(s):
            failures.append(f"  SHOULD match but did NOT: {s!r}")
    for s in should_not_match:
        if compiled.fullmatch(s):
            failures.append(f"  Should NOT match but DID: {s!r}")
    if failures:
        print(f"FAIL {name}:")
        for f in failures: print(f)
    else:
        print(f"PASS {name} ({len(should_match)} positive, {len(should_not_match)} negative)")
```

> **You should see.** Nothing at all, and no error.  The file only defines a function so far; nothing calls it until you add a pattern and its `check()` call.

> **If it fails.**
> - `SyntaxError` or `IndentationError`: the paste lost its indentation.  Every line inside `check()` must be indented by four spaces, and the two `for` loop bodies by eight.
> - `python3: command not found`: use `python` instead, as noted in Environment and Setup.

`fullmatch` succeeds only when the pattern matches the entire string, from the first character to the last.  That is deliberate.  A pattern that matches only the first part of `CS3741` is too permissive, and `fullmatch` exposes it.

### Step 1b: Write the Ten Required Patterns

Write a pattern for each item below.  Define each one as a raw string with the name shown, and pass it to `check()`, which compiles it with `re.compile`.  Test each pattern with at least three positive and two negative cases.  The lists under each pattern give you starting cases.  The rubric also asks for a one-sentence explanation of each non-trivial construct in a pattern (a lookahead, a bounded repeat, an alternation), so write that sentence as a comment above the pattern.

> **Do this.** For each of P1 through P10, add this block to `patterns.py`, below the harness, and run `python3 patterns.py` after each one:
> 1. A comment with one sentence per non-trivial construct in the pattern.
> 2. The pattern itself, as a raw string, named exactly as shown in the list.
> 3. A `check()` call with at least three `should_match` and two `should_not_match` strings, starting from the lists below and adding your own.
>
> ```python
> # P2 IDENTIFIER: <one sentence per non-trivial construct goes here>
> IDENTIFIER = r"..."   # TODO
>
> check("IDENTIFIER", IDENTIFIER,
>       should_match=["foo", "_bar", "x1", "my_var_2"],
>       should_not_match=["1foo", "-x", "foo bar", '"x"'])
> ```

**P1 `COURSE_CODE`:** Ursinus course codes: two to four capital letters, an optional hyphen, then exactly three digits.
- Match: `CS374`, `MATH111`, `BIO-101`, `ENGL-201`
- No match: `cs374`, `CS3741`, `CS-37`, `374`

**P2 `IDENTIFIER`:** A legal programming identifier.  It starts with a letter or underscore, and any mix of letters, digits, and underscores may follow.  The pattern must match the full string.
- Match: `foo`, `_bar`, `x1`, `my_var_2`
- No match: `1foo`, `-x`, `foo bar`, `"x"`

**P3 `DECIMAL`:** A decimal number with an optional sign and an optional fractional part.  The integer part is required, so a bare `.` or a trailing dot such as `3.` is not valid.
- Match: `3`, `-3`, `+3.14`, `0.5`, `-0.001`
- No match: `.5`, `3.`, `--3`, `3..14`, `abc`

**P4 `TIME_12H`:** A 12-hour clock time.  The hour is 1-12.  Minutes are optional, but when present they must be two digits.  The meridiem (`AM` or `PM`) is required and follows a single space.
- Match: `8 AM`, `12:00 PM`, `1:30 AM`, `11:59 PM`
- No match: `13:00 AM`, `0:00 AM`, `8:5 PM`, `8AM`, `8:00`

**P5 `EMAIL`:** A practical email address (not RFC-compliant): one or more word characters or dots before `@`, then a domain of word characters and dots with at least one dot.
- Match: `user@example.com`, `bill.j@ursinus.edu`, `x@y.z`
- No match: `@example.com`, `user@`, `user@com`, `user @example.com`

**P6 `US_PHONE`:** A US phone number in the format `(NXX) NXX-XXXX`, where N is a digit from 2 to 9.
- Match: `(215) 555-1234`, `(800) 123-4567`
- No match: `215-555-1234`, `(015) 555-1234`, `(215)555-1234`

**P7 `ISO_DATE`:** An ISO 8601 date, `YYYY-MM-DD`.  Month is 01-12 and day is 01-31.  A regex cannot check how many days a particular month has, so validate only the format and these ranges.
- Match: `2026-09-18`, `2000-01-01`, `1999-12-31`
- No match: `26-09-18`, `2026-9-18`, `2026-13-01`, `2026-00-15`

**P8 `HEX_COLOR`:** A CSS hex color: a `#` followed by exactly 3 or 6 hexadecimal digits, in either upper or lower case.
- Match: `#fff`, `#FFF`, `#1a2b3c`, `#ABC`
- No match: `#gg1122`, `fff`, `#1234`, `#12345g`

**P9 `IPV4_ADDRESS`:** An IPv4 address: four groups of 1-3 digits separated by dots.  Validate the format and the 1-3 digit length of each octet.  Checking the 0-255 range is encouraged but not required.
- Match: `192.168.1.1`, `10.0.0.0`, `255.255.255.255`, `0.0.0.0`
- No match: `192.168.1`, `192.168.1.1.1`, `abc.def.ghi.jkl`

**P10 `MARKDOWN_LINK`:** A Markdown hyperlink `[text](url)`, where text is any run of non-`]` characters and url is any run of non-`)` characters.
- Match: `[Google](https://google.com)`, `[CS374](../index.html)`, `[x](y)`
- No match: `[Google]`, `(https://google.com)`, `Google(https://google.com)`

> **You should see.** After the tenth pattern, `python3 patterns.py` prints ten `PASS` lines and no `FAIL` lines.  The counts in parentheses are your own case counts, so yours will differ from these once you add cases.

```text
PASS COURSE_CODE (4 positive, 4 negative)
PASS IDENTIFIER (4 positive, 4 negative)
PASS DECIMAL (5 positive, 5 negative)
PASS TIME_12H (4 positive, 5 negative)
PASS EMAIL (3 positive, 4 negative)
PASS US_PHONE (3 positive, 3 negative)
PASS ISO_DATE (3 positive, 4 negative)
PASS HEX_COLOR (4 positive, 4 negative)
PASS IPV4_ADDRESS (4 positive, 3 negative)
PASS MARKDOWN_LINK (3 positive, 3 negative)
```

> **If it fails.**
> - `Should NOT match but DID`: the pattern is too permissive.  A character class is too broad, a quantifier allows too many repeats, or an optional piece lets a wrong string through.
> - `SHOULD match but did NOT`: the pattern is too strict.  The usual causes are a literal that needs escaping (`.`, `+`, `(`, `)`, `[`) or a piece that should be optional but has no `?`.
> - `re.error` before any `PASS` or `FAIL` line: the pattern itself does not compile.  Look for an unbalanced bracket or parenthesis; the message reports the position.

> **Watch out.**
> - P6 lists only two positive cases.  The rubric requires at least three, so add at least one of your own to every pattern that falls short.
> - I run hidden test cases too.  The rubric names two common misses: permitting leading zeros where the description forbids them, and leaving a pattern unanchored that should be anchored.  Add the negative cases you would use to catch those before I do.
> - `check()` uses `fullmatch`, so a pattern passes here with or without `^` and `$`.  Decide deliberately which approach each pattern takes.  Q2 in Part 4 asks you to state which anchor approach you used in each pattern and why, and Part 3 reuses P5 and P6 without anchors.

---

## Part 2: Mini Lexer Using re.finditer (25 points)

Part 2 builds a lexer, a program that splits source text into tokens, out of a single regex and `re.finditer`.  A token is a labeled piece of source text such as a keyword, a number, or an operator.

### The finditer Approach

A production lexer does not call `re.match` in a loop at each position.  Instead it joins every token pattern into one large alternation (a list of patterns separated by `|`) and calls `re.finditer`, which returns every non-overlapping match in a single pass.  Each alternative is a named group, `(?P<NAME>pattern)`, so each match reports which token rule fired through `m.lastgroup`.

```python
import re

TOKEN_SPEC = [
    ("WHITESPACE",  r"[ \t\n]+"),
    ("FLOAT",       r"\d+\.\d+"),
    ("INT",         r"\d+"),
    ("IF",          r"if(?!\w)"),   # negative lookahead prevents matching "iffy"
    ("IDENT",       r"[a-zA-Z_]\w*"),
    ("PLUS",        r"\+"),
    ("MINUS",       r"-"),
    ("EQ",          r"="),
    ("LPAREN",      r"\("),
    ("RPAREN",      r"\)"),
    ("SEMICOLON",   r";"),
]

# Build the master pattern: (?P<NAME>pattern)|(?P<NAME2>pattern2)|...
MASTER = re.compile(
    "|".join(f"(?P<{name}>{pat})" for name, pat in TOKEN_SPEC)
)
```

Order matters in `TOKEN_SPEC`.  At each position the engine tries the alternatives left to right and takes the first one that matches.  So `FLOAT` must come before `INT` (otherwise `3.14` lexes as `3`), and every keyword must come before `IDENT`.  This ordering is how the alternation achieves maximal munch, the rule that a lexer takes the longest token available at each position.  The `(?!\w)` after `if` is a negative lookahead: it succeeds only when the next character is not a word character, so `iffy` falls through to `IDENT`.

### Step 2a: Implement mini_lex()

`mini_lex()` walks the matches in order and checks that each match starts where the previous one ended.  Any gap means a character matched no rule, and the function raises `LexError` at that position.  `LexError` is not defined in the snippet below; you declare it as an `Exception` subclass in your file.

> **Do this.**
> 1. Open `mini_lexer.py`.  Paste the `TOKEN_SPEC` and `MASTER` code from The finditer Approach at the top.
> 2. Below it, declare `LexError` (the first snippet below).
> 3. Below that, paste `mini_lex()` (the second snippet).
> 4. At the bottom of the file, add the main block (the third snippet), which lexes one sample line and prints the result.
> 5. Run the file with the command below.

```python
class LexError(Exception):
    """Raised when a character matches no rule in TOKEN_SPEC."""
    pass
```

```python
def mini_lex(source: str) -> list:
    """Return a list of (token_type, value, start_pos) tuples, skipping whitespace.
    Raise LexError on any character that matches no rule (a gap in finditer coverage)."""
    tokens = []
    pos = 0
    for m in MASTER.finditer(source):
        if m.start() != pos:
            raise LexError(f"Unrecognized character {source[pos]!r} at position {pos}")
        kind = m.lastgroup
        if kind != "WHITESPACE":
            tokens.append((kind, m.group(), m.start()))
        pos = m.end()
    if pos != len(source):
        raise LexError(f"Unrecognized character {source[pos]!r} at position {pos}")
    return tokens
```

```python
if __name__ == "__main__":
    print(mini_lex("if x = 3.14;"))
```

```bash
python3 mini_lexer.py
```

> **You should see.** Five tuples, one per token.  Whitespace is consumed but not listed.  The third value in each tuple is the index in the source string where that token starts.

```text
[('IF', 'if', 0), ('IDENT', 'x', 3), ('EQ', '=', 5), ('FLOAT', '3.14', 7), ('SEMICOLON', ';', 11)]
```

> **If it fails.**
> - `NameError: name 'MASTER' is not defined`: the `TOKEN_SPEC` and `MASTER` block must sit above `mini_lex()` in the file.
> - `NameError: name 'LexError' is not defined`: the class declaration is missing or sits below the main block.
> - The output shows `('INT', '3', 7)` followed by a `LexError` at the dot: `FLOAT` is listed below `INT`.  Move it up.

### Step 2b: Extend the Token Spec

Extend `TOKEN_SPEC` to cover the language in the table below.  Use at least 15 token types, and include every keyword, operator, and literal listed.  Put the negative lookahead `(?!\w)` on every keyword so that `iffy` does not tokenize as `IF`.

| Category | Tokens |
|----------|--------|
| Keywords | `if`, `else`, `while`, `let`, `print`, `true`, `false`, `and`, `or`, `not`, `fun` |
| Literals | `INT` (`42`), `FLOAT` (`3.14`), `STRING` (`"hello"`), `IDENT` (`my_var`) |
| Two-char operators | `<=`, `>=`, `==`, `!=`, `->` |
| One-char operators | `=`, `<`, `>`, `+`, `-`, `*`, `/`, `!` |
| Punctuation | `(`, `)`, `{`, `}`, `;`, `:`, `,` |
| Skipped | whitespace, `# comment to end of line` |

> **Do this.**
> 1. Replace `TOKEN_SPEC` in `mini_lexer.py` with a longer list built on the skeleton below.  Keep the entries you already have and fill in each `# TODO`.
> 2. Name each keyword's token type in capitals (`LET`, `WHILE`, and so on); the ordering table in Step 2c expects `LET`.
> 3. "Skipped" means `mini_lex()` consumes the match but does not add a tuple, exactly as it does for `WHITESPACE`.  Extend the `if kind != "WHITESPACE"` test so it skips comments too.
> 4. Apply the rule that puts `FLOAT` before `INT` when you place each two-character operator relative to its one-character prefix.
> 5. Run `python3 mini_lexer.py` after each group of entries, not after all of them.
>
> ```python
> TOKEN_SPEC = [
>     ("WHITESPACE",  r"[ \t\n]+"),
>     ("COMMENT",     r"..."),            # TODO: a '#' and everything to the end of the line
>     ("FLOAT",       r"\d+\.\d+"),
>     ("INT",         r"\d+"),
>     ("STRING",      r"..."),            # TODO: double-quoted text
>     # TODO: one entry per keyword, each ending in (?!\w), all placed before IDENT
>     ("IF",          r"if(?!\w)"),
>     ("IDENT",       r"[a-zA-Z_]\w*"),
>     # TODO: two-character operators
>     # TODO: one-character operators
>     # TODO: punctuation
> ]
> ```

> **You should see.** The sample line from Step 2a still prints the same five tuples, since it uses no new token types.  Change the sample to `let x = 1;` and `let` now lexes as a keyword rather than an identifier.

```text
[('LET', 'let', 0), ('IDENT', 'x', 4), ('EQ', '=', 6), ('INT', '1', 8), ('SEMICOLON', ';', 9)]
```

> **If it fails.**
> - `re.error: redefinition of group name`: two entries in `TOKEN_SPEC` share a name.  Every name must be unique because each becomes a named group.
> - `let` still comes back as `IDENT`: the `LET` entry sits below `IDENT`, or its pattern lacks the `(?!\w)` lookahead and a different rule wins.
> - `<=` comes back as `LT` then `EQ`: the two-character entry sits below the one-character entry.

The Lexer assignment asks you to tokenize this same language with a reusable component, so the work you do here carries forward directly.  The table above has everything you need; you do not need that assignment sheet to finish this one.

### Step 2c: Verify Ordering and Maximal Munch

Run `mini_lex` on each input below and confirm that the output matches the expected token types.  If `iffy` comes back as `IF`, or `3.14` comes back as `INT`, fix the order of `TOKEN_SPEC`.

| Input | Expected |
|-------|----------|
| `if` | `[("IF", "if", 0)]` |
| `iffy` | `[("IDENT", "iffy", 0)]` |
| `3.14` | `[("FLOAT", "3.14", 0)]` |
| `3` | `[("INT", "3", 0)]` |
| `let x = 1;` | `LET IDENT EQ INT SEMICOLON` |
| `@` | `LexError at position 0` |

> **Do this.**
> 1. Replace the main block at the bottom of `mini_lexer.py` with the loop below.  It runs all six inputs and catches the `LexError` so the last input does not end the program.
> 2. Run `python3 mini_lexer.py` and compare each line to the table.
> 3. Keep this loop in the file; its output is part of `test_output.txt` in the Deliverables.
>
> ```python
> if __name__ == "__main__":
>     for src in ["if", "iffy", "3.14", "3", "let x = 1;", "@"]:
>         try:
>             print(f"{src!r:14} -> {mini_lex(src)}")
>         except LexError as e:
>             print(f"{src!r:14} -> LexError: {e}")
> ```

> **You should see.** Six lines, one per input, matching the table row for row.

```text
'if'           -> [('IF', 'if', 0)]
'iffy'         -> [('IDENT', 'iffy', 0)]
'3.14'         -> [('FLOAT', '3.14', 0)]
'3'            -> [('INT', '3', 0)]
'let x = 1;'   -> [('LET', 'let', 0), ('IDENT', 'x', 4), ('EQ', '=', 6), ('INT', '1', 8), ('SEMICOLON', ';', 9)]
'@'            -> LexError: Unrecognized character '@' at position 0
```

> **If it fails.**
> - `iffy` prints as `IF`: the keyword pattern is missing its `(?!\w)` lookahead.
> - `3.14` prints as `INT` then `LexError` at position 1: `FLOAT` is below `INT`.
> - `@` prints a token instead of `LexError`: one of your patterns is too broad and swallows characters it should not (an unescaped `.` is the usual cause).

---

## Part 3: Regex-Based Text Transformer and Log Parser (25 points)

Part 3 uses regexes to change text and to pull structured data out of a log file.  It has three steps: a text transformer, a greedy versus lazy demonstration, and a log parser.

### Step 3a: Text Transformer

In `transformer.py`, write a `transform(text: str) -> str` function that applies these three substitutions, in this order:

1.  Redact emails: replace every email address with `[EMAIL]` using `re.sub`.  Use P5 from Part 1 without anchoring, because the address sits inside a longer sentence.
2.  Normalize dates: convert `MM/DD/YYYY` dates to ISO `YYYY-MM-DD`.  Capture month, day, and year as groups, then reorder them with group references in the replacement string (e.g., `r"\3-\1-\2"`).
3.  Redact phone numbers: replace US phone numbers (P6 from Part 1) with `[PHONE]`.

> **Do this.**
> 1. Open `transformer.py` and paste the skeleton below.  The three-line input paragraph you must demonstrate on is already in `SAMPLE`.
> 2. Fill in the three patterns and the three `re.sub` calls at the `# TODO` markers.  Copy P5 and P6 from `patterns.py` and strip any anchors.
> 3. Run the file with the command below.

```python
import re

EMAIL = r"..."      # TODO: P5 from Part 1, without anchors
US_DATE = r"..."    # TODO: MM/DD/YYYY, with month, day, and year as three capture groups
US_PHONE = r"..."   # TODO: P6 from Part 1, without anchors

def transform(text: str) -> str:
    """Redact emails, normalize MM/DD/YYYY dates to ISO, then redact phone numbers."""
    # TODO: three re.sub calls, in the order listed above
    return text

SAMPLE = """Contact MONGAN, WILLIAM at billmongan@gmail.com or call (610) 555-0192.
The registration deadline was 09/01/2026.
A second contact: support@ursinus.edu, deadline 12/15/2026."""

if __name__ == "__main__":
    print(transform(SAMPLE))
```

```bash
python3 transformer.py
```

> **You should see.** These three lines.  Everything outside the redacted and converted pieces stays exactly as it was in `SAMPLE`.

```text
Contact MONGAN, WILLIAM at [EMAIL] or call [PHONE].
The registration deadline was 2026-09-01.
A second contact: [EMAIL], deadline 2026-12-15.
```

> **If it fails.**
> - Nothing is replaced: the pattern still carries `^` and `$` (or `\A` and `\Z`) from Part 1, so it can only match a whole string, never a piece of one.
> - The date prints as `01-09-2026` or `09-01-2026`: the group references in the replacement string are in the wrong order.  Count the capture groups left to right.
> - The phone number survives: the parentheses in the pattern are not escaped, so `(` opens a group instead of matching a literal `(`.

### Step 3b: Greedy vs. Lazy Demonstration

A greedy quantifier (`*`) matches as much text as it can.  A lazy quantifier (`*?`) matches as little as it can.  Show one input string and two patterns where the two produce different captures.

> **Do this.**
> 1. Add the code below to `transformer.py`, inside the main block after the `transform(SAMPLE)` call, so one run prints both demonstrations.
> 2. In a comment next to the two `re.search` lines, explain in one sentence why greedy captured more.
> 3. Run `python3 transformer.py` again.

```python
import re
text = '<b>bold</b> and <i>italic</i>'
greedy = re.search(r'<.*>',  text)   # greedy
lazy   = re.search(r'<.*?>', text)   # lazy
print(f"Greedy: {greedy.group()!r}")
print(f"Lazy:   {lazy.group()!r}")
```

> **You should see.** Two lines after the transformer output.  The greedy pattern runs to the last `>` in the string; the lazy one stops at the first.

```text
Greedy: '<b>bold</b> and <i>italic</i>'
Lazy:   '<b>'
```

You use this exact example again in Q1 of Part 4, so keep the input string and both patterns unchanged.

### Step 3c: Log Parser

In `log_parser.py`, write a `parse_log(log_path: str, config_path: str)` function for the provided server log.  Each line looks like `2026-09-18 08:10:22 WARN disk usage 91% on /dev/sda1`.  The function must:

1.  Use one `re.finditer` pattern with named groups to extract `date`, `time`, `level`, and `message` from each log line.
2.  Report counts by level (how many INFO, WARN, and ERROR lines).
3.  Report the earliest and latest timestamps, as strings in `YYYY-MM-DD HH:MM:SS` format.
4.  Extract every percentage value (`\d+%`) mentioned in WARN lines and report the maximum.
5.  Write all ERROR lines, each prefixed with its original line number, to `errors.txt`.

The named-group pattern must match this line format exactly:

```text
YYYY-MM-DD HH:MM:SS LEVEL message text here
```

Store both the input log path and the output `errors.txt` path in a JSON configuration file rather than in the code.  A JSON file holds data as nested names and values, and Python's `json.load` reads it into a dictionary.

> **Do this.**
> 1. Open `config.json` and paste the two-key object below.
> 2. Save the provided server log in `cs374-regex/` under the name `config.json` points to, `server.log`.
> 3. Open `log_parser.py` and paste the skeleton below.  Fill in the pattern and the `# TODO` markers.
> 4. Run the file with the command below.

```json
{
  "log_path": "server.log",
  "errors_path": "errors.txt"
}
```

```python
import json
import re

LINE = re.compile(r"...")   # TODO: named groups date, time, level, message

def parse_log(log_path: str, config_path: str) -> None:
    """Parse the log at log_path.  Read the errors.txt path from the JSON at config_path."""
    with open(config_path) as f:
        config = json.load(f)
    # TODO: read the log, run LINE.finditer over it, and collect from the named groups:
    #   counts by level, the earliest and latest timestamps, the maximum WARN percentage
    # TODO: write every ERROR line, prefixed with its line number, to config["errors_path"]
    # TODO: print the five report lines shown below

if __name__ == "__main__":
    with open("config.json") as f:
        cfg = json.load(f)
    parse_log(cfg["log_path"], "config.json")
```

```bash
python3 log_parser.py
```

> **You should see.** Five report lines in this shape, and a new `errors.txt` in `cs374-regex/`.  The numbers come from the provided log, so match the shape, not these exact values.  Open `errors.txt` and confirm each line begins with its line number from the original log.

```text
Counts: INFO=42, WARN=8, ERROR=3
Earliest: 2026-09-01 00:01:14
Latest:   2026-09-18 23:59:59
Max WARN percentage: 91%
ERROR lines written to errors.txt
```

> **If it fails.**
> - `FileNotFoundError: server.log`: the log is not in `cs374-regex/`, or you ran the command from a different folder.
> - Every count is zero: the pattern matches nothing.  If you anchored it with `^` and `$` and run `finditer` over the whole file, add the `re.MULTILINE` flag so the anchors match at each line, not only at the ends of the file.
> - `KeyError: 'date'`: a named group is misspelled, or the pattern uses a plain group `(...)` where a named group `(?P<date>...)` is required.

> **Watch out.** The rubric's top row asks for more than the five items above: malformed lines (any line that does not fit the format) must be detected and reported with their line number rather than silently dropped, the configuration must live in `config.json`, and `errors.txt` must be generated by the program, not written by hand.  `enumerate(lines, start=1)` is the simplest way to keep a line number next to each line.

---

## Part 4: Pattern Analysis (25 points)

Answer the four questions below in `readme.md`.  Each answer must be at least one paragraph and must include a concrete example from your own work in this assignment.

> **Do this.**
> 1. Open `readme.md` and add four headings, `Q1` through `Q4`.
> 2. Under each, write at least one paragraph that quotes a pattern, an input, or an output from your own files.  Restating the course notes without your own example earns the lowest rubric row.
> 3. End the file with the Python version you used (`python3 --version`), so that I can reproduce your results.

### Q1: Greedy vs. Lazy

Explain the difference between greedy (`*`, `+`) and lazy (`*?`, `+?`) quantifiers, using the specific example from Step 3b.  Then state when you would prefer lazy over greedy in production code.

### Q2: Anchors

An anchor is a pattern element that matches a position rather than a character.  Explain the difference between `^`, `$`, `\A`, and `\Z`.  Show a pattern from your Part 1 library where removing the anchors (or switching from `fullmatch` to `search`) would cause a false positive.  State which anchor approach you used in each Part 1 pattern and why.

### Q3: Named Groups

Explain the difference between plain groups `(...)`, non-capturing groups `(?:...)`, and named groups `(?P<name>...)`.  Show how `groupdict()` differs from `groups()` using your log parser pattern from Step 3c.

### Q4: The Limits of Regular Expressions

In one paragraph, explain why no regular expression can validate balanced nested parentheses in general.  Your explanation must:
- Reference the pumping lemma for regular languages (by name; you do not need to reproduce the full proof) (taught in the Regular Expressions class session with a worked example; see Allison Ch. 4).
- Name the level of the Chomsky hierarchy that handles context-free languages.
- Name the component of your language pipeline (from the Lexer, Parser, and Interpreter assignments) whose job it is to handle balanced nesting.

---

## Deliverables

> **Do this.**
> 1. From inside `cs374-regex/`, capture the output of all four modules into `test_output.txt` with the commands below.  The first `>` creates the file; each `>>` appends to it.
> 2. Confirm `errors.txt` is present from your last `log_parser.py` run.
> 3. Zip the `cs374-regex/` folder (right-click and compress, or `zip -r cs374-regex.zip cs374-regex` from the parent folder) and submit the ZIP.
>
> ```bash
> python3 patterns.py > test_output.txt
> python3 mini_lexer.py >> test_output.txt
> python3 transformer.py >> test_output.txt
> python3 log_parser.py >> test_output.txt
> ```

The ZIP must contain:

| File or artifact | What it shows | Rubric row |
|------------------|---------------|------------|
| `patterns.py` | All ten patterns with the `check()` harness and test calls | Pattern Library |
| `mini_lexer.py` | The mini lexer with the extended `TOKEN_SPEC` and the Step 2c loop | Mini Lexer |
| `transformer.py` | The text transformer and the greedy vs. lazy demonstration | Text Transformer and Log Parser |
| `log_parser.py` | The log parser | Text Transformer and Log Parser |
| `config.json` | The log parser configuration | Text Transformer and Log Parser |
| `errors.txt` | The generated errors file from the provided log | Text Transformer and Log Parser |
| `test_output.txt` | Output of running all four modules | All rows |
| `readme.md` | Approximately one page: the four analysis answers, the limits paragraph, and your Python version | Pattern Analysis |

List your Python version in `readme.md` so that your results can be reproduced.

---

## Self-Check Before You Submit

- [ ] `python3 patterns.py` prints ten `PASS` lines and no `FAIL` lines, and every pattern has at least three positive and two negative cases.
- [ ] Every pattern is a raw string, uses the name shown, and carries a one-sentence comment for each non-trivial construct.
- [ ] `python3 mini_lexer.py` prints the six Step 2c lines exactly as tabled, and `TOKEN_SPEC` has at least 15 types with `(?!\w)` on every keyword.
- [ ] `mini_lex()` raises `LexError` with the position for any unrecognized character, and skips comments as well as whitespace.
- [ ] `python3 transformer.py` prints the three transformed lines and the two greedy/lazy lines, with the one-sentence comment in place.
- [ ] `python3 log_parser.py` reads its paths from `config.json`, reports malformed lines with their line numbers, and writes `errors.txt`.
- [ ] `readme.md` answers Q1 through Q4 with examples from your own files, names the Chomsky level and the pipeline component in Q4, and lists your Python version.
- [ ] `test_output.txt` is freshly generated from the files you are submitting.

---

## Grading Breakdown

| Component | Points |
|-----------|--------|
| Part 1: Pattern Library | 25 |
| Part 2: Mini Lexer with re.finditer | 25 |
| Part 3: Text Transformer and Log Parser | 25 |
| Part 4: Pattern Analysis | 25 |
| **Total** | **100** |

---

## Reflection Prompts

- Which pattern took the most revisions, and what misconception did the failures expose?
- Where did you choose a simpler pattern over a perfectly precise one, and how did you document the tradeoff?
- After completing Part 2, what are the limits of a regex-only lexer?  Name one thing this `finditer` loop cannot do that a hand-written scanner with `peek`/`advance` can.  You'll build exactly that in the Lexer assignment.
- If collaboration with a buddy was permitted, did you work with a buddy on this assignment?  If so, who?  If not, do you certify that this submission represents your own original work?  Please identify any and all portions of your submission that were not originally written by you.
- AI disclosure: list any generative-AI tools you used, for what, and how you verified the results (or state 'none').
- Approximately how many hours it took you to finish this assignment (I will not judge you for this at all; I am simply using it to gauge if the assignments are too easy or hard)?
