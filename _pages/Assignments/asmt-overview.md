---
layout: assignment
permalink: /Assignments/Overview
title: "CS374: Principles of Programming Languages - Overview"

info:
  coursenum: CS374
  purpose: "To confirm your Python toolchain, judge two languages you already use against the course's evaluation criteria, and capture a baseline of your relationship with languages before the build begins."
  tilt:
    task: "Argue readability and writability tradeoffs in two languages you already know and translate a snippet across paradigms, verify your environment with the starter script, and write a short Language Autobiography."
    criteria: "I assess your work on a defended pair of language judgments and an honest paradigm translation, a verified environment, and a specific, reflective autobiography.  The rubric below has the details."
  points: 100
  goals:
    - To turn the reading's evaluation criteria into judgments you can defend about languages you already use
    - To classify a snippet's paradigm and name what it costs to translate it into another
    - To verify a working Python development environment for the semester's build
    - To demonstrate baseline command-line, git, and Python-environment fluency by navigating a shell, authenticating to GitHub with an SSH key, cloning and committing to a repository, and creating a reproducible environment with uv
    - To reflect on your language background as a baseline for the course
    - To run the provided starter script that exercises the libraries used throughout the semester
  rubric:
    - weight: 10
      description: "Part 0: Evaluating Languages and Paradigms"
      preemerging: Neither the language comparison nor the paradigm translation is attempted
      beginning: Two languages are named and a snippet is classified, but the claims are asserted without a design choice pointed to in either language
      progressing: Each language is tied to a specific design choice and the snippet is translated, but the write-up does not say what the translation cost, or does not commit to which criterion you value more
      proficient: Each of the two languages is tied to a named design choice that makes it more readable or more writable; the paradigm of the snippet is classified and it is translated (or the write-up argues concretely why it cannot be); the translation cost is named; and you say which criterion you would give up and why
    - weight: 36
      description: Environment Setup and Verification
      preemerging: Little or no evidence that the environment was attempted
      beginning: Some components verified, but the transcript is missing or incomplete, or only one or two of the three verification steps are completed
      progressing: Python environment verified with a complete transcript including version information; the starter script ran but with a minor failure (missing library, wrong Python version) documented with a hypothesis and fix attempt, or the command-line and git checkpoint is incomplete
      proficient: Python 3.10 or later verified; the starter script produces the expected banner; editor/IDE identified; all three verification steps produce transcript evidence; the command-line and git checkpoint (Part 1.5) is complete, showing shell navigation and search, an SSH key registered with GitHub and verified with `ssh -T`, a git commit pushed to a remote over SSH, and a uv environment; any failure is documented with error text, hypothesis, and resolution
    - weight: 36
      description: Language Autobiography
      preemerging: The autobiography is missing or does not address any of the four prompts
      beginning: The autobiography addresses some prompts superficially, without specific examples
      progressing: All four prompts are addressed with specific examples drawn from the student's own experience, with limited connection to course themes (parsing, semantics, scoping)
      proficient: All four prompts are addressed with specific examples; the "language fought you" entry uses precise vocabulary (syntax, semantics, type, scope, evaluation order); the reflection question is stated as an open question, not a question whose answer the student already knows
    - weight: 18
      description: Submission
      preemerging: No submission, or the submission is missing major components
      beginning: The submission is present but disorganized, transcript and autobiography are hard to tell apart, or one is missing
      progressing: All required components are present in one file, with a minor omission such as an unlabeled transcript section
      proficient: A single, well-organized PDF (or Markdown) containing a complete labeled transcript for every verification step and all four autobiography prompts, with the collaboration, AI-disclosure, and time questions answered
  readings:
    - rtitle: "Welcome Activity"
      rlink: "https://www.billmongan.com/Ursinus-CS374-Overview"
    - rtitle: "Thain, Chapter 1"
    - rtitle: "uv: the Python environment manager we standardize on (Part 1.5)"
      rlink: "https://docs.astral.sh/uv/"
    - rtitle: "Setup (Route A): The Course Development Environment - Docker, Git, and GitHub (Tutorial)"
      rlink: "../Tutorials/DevEnvironment"
    - rtitle: "Setup (Part 1.5): Shell Skills for Language Development, the step-by-step tutorial article this assignment's shell work follows"
      rlink: "../Tutorials/ShellForLanguageDev"
    - rtitle: "GitHub: Connecting to GitHub with SSH (generate a key, add it to your account, and test it)"
      rlink: "https://docs.github.com/en/authentication/connecting-to-github-with-ssh"

