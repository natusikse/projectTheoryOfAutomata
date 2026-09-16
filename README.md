# English Is Not a Context-Free Language

A Python coursework project exploring formal-language concepts from James Higginbotham's 1984 paper, *English Is Not a Context-Free Language*.

The repository also contains exercises on deterministic and nondeterministic finite automata, graph properties, language generation, and NFA-to-DFA conversion.

## Project Background

Higginbotham considers whether English can be described as a context-free language.

The argument uses the closure property stating that the intersection of a context-free language with a regular language must also be context-free. Higginbotham constructs a regular set of English-like sentence patterns and argues that its intersection with English is not context-free.

The central pattern includes expressions such as:

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

The Python implementation explores a bounded, simplified version of these sentence patterns and their token-count dependencies.

## Repository Contents

### `project.py`

The main exploratory implementation:

- generates bounded artificial English-like sentences;
- models a regular sentence pattern;
- filters strings using constraints involving `him` and `this`;
- compares repeated noun-phrase and verb-phrase structures;
- identifies examples that illustrate the difficulty of tracking multiple dependencies with a simple pushdown-automaton model.

### `HW_2.py`

Formal-languages coursework containing:

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

## Running the Project

Requirements:

- Python 3.10+

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

## Scope and Limitations

- This is an educational coursework repository.
- The sentence generator explores only bounded examples.
- The implementation is a simplified computational interpretation of selected patterns from the paper.
- It does not independently reproduce the complete mathematical argument.
- The generated strings should not be treated as a linguistic corpus.
- The simulation is intended to support learning about formal languages rather than establish a new proof.

## Reference

James Higginbotham. “English Is Not a Context-Free Language.” *Linguistic Inquiry*, volume 15, 1984.

JSTOR: [https://www.jstor.org/stable/4178381](https://www.jstor.org/stable/4178381)