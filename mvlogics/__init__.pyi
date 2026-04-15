'''Implementations of various logics, not necessarily with two truth values. A logic is a propositional calculus, with an example being Aristotle's
logical calculus, where the only truth values are T and F and the law of the excluded middle holds. Logics do not support subclassing, analogously
to the built-in type bool. Members of all classes in this module are lazily generated to avoid significant memory overhead.'''
from _collections_abc import Callable
from decimal import Decimal
from fractions import Fraction
from typing import Any, ClassVar, Final, Literal, NoReturn, Self, TypeGuard, final, overload
from .protocols import DecimalLogicBase, GödelLogic, LogicBase, MemberlessLogicBase, PostLogic, RationalLogicBase, RationalTNormLogic, StrictLogicBase, TNormLogic, ŁukasiewiczLogic
__all__ = 'ALL_LOGICS', 'ALL_LOGICS_TUPLE', 'ALL_METHODS', 'B4', 'BI3', 'EXTENSION_METHODS', 'FAKE_PROTOCOLS', 'FAKE_PROTOCOLS_TUPLE', 'FORBIDDEN', 'G3', 'K3', 'L3', 'LP', 'MIXIN_METHODS', 'NP', 'P3', 'RECOMMENDED_METHODS', 'REQUIRED_ATTRS', 'RM3', 'Π', 'Boolean', 'G_aleph_0', 'G_inf', 'L_aleph_0', 'L_inf', 'NP_aleph_0', 'SmT', 'Unit', 'Π_aleph_0', 'convert', 'decimal_logic_from_implication', 'decimal_t_norm_logic', 'gödel_logic', 'is_builtin_logic', 'is_builtin_logic_member', 'is_logic', 'is_logic_member', 'logic_from_implication', 'post_logic', 'rational_logic_from_implication', 'rational_t_norm_logic', 't_norm_logic', 'łukasiewicz_logic'
__version__: Final[str]
REQUIRED_ATTRS: frozenset[str]
'''The method names all logic classes must have.'''
RECOMMENDED_METHODS: frozenset[str]
'''The method names logic classes are recommended to have if suitable, corresponding to less common logical operations.'''
MIXIN_METHODS: frozenset[str]
'''The method names of methods that will be provided automatically to logic base classes.'''
EXTENSION_METHODS: frozenset[str]
'''The method names logic classes may have for specialized use cases, including possibly niche fuzzy and modal logic operators.'''
FORBIDDEN: frozenset[str]
'''Method/property names logic classes are forbidden from implementing.'''
ALL_METHODS: frozenset[str]
'''Equivalent to RECOMMEDED_METHODS | REQUIRED_ATTRS | MIXIN_METHODS | EXTENSION_METHODS.'''
FAKE_PROTOCOLS: frozenset[str]
'''The names of the 'protocols' defined in the `protocols` submodule, which support instance and subclass testing.'''
ALL_LOGICS: frozenset[str]
'''The names of all built-in logics defined in this module.'''
FAKE_PROTOCOLS_TUPLE: tuple[str, ...]
'''`FAKE_PROTOCOLS` as a tuple with a canonical ordering.'''
ALL_LOGICS_TUPLE: tuple[str, ...]
'''`ALL_LOGICS` as a tuple with a canonical ordering.'''
def convert[L: MemberlessLogicBase](member: MemberlessLogicBase, cls: type[L]) -> L: '''Convert a logic member `member` to a member of another logic class `cls`.'''
def is_logic(typ: type) -> TypeGuard[type[MemberlessLogicBase]]: '''Return whether `typ` is a logic class.'''
def is_logic_member(obj: object) -> TypeGuard[MemberlessLogicBase]: '''Return whether `obj` is a logic member.'''
def is_builtin_logic(typ: type) -> TypeGuard[type[LogicBase[Any]|Unit]]: '''Return whether `typ` is a built-in logic class.'''
def is_builtin_logic_member(obj: object) -> TypeGuard[LogicBase[Any]|Unit]: '''Return whether `obj` is a member of a built-in logic class.'''
@final
class Unit(MemberlessLogicBase):
    '''An implementation of a single-valued logic. May be useful as a base case in various recursive operations.'''
    T: ClassVar[Self]
    def __new__(cls) -> Self: ...
    def __and__(self, other: Self, /) -> Self: ...
    def __or__(self, other: Self, /) -> Self: ...
    def __invert__(self) -> Self: ...
    def box(self) -> Self: ...
    def diamond(self) -> Self: ...
    def gullibility(self, other: Self, /) -> Self: ...
    def consensus(self, other: Self, /) -> Self: ...
    def __bool__(self) -> NoReturn: ...
@final
class Boolean(LogicBase[bool]):
    '''Boolean or Aristotelian logic, where the law of the excluded middle holds.
    Simply wraps the built-in class `bool` to satisfy the interface.'''
    T: ClassVar[Self]
    F: ClassVar[Self]
    def __and__(self, other: Self, /) -> Self: ...
    def __or__(self, other: Self, /) -> Self: ...
    def __invert__(self) -> Self: ...
    def box(self) -> Self: ...
    def diamond(self) -> Self: ...
