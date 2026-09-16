# English Is Not a Context-Free Language

[![Python CI](https://github.com/natusikse/projectTheoryOfAutomata/actions/workflows/ci.yml/badge.svg)](https://github.com/natusikse/projectTheoryOfAutomata/actions/workflows/ci.yml)

A Python coursework project exploring formal languages, finite automata, and selected computational patterns inspired by James Higginbotham's paper *English Is Not a Context-Free Language*.

The repository combines a bounded natural-language experiment with exercises involving deterministic and nondeterministic finite automata, graph properties, language generation, and NFA-to-DFA conversion.

## Project Background

Context-free grammars are widely used to model hierarchical structures in programming languages and natural language syntax. However, some linguistic dependencies cannot be represented by a simple context-free model.

In his 1984 paper, James Higginbotham examines whether English can be described as a context-free language. His argument uses the closure property stating that the intersection of a context-free language with a regular language must also be context-free.

The project explores a bounded and simplified computational version of selected sentence patterns discussed in this context.

Example building blocks include:

```text
the woman such that
the man such that
she
gave him to him
gave him to this
gave this to him
gave this to this
left is here
```

The implementation generates artificial English-like strings and examines dependencies between repeated noun-phrase and verb-phrase structures.

It is intended as a computational learning exercise rather than an independent formal proof of Higginbotham's result.

## Repository Contents

### `project.py`

The main natural-language exploration.

It:

- generates bounded artificial English-like sentences;
- models a restricted regular sentence pattern;
- filters strings using constraints involving `him` and `this`;
- compares repeated noun-phrase and verb-phrase structures;
- explores token-count dependencies that are difficult to represent with a simple pushdown-automaton model.

### `HW_2.py`

Formal-languages coursework containing exercises related to:

- deterministic finite automata;
- nondeterministic finite automata;
- epsilon closures;
- word recognition;
- bounded language generation;
- NFA-to-DFA conversion.

### `HW_1.py`

Additional theoretical-computer-science exercises involving:

- finite graph validation;
- tree recognition;
- subgraph generation;
- palindrome generation;
- numerical sequence computation.

### `main.py`

An additional entry point retained from the original coursework submission.

## Requirements

- Python 3.10 or newer;
- no third-party dependencies.

The project uses only the Python standard library.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/natusikse/projectTheoryOfAutomata.git
cd projectTheoryOfAutomata
```

Run the natural-language exploration:

```bash
python3 project.py
```

Run the automata exercises:

```bash
python3 HW_2.py
```

Run the additional coursework files:

```bash
python3 HW_1.py
python3 main.py
```

## Automated Checks

GitHub Actions checks that every Python source file is syntactically valid under Python 3.10 and Python 3.13.

The workflow compiles the files without modifying their source code:

```bash
python3 -m py_compile HW_1.py HW_2.py main.py project.py
```

The workflow configuration is available in `.github/workflows/ci.yml`.

## Project Structure

```text
projectTheoryOfAutomata/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── HW_1.py
├── HW_2.py
├── main.py
├── project.py
└── README.md
```

## Concepts Demonstrated

- formal languages;
- context-free languages;
- closure properties;
- finite automata;
- deterministic and nondeterministic computation;
- epsilon transitions;
- NFA-to-DFA conversion;
- bounded language generation;
- graph and tree properties;
- computational exploration of linguistic dependencies.

## Scope and Limitations

- This is an educational coursework repository.
- The sentence generator explores only bounded examples.
- The implementation is a simplified computational interpretation of selected linguistic patterns.
- It does not independently reproduce the complete mathematical argument from the paper.
- The generated strings are artificial examples and should not be treated as a linguistic corpus.
- A finite computational experiment cannot by itself establish that an infinite language is not context-free.
- The project is intended to support learning about automata and formal-language theory rather than present a new linguistic proof.

## Reference

James Higginbotham. “English Is Not a Context-Free Language.” *Linguistic Inquiry*, Vol. 15, No. 2, Spring 1984, pp. 225–234.

[JSTOR: English Is Not a Context-Free Language](https://www.jstor.org/stable/4178381)

## Academic Context

This repository contains coursework and exploratory implementations created while studying theory of computation and formal languages.

The original Python source files are intentionally preserved. Subsequent repository improvements focus on documentation, reproducibility, automated syntax checks, and presentation rather than changing the underlying algorithms.