tags:
  - intro
  - languages

---

The purpose of this warmup is to confirm your tools before the build begins, and to capture your current relationship with programming languages as a baseline you'll come back to at the end of the semester.  (Your team charter is **not** part of this assignment.  You'll draft it with the [Team Language Project]({{ site.baseurl }}/Projects/TeamLanguage) Design-Phase Submission and sign it with the Proposal.)

The Warmup is the Teams-based onboarding survey, and the Overview is the technical setup plus the Language Autobiography.  They are separate deliverables.

One pointer before you begin.  Several assignments this semester offer **directions**, which are equivalent ways of meeting the same deliverable, and some of those directions build toward live-coded music.  If a language that makes music appeals to you, please skim the [Music and Live-Coding guide]({{ site.baseurl }}/Projects/TeamLanguage#the-music-and-live-coding-path) this week.  You choose directions later, inside each assignment, so nothing is committed now.

---

## Part 0: Before You Start — Evaluating Languages and Paradigms (10 points)

Do this one **first**, before the rest of the assignment.  It takes about fifteen minutes and a pencil, and it is the only part of this assignment that has nothing to do with your toolchain.

Readability and writability are easy words to nod at and hard to use well.  They only get sharp when you point them at code you have actually written, in languages you have actually argued about.

**1. Two languages you already know.**  Pick two.  Write **one sentence each** naming a specific *design choice* that makes one of them more **readable** and the other more **writable**.  A design choice is something concrete — significant whitespace, mandatory type annotations, operator overloading, list comprehensions, semicolons, `null` — not a mood.  Then say which of the two criteria you would give up if you had to, and why.

**2. A snippet across paradigms.**  Take about five lines of code in any language and classify the paradigm it primarily represents (imperative, object-oriented, functional, declarative).  Then rewrite it in a *different* paradigm, and name what the translation cost you: lines, clarity, performance, or something you could no longer express at all.

If you cannot finish the translation, that is a real answer and it earns full credit — as long as you say precisely where it broke and why. An argument you could not finish is more useful to me than a clean page.

**What to bring to class:** the sticking point. The translation that stalled, or the design choice you could not call good or bad. That is what we start from.

Put both parts in your submission under a heading `Part 0`.

---

## Part 1: Environment Verification

This course builds a language implementation in Python, incrementally, across six assignments.  The final pipeline connects a lexer, parser, AST, environments, and an evaluator; every stage uses `re` (regular expressions), `json` (configuration files), and Python's structural pattern matching (`match`/`case`, available in Python 3.10+).  Verify that all three work before the build begins.

Complete this part by **one of two routes**; the transcript requirement at the end applies to whichever you choose.

### Route A (recommended): the course dev container

Set up the course Docker container by following the [Development Environment tutorial]({{ site.baseurl }}/Tutorials/DevEnvironment): one container image with the entire semester's toolchain preinstalled (Python 3.11, pytest, hypothesis, PLY, `uv`, a Scheme for the functional programming assignment, and flex/bison/gcc/make for the generator-toolchain directions), bind-mounted onto a `cs374-work` GitHub repository you create in the tutorial.  Then:

1.  Copy `warmup_check.py` (from Step 2 of Route B below) into your `cs374-work` repository.
2.  Enter the container and run it **inside the container**: `python3 warmup_check.py`.  Include the full transcript (the container prompt, `python3 --version`, and the script's banner output) in your submission.
3.  Complete Step 3 of Route B (editor/IDE) as written; VS Code with the Dev Containers extension, opened inside the course container, is the recommended answer and satisfies all three bullets.

Route A students skip Steps 1-2 of Route B on the host: the tutorial's toolchain verification plus the in-container `warmup_check.py` transcript covers them.

### Route B: native install

**Step 1: Confirm Python 3.10 or later.**

```bash
python3 --version
```

If the version is earlier than 3.10, install a newer version or use a virtual environment.  On macOS, `brew install python@3.12`; on Windows, download from python.org; on Linux, `sudo apt install python3.12` (Debian/Ubuntu) or equivalent.

**Step 2: Run the starter script.**

Download `warmup_check.py` from the course site (or copy it from below) and run it.  It exercises `re`, `json`, and `match`/`case`, and prints a confirmation banner if all three pass.  Note: on Windows consoles that garble the yes/no characters, run with `PYTHONIOENCODING=utf-8` or read the True/False values instead.

```python
# warmup_check.py: CS374 environment verification script
# Run with: python3 warmup_check.py

import sys, re, json

EXPECTED_PYTHON = (3, 10)

def check_python_version():
    v = sys.version_info
    ok = (v.major, v.minor) >= EXPECTED_PYTHON
    print(f"[{'OK' if ok else 'FAIL'}] Python {v.major}.{v.minor}.{v.micro}  "
          f"(need >= {EXPECTED_PYTHON[0]}.{EXPECTED_PYTHON[1]})")
    return ok

def check_re():
    # Test: tokenize a tiny expression
    pattern = re.compile(r"(?P<NUM>\d+)|(?P<PLUS>\+)|(?P<WS>\s+)")
    tokens = [(m.lastgroup, m.group()) for m in pattern.finditer("1 + 2")
              if m.lastgroup != "WS"]
    ok = tokens == [("NUM", "1"), ("PLUS", "+"), ("NUM", "2")]
    print(f"[{'OK' if ok else 'FAIL'}] re module: tokenized '1 + 2' -> {tokens}")
    return ok

def check_json():
    data = json.loads('{"language": "Mini", "version": 1, "strict": true}')
    ok = data["language"] == "Mini" and data["version"] == 1
    print(f"[{'OK' if ok else 'FAIL'}] json module: parsed {data}")
    return ok

def check_match_case():
    # Requires Python 3.10+
    def classify(x):
        match x:
            case int(n) if n < 0:  return "negative int"
            case int(n):           return "non-negative int"
            case str(s):           return f"string '{s}'"
            case _:                return "other"
    tests = [(-1, "negative int"), (5, "non-negative int"), ("hi", "string 'hi'")]
    ok = all(classify(v) == expected for v, expected in tests)
    print(f"[{'OK' if ok else 'FAIL'}] match/case: all {len(tests)} structural tests passed")
    return ok

def check_dataclasses():
    from dataclasses import dataclass
    @dataclass
    class Token:
        type: str
        value: str
        line: int = 1
    t = Token("NUM", "42")
    ok = t.type == "NUM" and t.line == 1
    print(f"[{'OK' if ok else 'FAIL'}] dataclasses: Token{t} constructed correctly")
    return ok

results = [
    check_python_version(),
    check_re(),
    check_json(),
    check_match_case(),
    check_dataclasses(),
]

print()
if all(results):
    print("=" * 50)
    print("  CS374 environment verified. OK")
    print("  You are ready to build a language.")
    print("=" * 50)
else:
    failed = sum(1 for r in results if not r)
    print(f"  {failed} check(s) failed. See above for details.")
    print("  Document each failure verbatim and bring it to class.")
```

**Save it and run it.**  Python runs files, so the snippet above has to land in one.  Open your `~/cs374` folder in VS Code (**File > Open Folder**), create a file with **File > New File**, paste the script, and save it as `warmup_check.py` in that folder; from the terminal alone, `nano warmup_check.py` (paste, Ctrl+O to write, Ctrl+X to exit) does the same thing.  Then run it from the directory the file lives in:

```bash
cd ~/cs374
python3 warmup_check.py
```

On Windows in PowerShell the command is `python warmup_check.py`, since Windows Python installs as `python`.  VS Code's Run button (the triangle in the top right, with the Python extension installed) runs the same command in its integrated terminal, and either transcript is fine for your submission.  If the shell answers `can't open file ... No such file or directory`, you are running from a different directory than the one you saved into; `ls` (or `dir`) will show you which.

**Step 3: Identify your editor or IDE.**

State which editor or IDE you will use for the semester and confirm that you can:
- Open, edit, and save a Python file.
- Run a Python file from within the editor (or from its integrated terminal).
- Set a breakpoint and inspect a variable in the debugger.

Recommended editors: VS Code (with Python extension), PyCharm Community Edition, or any editor you already know.  Avoid IDEs that hide the command line entirely; you will need `python3`, `git`, and occasionally `pip` directly.

**Capture a transcript** (copy-paste or screenshot) of all three steps: for Route A, that means the in-container `warmup_check.py` run with `python3 --version`, plus the editor step.  If any step fails, document the error text verbatim, your hypothesis about the cause, and what you tried to fix it.  A well-documented failure with a follow-up plan earns full credit for that step.

---

## Part 1.5: Command-Line and Git Checkpoint

You will build one language across six assignments, each importing the previous stage's component *unchanged*, all from the terminal and all under version control.  This checkpoint confirms those underlying tools work before the pipeline depends on them.  You don't need to be a shell expert.  You need to navigate, version your work, and create a reproducible environment.  The two required-setup tutorials teach all of it, so I have not repeated any of it here.  Work through the [Course Development Environment]({{ site.baseurl }}/Tutorials/DevEnvironment) for the container, git identity, and the daily loop, and [Shell Skills for Language Development]({{ site.baseurl }}/Tutorials/ShellForLanguageDev), a step-by-step article with a *Try it* checkpoint per step, for navigation, `grep`, redirection, and the test harness.  The **Command-Line Survival** links below fill any remaining gaps.

**Container-route note (Route A):** perform the git steps of this checkpoint **from inside the course container**, against the `cs374-work` GitHub repository you created in the [Development Environment tutorial]({{ site.baseurl }}/Tutorials/DevEnvironment); the tutorial's practice section (create `hello.py`, run, commit, push) is exactly this checkpoint, so its transcript satisfies the shell-navigation and git items below.  The `uv` step still runs on your host (the container image already pins the course packages; `uv` is your reproducible-environment tool for the native route and anywhere outside the container).

Complete each step and capture the terminal output:

1.  **Navigate and search.**  Create a course directory, enter it, and list it: `mkdir -p ~/cs374 && cd ~/cs374 && pwd && ls -la`.  That directory is empty at this point, so make a file for the search to find before you search.  Redirecting a couple of lines into a file is the quickest way, though typing them into an editor (`nano sample.txt`, or a new file saved from VS Code) or copying in a `.py` file you already have works just as well:

    ```bash
    printf 'let x = 1;\nlet y = x + 2;\nprint y;\n' > sample.txt
    cat sample.txt
    ```

    Note that `touch sample.txt` creates the file but leaves it empty, and a search over an empty file matches nothing, so put a line or two inside it.  (In native PowerShell, the equivalent is `Set-Content sample.txt "let x = 1;"`, since `printf` and `grep` are Unix shell tools; `Select-String` is the PowerShell search command.  Running these from WSL2 or Git Bash keeps the commands as written.)

    Now run one search with `grep -n` (or `rg`), and paste the command and its output:

    ```bash
    grep -n "let" sample.txt
    ```

    (`~` means your home folder; it works in macOS Terminal, Linux shells, WSL2, Git Bash, and PowerShell, but *not* in the Windows Command Prompt, where the equivalent is `%USERPROFILE%`.  Run these from PowerShell or WSL2 on Windows.)  Searching text is the daily reality of lexer and parser work, the same regular expressions you will use in the Regex assignment.  ([regex101](https://regex101.com/) is your friend there.)

2.  **Authenticate to GitHub with an SSH key.**  You will push to GitHub all semester, and GitHub has not accepted account passwords over HTTPS for years, so settle authentication now rather than discovering it at your first `git push`.  Use a key you already have, or create one.

    Check first, because you may already have one: run `ls -al ~/.ssh` and look for a pair such as `id_ed25519` and `id_ed25519.pub`.  If a pair is there and you know it is registered with GitHub, jump to the test below.

    **Create a key.**  Ed25519 is the current default; use `ssh-keygen -t rsa -b 4096` instead only on a system too old to support it.

    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```

    Accept the default path (`~/.ssh/id_ed25519`).  A passphrase is optional and worth setting; if you set one, load the key into the agent so you are not retyping it every push: `eval "$(ssh-agent -s)"`, then `ssh-add ~/.ssh/id_ed25519`.

    **Add the public key to GitHub.**  Print it with `cat ~/.ssh/id_ed25519.pub` and copy the entire line, then on GitHub open **Settings -> SSH and GPG keys -> New SSH key**, title it so you can tell which machine it belongs to, and paste.  Paste the `.pub` file and nothing else: the file *without* `.pub` is your private key, and it never leaves your machine, never goes in a repository, and never gets pasted into a web form.

    **Test it, and paste this output into your submission:**

    ```bash
    ssh -T git@github.com
    ```

    The first connection asks you to confirm GitHub's host fingerprint; answering `yes` is expected.  Success looks like `Hi YOURUSERNAME! You've successfully authenticated, but GitHub does not provide shell access.`  That is the success message, not an error: GitHub is telling you the key works and that SSH to GitHub is only ever used for git, never for a login shell.

    From here on, use the SSH remote form, `git@github.com:YOURUSERNAME/REPO.git`, rather than the `https://` URL.  If you already cloned over HTTPS, switch the existing remote rather than re-cloning:

    ```bash
    git remote set-url origin git@github.com:YOURUSERNAME/REPO.git
    ```

    **A shortcut, and the one I would take on native Windows.**  The [GitHub CLI](https://cli.github.com/), the `gh` command, does this entire exchange for you.  Install it (`winget install --id GitHub.cli` in PowerShell, `brew install gh` on macOS, or your package manager on Linux), then run `gh auth login`, choose **GitHub.com**, choose **SSH** as the protocol, and answer yes when it offers to generate a new SSH key and upload it to your account.  That one prompt replaces `ssh-keygen`, the `cat` of the `.pub` file, and the paste into Settings.  Verify it exactly as above, with `ssh -T git@github.com`, and paste that output; `gh` also clones for you, with `gh repo clone YOURUSERNAME/REPO` in place of the `git clone` in step 3.

    This matters most on **native Windows without WSL2**, where you would otherwise have to assemble the SSH tooling yourself.  Two separate downloads help there, and they are worth telling apart.  [GitHub Desktop](https://desktop.github.com/) is the graphical client; it bundles Git for Windows, which is where `ssh-keygen` and Git Bash come from, and it handles its own authentication so you can clone, commit, and push without touching a key at all.  `gh` is the command-line tool just described, and it is a separate install rather than something GitHub Desktop brings along, though installing both is common and they coexist happily.  Either one spares you the manual key dance; the Ubuntu or WSL2 route gives you the standard Unix tooling instead, and every command on this page then works as written.

    (Route A students: this key lives on your **host** machine, which is where you just made it.  Whether to expose it to the container or use a repository-scoped token inside the container instead is a separate decision, and Step 5 of the [Development Environment tutorial]({{ site.baseurl }}/Tutorials/DevEnvironment) walks through both.  Either way, create and register the key here.)

3.  **Version control.**  Get a repository on your machine, commit a file to it, and push that commit back to GitHub.  Which command starts you off depends on where the repository already exists, and this is the distinction worth learning once rather than guessing at every semester: **clone** when the repository is already on GitHub, and `git init` only when it is not.

    **If the repository already exists on GitHub** (your GitHub Classroom repository, or the `cs374-work` repository you created in the [Development Environment tutorial]({{ site.baseurl }}/Tutorials/DevEnvironment)), clone it.  Cloning downloads the full repository, sets `origin` to the URL you cloned from, and leaves you in a working copy that is already connected, so there is no `git remote add` afterward.  Copy the address from the green **Code** button on the repository page, choosing the **SSH** tab so you get the `git@github.com:` form the key you just tested authenticates:

    ```bash
    cd ~/cs374
    git clone git@github.com:YOURUSERNAME/REPO.git
    cd REPO
    git remote -v
    ```

    `git clone` creates a *new folder* named after the repository, inside whatever directory you run it from, which is why you `cd` into it on the next line.  `git remote -v` should print your SSH URL twice, once for fetch and once for push; that is your evidence the working copy is wired to GitHub.  A repository with no commits yet clones with a warning that it is empty, and that is fine, since the commit below is about to fill it.

    **Prefer to do this in VS Code?**  You can, and it drives the same git underneath, so the result is identical.  With no folder open, the Source Control view (Ctrl+Shift+G, or Cmd+Shift+G on macOS) offers a **Clone Repository** button; from anywhere, the Command Palette (Ctrl+Shift+P, or Cmd+Shift+P) runs **Git: Clone**.  Either one asks for the repository address, where you paste the same SSH URL, then asks which local folder to put it in, `~/cs374` here, and offers to open the clone when it finishes.  Say yes: the integrated terminal (Ctrl+`) then opens already inside the repository, which is where you run `git log --oneline` for your transcript.  The palette also offers **Clone from GitHub**, which lets you pick from a list of your repositories instead of pasting a URL, though it signs you in to GitHub inside VS Code and authenticates as that account rather than with your key.  This is the same editor you identified in Part 1, Step 3, so if you set a breakpoint there you already have it installed.

    **If you are starting from a folder on your machine instead**, with no repository on GitHub yet, create the repository on GitHub first (**+ > New repository**, no README, which keeps the histories from conflicting), then `git init` locally and attach that remote by hand:

    ```bash
    git init
    git remote add origin git@github.com:YOURUSERNAME/REPO.git
    ```

    **Either way, the commit is the same.**  Git versions files, so the repository needs at least one file in it before there is anything to commit; create that file the way you created `sample.txt` above, with a redirect, an editor, or a copy of something you already have:

    ```bash
    printf '# CS374 scratch repository\n' > README.md
    git add README.md
    git commit -m "first commit"
    git push -u origin main
    ```

    Use the SSH remote you tested in step 2; the push should not prompt you for a username or password.  Three things commonly go sideways here: `git commit` without `-m` drops you into an editor, and `:q!` leaves it if that editor turns out to be `vim`; `git push` complains if your default branch is not named `main`, which `git branch -M main` fixes; and a `git clone` that asks for a password means you copied the HTTPS address rather than the SSH one, so `git remote set-url origin git@github.com:YOURUSERNAME/REPO.git` puts it right without re-cloning.  Paste `git log --oneline`.  Your team will live in git during the capstone, so start now.
4.  **Reproducible Python with uv.**  Install [uv](https://docs.astral.sh/uv/), the fast modern Python environment manager we standardize on this term, and create a project environment: `uv venv`, then `uv run python --version`, then `uv add pytest` (you will write test suites all semester).  Paste the output.  There is no course project here yet, so `uv add` may stop on a missing `pyproject.toml` (and a bare `pytest` would say `no tests ran`); that is fine for this checkpoint, and `uv init` before `uv add` clears it if you want the install to complete.  What I am checking is that the tools are installed and on your PATH, so the output that fails this step is `uv: command not found` or `pytest: command not found`, not a complaint about a missing project.  (If you cannot install uv, fall back to `python -m venv` + `pip`, and note the fallback in your submission.)

### Command-Line Survival: reference (use as needed)

- [tldr pages](https://tldr.sh/): example-first cheat sheets (`tldr grep`).
- [explainshell](https://explainshell.com/): annotates any command line flag by flag.
- [ShellCheck](https://www.shellcheck.net/): lints shell scripts (you will use it in the project's scripting-targets extension).
- [regex101](https://regex101.com/): interactive regex tester, directly useful for the Regex and Lexer assignments.

### Part 1.5 Checklist

- [ ] A shell transcript showing directory creation, navigation, and a `grep`/`rg` search
- [ ] The output of `ssh -T git@github.com`, showing your GitHub username
- [ ] A `git log --oneline` transcript showing at least one commit pushed to a remote over SSH
- [ ] A `uv` (or documented fallback) transcript creating an environment and adding `pytest`

---

## Part 2: Language Autobiography

The purpose of this section is to capture your relationship with programming languages at the start of the course, as a baseline you will revisit in your final report.  Write approximately one page (400-600 words), addressing all four prompts below.

**Prompt 1: Your language history.**
List every programming language and formal notation you have used, and please count regex, SQL, spreadsheets, HTML, configuration languages, and shell scripts.  For each one, write a sentence on what it was good at from your perspective as a user.  Don't worry about precision here; I want your candid impressions more than textbook accuracy.

*Example opening:* "Python (four years): excellent for data exploration because the REPL makes it easy to try ideas without a compile step.  SQL (one semester): surprisingly good at expressing 'find all rows where' queries, but I found joins hard to visualize..."

**Prompt 2: A moment the language fought you.**
Describe one specific moment when a language was harder to use than you expected, meaning something you wanted to express that the language made difficult, surprising, or impossible.  Please be concrete, and name the language, the construct you were trying to write, and what the language made you do instead.

*What to aim for:* an answer that uses at least one of these words precisely: syntax, semantics, type, scope, evaluation order, binding.  You do not need to know all these words yet; use the ones you know and leave placeholders for the ones you don't.

**Prompt 3: A moment of elegance.**
Describe one feature of any language (or of a language feature you read about) that felt elegant the first time you understood it.  "Elegant" can mean surprisingly concise, surprisingly general, or surprisingly consistent.

**Prompt 4: An open question.**
Pose one question about how programming languages work that you hope this course will answer.  The best questions are the ones you don't know the answer to, and not the ones you could look up in Wikipedia.

*Examples of good questions:* "Why does Python have both `is` and `==`, and what is actually different between them at the implementation level?"  "How does a compiler know which variables a closure needs to capture?"  "Is there a way to guarantee that a recursion terminates without running it?"

---

## Deliverables

Submit a **single PDF** (preferred) or Markdown file containing:
1.  Part 0: the two language judgments and the paradigm translation, under a `Part 0` heading.
2.  The verification transcript for all three environment steps.
3.  The command-line and git checkpoint transcript (Part 1.5: navigation/search, the `ssh -T git@github.com` result, git commit/push, uv environment).
4.  The language autobiography (all four prompts, approximately one page).

Please also answer the following questions in your submission:

- If collaboration with a buddy was permitted, did you work with a buddy on this assignment?  If so, who?  If not, do you certify that this submission represents your own original work?  Please identify any and all portions of your submission that were not originally written by you.
- AI disclosure: list any generative-AI tools you used, for what, and how you verified the results (or state 'none').
- Approximately how many hours it took you to finish this assignment (I will not judge you for this at all; I am simply using it to gauge if the assignments are too easy or hard).