@final
class K3(StrictLogicBase[int]):
    '''Kleene's strong logic of indeterminancy (K_3), in which besides the truth values T and F, a new 'indeterminate' truth value I is introduced.
    T is the only designated truth value.'''
    T: ClassVar[Self]
    I: ClassVar[Self]
    F: ClassVar[Self]
    def __and__(self, other: Self, /) -> Self: ...
    def __or__(self, other: Self, /) -> Self: ...
    def __invert__(self) -> Self: ...
    def gullibility(self, other: Self, /) -> Self: ...
    def consensus(self, other: Self, /) -> Self: ...
@final
class LP(StrictLogicBase[int]):
    '''Priest's 'logic of paradox' (P_3), provisionally named LP because P_3 refers to ternary Post logic here. The truth tables are equivalent to those of Kleene's, except I is also designated as a truth value. The gullibility operation is thus not as well-defined as in K_3, and in the case that one operand is T and the other F, the arbitrary convention to return F is chosen.'''
    T: ClassVar[Self]
    I: ClassVar[Self]
    F: ClassVar[Self]
    def __and__(self, other: Self, /) -> Self: ...
    def __or__(self, other: Self, /) -> Self: ...
    def __invert__(self) -> Self: ...
    def gullibility(self, other: Self, /) -> Self: ...
    def consensus(self, other: Self, /) -> Self: ...
@final
class BI3(StrictLogicBase[int]):
    '''Dmitry Bochvar's internal three-value logic, also known as Kleene's weak three-value logic. The indeterminate truth value is contagious in the sense that it propagates as the result of any operation that involves it.'''
    T: ClassVar[Self]
    I: ClassVar[Self]
    F: ClassVar[Self]
    def __and__(self, other: Self, /) -> Self: ...
    def __or__(self, other: Self, /) -> Self: ...
    def __invert__(self) -> Self: ...
    def gullibility(self, other: Self, /) -> Self: ...
    def consensus(self, other: Self, /) -> Self: ...
@final
class RM3(LogicBase[int]):
    '''The R-mingle 3 logic, whose significance lies in its material implication implementation. The axiom of weakening does not hold in RM3.'''
    T: ClassVar[Self]
    B: ClassVar[Self]
    F: ClassVar[Self]
    def __and__(self, other: Self, /) -> Self: ...
    def __or__(self, other: Self, /) -> Self: ...
    def __invert__(self) -> Self: ...
@final
class B4(StrictLogicBase[int]):
    '''Belnap's logic B_4, a combination of K_3 and P_3, such that the overdetermined I is called B for 'both', and the underdetermined N for 'neither' The truth tables are derived accordingly.'''
    T: ClassVar[Self]
    B: ClassVar[Self]
    N: ClassVar[Self]
    F: ClassVar[Self]
    def __and__(self, other: Self, /) -> Self: ...
    def __or__(self, other: Self, /) -> Self: ...
    def __invert__(self) -> Self: ...
    def gullibility(self, other: Self, /) -> Self: ...
    def consensus(self, other: Self, /) -> Self: ...
@final
class SmT(GödelLogic):
    '''Smetanov logic, also known as the logic of here and there and Gödel G3 logic. Introduced by Arend Heyting in 1930 to study intuitionistic logic, it is a three-valued intermediate logic where the intermediate value can be understood as 'not false'.'''
    T: ClassVar[Self]
    NF: ClassVar[Self]
    F: ClassVar[Self]
@final
class G3(GödelLogic):
    '''A three-valued logic of Gödel's, also known as Smetanov logic and the logic of here and there. Belongs to a larger family of 'Gödel' logics G_k with truth values 0, 1/(k-1), 2/(k-1), ..., (k-2)/(k-1), 1, with 1 designated as a 'true' truth value.'''
    T: ClassVar[Self]
    NF: ClassVar[Self]
    F: ClassVar[Self]
@final
class L3(ŁukasiewiczLogic):
    '''Jan Łukasiewicz's three-valued logic; the truth values for 0, 1/2, 1 are called F, U and T respectively.'''
    T: ClassVar[Self]
    U: ClassVar[Self]
    F: ClassVar[Self]
@final
class P3(PostLogic):
    '''Ternary Post logic, with a cyclic implementation of the negation operator.'''
    T: ClassVar[Self]
    U: ClassVar[Self]
    F: ClassVar[Self]
@final
class Π(DecimalLogicBase): '''Product logic, with truth values between 0 and 1. For precision, please pass in a string (e.g. '3.14159' instead of 3.14159) to the constructor; however, passing an int, float or decimal.Decimal instance is also acceptable.'''
@final
class G_inf(DecimalLogicBase): '''Gödel's infinite-valued logic, with real numbers between 0 and 1 as truth values.'''
@final
class L_inf(DecimalLogicBase):
    '''Łukasiewicz's infinite-valued logic, with real numbers between 0 and 1 as truth values.'''
    def strong_disjunction(self, other: Self, /) -> Self: ...
    def strong_conjunction(self, other: Self, /) -> Self: ...
    def diamond(self) -> Self: ...
    def box(self) -> Self: ...
    def doubtful(self) -> Self: ...
