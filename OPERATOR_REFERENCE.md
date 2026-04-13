# Operator reference

Each logic class implements as many operators that make sense for it as possible. They have standardized names, signatures and semantics, as follows:

## Shared by all logics

`__and__`: And
`__or__`: Or
`__invert__`, `__neg__`: Not
`__pos__`: Identity
`implies`: Implication
`iff`, `xnor`: Biconditional
`nor`: Neither
`nand`: Sheffer stroke
`abjunction`: Nonimplication
`converse_implies`: Converse implication
`converse_abjunction`: Converse nonimplication

## Optional

`strong_conjunction`: Strong conjunction; not (a implies (not b))
`strong_disjunction`: Strong disjunction; (not a) implies b
`diamond`: Modal diamond; (not a) implies a
`box`: Modal box; not diamond(not a)
`doubtful`: a equivalent to (not a)
`gullibility`: a if a is equivalent to b, uncertain otherwise
`consensus`: a if a is equivalent to b; the other input if an input is uncertain, uncertain otherwise
