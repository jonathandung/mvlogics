# Operator reference

Each logic class implements as many operators that make sense for it as possible. They have standardized names, signatures and semantics as follows.

Note that the symbols shown are the operators as you would invoke them in Python, not the actual operators in logic.

## Shared by all logics

- ``__and__`` (&): And
- ``__or__`` (|): Or
- ``__invert__`` (~), ``__neg__`` (-): Not
- ``__pos__`` (+): Identity
- ``implies``: Implication
- ``iff``, ``xnor``: Biconditional
- ``nor``: Neither
- ``nand``: Sheffer stroke
- ``abjunction``: Nonimplication
- ``converse_implies``: Converse implication
- ``converse_abjunction``: Converse nonimplication

## Optional

- ``strong_conjunction``: Strong conjunction; not (a implies (not b))
- ``strong_disjunction``: Strong disjunction; (not a) implies b
- ``diamond``: Modal diamond; (not a) implies a
- ``box``: Modal box; not diamond(not a)
- ``doubtful``: a equivalent to (not a)
- ``gullibility``: a if a is equivalent to b, uncertain otherwise
- ``consensus``: a if a is equivalent to b; the other input if an input is uncertain, uncertain otherwise

## Truth table for boolean logic

| `P` | `Q` | `P&Q` | `P.__or__(Q)` | `~P` | `P.implies(Q)` | `P.iff(Q)` | `P.nor(Q)` | `P.nand(Q)` | `P.abjunction(Q)` | `P.converse_implies(Q)` | `P.converse_abjunction(Q)` |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | F | T | T | F | F | F | T | F |
| T | F | F | T | F | F | F | F | T | T | T | F |
| F | T | F | T | T | T | F | F | T | F | F | T |
| F | F | F | F | T | T | T | T | T | F | T | F |