@final
class NP(TNormLogic): '''A t-norm logic with the nilpotent minimum norm as the implication operator.'''
@final
class Π_aleph_0(RationalLogicBase): '''Product logic, with rational numbers between 0 and 1 as truth values. Pass in what Fraction takes to the constructor.'''
@final
class G_aleph_0(RationalLogicBase): '''Gödel's infinite-valued logic, with rational numbers between 0 and 1 as truth values.'''
@final
class L_aleph_0(RationalLogicBase):
    '''Łukasiewicz's infinite-valued logic, with rational numbers between 0 and 1 as truth values.'''
    def strong_disjunction(self, other: Self, /) -> Self: ...
    def strong_conjunction(self, other: Self, /) -> Self: ...
    def diamond(self) -> Self: ...
    def box(self) -> Self: ...
    def doubtful(self) -> Self: ...
@final
class NP_aleph_0(RationalTNormLogic): '''A t-norm logic with the nilpotent minimum norm as the implication operator and rational truth values only.'''
@overload
def gödel_logic(name_1: str, name_2: str, /, *names: str, clsname: str|None=...) -> type[GödelLogic]: '''Returns a Gödel logic class with name clsname and truth values of names name_1 (0), name_2 (1/(k-1)), ..., name_(k-1) ((k-2)/(k-1)), name_k (1).'''
@overload
def gödel_logic(*, k: int, prefix: str=..., clsname: str|None=...) -> type[GödelLogic]: ...
@overload
def łukasiewicz_logic(name_1: str, name_2: str, /, *names: str, clsname: str|None=...) -> type[ŁukasiewiczLogic]: '''Returns a Łukasiewicz logic class with name clsname and truth values of names name_1 (0), name_2 (1/(k-1)), ..., name_(k-1) ((k-2)/(k-1)), name_k (1).'''
@overload
def łukasiewicz_logic(*, k: int, prefix: str=..., clsname: str|None=...) -> type[ŁukasiewiczLogic]: ...
@overload
def post_logic(name_1: str, name_2: str, /, *names: str, clsname: str|None=...) -> type[PostLogic]: '''Returns a Postlogic class with name `clsname` and truth values of names `name_1` (0), `name_2` (1/(k-1)), ..., `name_(k-1)` ((k-2)/(k-1)), `name_k` (1).'''
@overload
def post_logic(*, k: int, prefix: str=..., clsname: str|None=...) -> type[PostLogic]: ...
@overload
def t_norm_logic(*, name: str, rational: Literal[False]=False, **additional: Any) -> Callable[[Callable[[Decimal, Decimal], Decimal]], type[TNormLogic]]: '''A decorator factory whose products return t-norm logic classes given the strong conjunction operator, given whether the members should be constrained to rational numbers.'''
@overload
def t_norm_logic(*, name: str, rational: Literal[True], **additional: Any) -> Callable[[Callable[[Fraction, Fraction], Fraction]], type[RationalTNormLogic]]: ...
@overload
def t_norm_logic(*, rational: Literal[False]=False, **additional: Any) -> Callable[[Callable[[Decimal, Decimal], Decimal]], type[TNormLogic]]: ...
@overload
def t_norm_logic(*, rational: Literal[True], **additional: Any) -> Callable[[Callable[[Fraction, Fraction], Fraction]], type[RationalTNormLogic]]: ...
@overload
def logic_from_implication(*, name: str, rational: Literal[False]=False, **additional: Any) -> Callable[[Callable[[Decimal, Decimal], Decimal]], type[DecimalLogicBase]]: '''A decorator factory whose products return logic classes given the implication operator only, given whether the members should be constrained to rational numbers.'''
@overload
def logic_from_implication(*, name: str, rational: Literal[True], **additional: Any) -> Callable[[Callable[[Fraction, Fraction], Fraction]], type[RationalLogicBase]]: ...
@overload
def logic_from_implication(*, rational: Literal[False]=False, **additional: Any) -> Callable[[Callable[[Decimal, Decimal], Decimal]], type[DecimalLogicBase]]: ...
@overload
def logic_from_implication(*, rational: Literal[True], **additional: Any) -> Callable[[Callable[[Fraction, Fraction], Fraction]], type[RationalLogicBase]]: ...
def decimal_t_norm_logic(strong_conjunctionf: Callable[[Decimal, Decimal], Decimal]) -> type[TNormLogic]: '''Version of `t_norm_logic` specific to decimals.'''
def rational_t_norm_logic(strong_conjunctionf: Callable[[Fraction, Fraction], Fraction]) -> type[RationalTNormLogic]: '''Version of `t_norm_logic` specific to fractions.'''
def decimal_logic_from_implication(impliesf: Callable[[Decimal, Decimal], Decimal]) -> type[DecimalLogicBase]: '''Version of `logic_from_implication` specific to decimals.'''
def rational_logic_from_implication(impliesf: Callable[[Fraction, Fraction], Fraction]) -> type[RationalLogicBase]: '''Version of `logic_from_implication` specific to fractions.'''
