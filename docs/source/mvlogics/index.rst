mvlogics
========

.. py:module:: mvlogics

.. autoapi-nested-parse::

   Implementations of various logics, not necessarily with two truth values. A logic is a propositional calculus, with an example being Aristotle's
   logical calculus, where the only truth values are T and F and the law of the excluded middle holds. Logics do not support subclassing, analogously
   to the built-in type bool. Members of all classes in this module are lazily generated to avoid significant memory overhead.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /mvlogics/protocols/index


Attributes
----------

.. autoapisummary::

   mvlogics.ALL_LOGICS
   mvlogics.ALL_LOGICS_TUPLE
   mvlogics.ALL_METHODS
   mvlogics.EXTENSION_METHODS
   mvlogics.FAKE_PROTOCOLS
   mvlogics.FAKE_PROTOCOLS_TUPLE
   mvlogics.FORBIDDEN
   mvlogics.MIXIN_METHODS
   mvlogics.RECOMMENDED_METHODS
   mvlogics.REQUIRED_ATTRS


Classes
-------

.. autoapisummary::

   mvlogics.B4
   mvlogics.BI3
   mvlogics.Boolean
   mvlogics.G3
   mvlogics.G_aleph_0
   mvlogics.G_inf
   mvlogics.K3
   mvlogics.L3
   mvlogics.LP
   mvlogics.L_aleph_0
   mvlogics.L_inf
   mvlogics.NP
   mvlogics.NP_aleph_0
   mvlogics.P3
   mvlogics.RM3
   mvlogics.SmT
   mvlogics.Unit
   mvlogics.Π
   mvlogics.Π_aleph_0


Functions
---------

.. autoapisummary::

   mvlogics.convert
   mvlogics.decimal_logic_from_implication
   mvlogics.decimal_t_norm_logic
   mvlogics.gödel_logic
   mvlogics.is_builtin_logic
   mvlogics.is_builtin_logic_member
   mvlogics.is_logic
   mvlogics.is_logic_member
   mvlogics.logic_from_implication
   mvlogics.post_logic
   mvlogics.rational_logic_from_implication
   mvlogics.rational_t_norm_logic
   mvlogics.t_norm_logic
   mvlogics.łukasiewicz_logic


Package Contents
----------------

.. py:class:: B4

   Bases: :py:obj:`protocols.StrictLogicBase`\ [\ :py:obj:`int`\ ]


   Belnap's logic B_4, a combination of K_3 and P_3, such that the overdetermined I is called B for 'both', and the underdetermined N for 'neither' The truth tables are derived accordingly.


   .. py:method:: __and__(other: Self, /) -> Self


   .. py:method:: __invert__() -> Self


   .. py:method:: __or__(other: Self, /) -> Self


   .. py:method:: consensus(other: Self, /) -> Self


   .. py:method:: gullibility(other: Self, /) -> Self


   .. py:attribute:: B
      :type:  ClassVar[Self]


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: N
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


.. py:class:: BI3

   Bases: :py:obj:`protocols.StrictLogicBase`\ [\ :py:obj:`int`\ ]


   Dmitry Bochvar's internal three-value logic, also known as Kleene's weak three-value logic. The indeterminate truth value is contagious in the sense that it propagates as the result of any operation that involves it.


   .. py:method:: __and__(other: Self, /) -> Self


   .. py:method:: __invert__() -> Self


   .. py:method:: __or__(other: Self, /) -> Self


   .. py:method:: consensus(other: Self, /) -> Self


   .. py:method:: gullibility(other: Self, /) -> Self


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: I
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


.. py:class:: Boolean

   Bases: :py:obj:`protocols.LogicBase`\ [\ :py:obj:`bool`\ ]


   Boolean or Aristotelian logic, where the law of the excluded middle holds.
   Actually just a wrapper around the built-in class bool which satisfies the interface.


   .. py:method:: __and__(other: Self, /) -> Self


   .. py:method:: __invert__() -> Self


   .. py:method:: __or__(other: Self, /) -> Self


   .. py:method:: box() -> Self


   .. py:method:: diamond() -> Self


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


.. py:class:: G3

   Bases: :py:obj:`protocols.GödelLogic`


   A three-valued logic of Gödel's, also known as Smetanov logic and the logic of here and there. Belongs to a larger family of 'Gödel' logics G_k with truth values 0, 1/(k-1), 2/(k-1), ..., (k-2)/(k-1), 1, with 1 designated as a 'true' truth value.


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: NF
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


.. py:class:: G_aleph_0

   Bases: :py:obj:`protocols.RationalLogicBase`


   Gödel's infinite-valued logic, with rational numbers between 0 and 1 as truth values.


.. py:class:: G_inf

   Bases: :py:obj:`protocols.DecimalLogicBase`


   Gödel's infinite-valued logic, with real numbers between 0 and 1 as truth values.


.. py:class:: K3

   Bases: :py:obj:`protocols.StrictLogicBase`\ [\ :py:obj:`int`\ ]


   Kleene's strong logic of indeterminancy (K_3), in which besides the truth values T and F, a new 'indeterminate' truth value I is introduced.
   T is the only designated truth value.


   .. py:method:: __and__(other: Self, /) -> Self


   .. py:method:: __invert__() -> Self


   .. py:method:: __or__(other: Self, /) -> Self


   .. py:method:: consensus(other: Self, /) -> Self


   .. py:method:: gullibility(other: Self, /) -> Self


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: I
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


.. py:class:: L3

   Bases: :py:obj:`protocols.ŁukasiewiczLogic`


   Jan Łukasiewicz's three-valued logic; the truth values for 0, 1/2, 1 are called F, U and T respectively.


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


   .. py:attribute:: U
      :type:  ClassVar[Self]


.. py:class:: LP

   Bases: :py:obj:`protocols.StrictLogicBase`\ [\ :py:obj:`int`\ ]


   Priest's 'logic of paradox' (P_3), provisionally named LP because P_3 refers to ternary Post logic here. The truth tables are equivalent to those of Kleene's, except I is also designated as a truth value. The gullibility operation is thus not as well-defined as in K_3, and in the case that one operand is T and the other F, the arbitrary convention to return F is chosen.


   .. py:method:: __and__(other: Self, /) -> Self


   .. py:method:: __invert__() -> Self


   .. py:method:: __or__(other: Self, /) -> Self


   .. py:method:: consensus(other: Self, /) -> Self


   .. py:method:: gullibility(other: Self, /) -> Self


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: I
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


.. py:class:: L_aleph_0

   Bases: :py:obj:`protocols.RationalLogicBase`


   Łukasiewicz's infinite-valued logic, with rational numbers between 0 and 1 as truth values.


   .. py:method:: box() -> Self


   .. py:method:: diamond() -> Self


   .. py:method:: doubtful() -> Self


   .. py:method:: strong_conjunction(other: Self, /) -> Self


   .. py:method:: strong_disjunction(other: Self, /) -> Self


.. py:class:: L_inf

   Bases: :py:obj:`protocols.DecimalLogicBase`


   Łukasiewicz's infinite-valued logic, with real numbers between 0 and 1 as truth values.


   .. py:method:: box() -> Self


   .. py:method:: diamond() -> Self


   .. py:method:: doubtful() -> Self


   .. py:method:: strong_conjunction(other: Self, /) -> Self


   .. py:method:: strong_disjunction(other: Self, /) -> Self


.. py:class:: NP

   Bases: :py:obj:`protocols.TNormLogic`


   A t-norm logic with the nilpotent minimum norm as the implication operator.


.. py:class:: NP_aleph_0

   Bases: :py:obj:`protocols.RationalTNormLogic`


   A t-norm logic with the nilpotent minimum norm as the implication operator and rational truth values only.


.. py:class:: P3

   Bases: :py:obj:`protocols.PostLogic`


   Ternary Post logic, with a cyclic implementation of the negation operator.


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


   .. py:attribute:: U
      :type:  ClassVar[Self]


.. py:class:: RM3

   Bases: :py:obj:`protocols.LogicBase`\ [\ :py:obj:`int`\ ]


   The R-mingle 3 logic, whose significance lies in its material implication implementation. The axiom of weakening does not hold in RM3.


   .. py:method:: __and__(other: Self, /) -> Self


   .. py:method:: __invert__() -> Self


   .. py:method:: __or__(other: Self, /) -> Self


   .. py:attribute:: B
      :type:  ClassVar[Self]


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


.. py:class:: SmT

   Bases: :py:obj:`protocols.GödelLogic`


   Smetanov logic, also known as the logic of here and there and Gödel G3 logic. Introduced by Arend Heyting in 1930 to study intuitionistic logic, it is a three-valued intermediate logic where the intermediate value can be understood as 'not false'.


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: NF
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


.. py:class:: Unit

   Bases: :py:obj:`protocols.MemberlessLogicBase`


   An implementation of a single-valued logic. May be useful as a base case in various recursive operations.


   .. py:method:: __and__(other: Self, /) -> Self


   .. py:method:: __bool__() -> NoReturn


   .. py:method:: __invert__() -> Self


   .. py:method:: __or__(other: Self, /) -> Self


   .. py:method:: box() -> Self


   .. py:method:: consensus(other: Self, /) -> Self


   .. py:method:: diamond() -> Self


   .. py:method:: gullibility(other: Self, /) -> Self


   .. py:attribute:: T
      :type:  ClassVar[Self]


.. py:class:: Π

   Bases: :py:obj:`protocols.DecimalLogicBase`


   Product logic, with truth values between 0 and 1. For precision, please pass in a string (e.g. '3.14159' instead of 3.14159) to the constructor; however, passing an int, float or decimal.Decimal instance is also acceptable.


.. py:class:: Π_aleph_0

   Bases: :py:obj:`protocols.RationalLogicBase`


   Product logic, with rational numbers between 0 and 1 as truth values. Pass in what Fraction takes to the constructor.


.. py:function:: convert[L: protocols.MemberlessLogicBase](member: protocols.MemberlessLogicBase, cls: type[L]) -> L

.. py:function:: decimal_logic_from_implication(impliesf: _collections_abc.Callable[[decimal.Decimal, decimal.Decimal], decimal.Decimal]) -> type[protocols.DecimalLogicBase]

   Version of `logic_from_implication` specific to decimals.


.. py:function:: decimal_t_norm_logic(strong_conjunctionf: _collections_abc.Callable[[decimal.Decimal, decimal.Decimal], decimal.Decimal]) -> type[protocols.TNormLogic]

   Version of `t_norm_logic` specific to decimals.


.. py:function:: gödel_logic(name_1: str, name_2: str, /, *names: str, clsname: str | None = ...) -> type[protocols.GödelLogic]
                 gödel_logic(*, k: int, prefix: str = ..., clsname: str | None = ...) -> type[protocols.GödelLogic]

.. py:function:: is_builtin_logic(typ: type) -> TypeGuard[type[protocols.LogicBase[Any] | Unit]]

.. py:function:: is_builtin_logic_member(obj: object) -> TypeGuard[protocols.LogicBase[Any] | Unit]

.. py:function:: is_logic(typ: type) -> TypeGuard[type[protocols.MemberlessLogicBase]]

.. py:function:: is_logic_member(obj: object) -> TypeGuard[protocols.MemberlessLogicBase]

.. py:function:: logic_from_implication(*, name: str, rational: Literal[False] = False, **additional: Any) -> _collections_abc.Callable[[_collections_abc.Callable[[decimal.Decimal, decimal.Decimal], decimal.Decimal]], type[protocols.DecimalLogicBase]]
                 logic_from_implication(*, name: str, rational: Literal[True], **additional: Any) -> _collections_abc.Callable[[_collections_abc.Callable[[fractions.Fraction, fractions.Fraction], fractions.Fraction]], type[protocols.RationalLogicBase]]
                 logic_from_implication(*, rational: Literal[False] = False, **additional: Any) -> _collections_abc.Callable[[_collections_abc.Callable[[decimal.Decimal, decimal.Decimal], decimal.Decimal]], type[protocols.DecimalLogicBase]]
                 logic_from_implication(*, rational: Literal[True], **additional: Any) -> _collections_abc.Callable[[_collections_abc.Callable[[fractions.Fraction, fractions.Fraction], fractions.Fraction]], type[protocols.RationalLogicBase]]

.. py:function:: post_logic(name_1: str, name_2: str, /, *names: str, clsname: str | None = ...) -> type[protocols.PostLogic]
                 post_logic(*, k: int, prefix: str = ..., clsname: str | None = ...) -> type[protocols.PostLogic]

.. py:function:: rational_logic_from_implication(impliesf: _collections_abc.Callable[[fractions.Fraction, fractions.Fraction], fractions.Fraction]) -> type[protocols.RationalLogicBase]

   Version of `logic_from_implication` specific to fractions.


.. py:function:: rational_t_norm_logic(strong_conjunctionf: _collections_abc.Callable[[fractions.Fraction, fractions.Fraction], fractions.Fraction]) -> type[protocols.RationalTNormLogic]

   Version of `t_norm_logic` specific to fractions.


.. py:function:: t_norm_logic(*, name: str, rational: Literal[False] = False, **additional: Any) -> _collections_abc.Callable[[_collections_abc.Callable[[decimal.Decimal, decimal.Decimal], decimal.Decimal]], type[protocols.TNormLogic]]
                 t_norm_logic(*, name: str, rational: Literal[True], **additional: Any) -> _collections_abc.Callable[[_collections_abc.Callable[[fractions.Fraction, fractions.Fraction], fractions.Fraction]], type[protocols.RationalTNormLogic]]
                 t_norm_logic(*, rational: Literal[False] = False, **additional: Any) -> _collections_abc.Callable[[_collections_abc.Callable[[decimal.Decimal, decimal.Decimal], decimal.Decimal]], type[protocols.TNormLogic]]
                 t_norm_logic(*, rational: Literal[True], **additional: Any) -> _collections_abc.Callable[[_collections_abc.Callable[[fractions.Fraction, fractions.Fraction], fractions.Fraction]], type[protocols.RationalTNormLogic]]

.. py:function:: łukasiewicz_logic(name_1: str, name_2: str, /, *names: str, clsname: str | None = ...) -> type[protocols.ŁukasiewiczLogic]
                 łukasiewicz_logic(*, k: int, prefix: str = ..., clsname: str | None = ...) -> type[protocols.ŁukasiewiczLogic]

.. py:data:: ALL_LOGICS
   :type:  frozenset[str]

.. py:data:: ALL_LOGICS_TUPLE
   :type:  tuple[str, Ellipsis]

.. py:data:: ALL_METHODS
   :type:  frozenset[str]

.. py:data:: EXTENSION_METHODS
   :type:  frozenset[str]

.. py:data:: FAKE_PROTOCOLS
   :type:  frozenset[str]

.. py:data:: FAKE_PROTOCOLS_TUPLE
   :type:  tuple[str, Ellipsis]

.. py:data:: FORBIDDEN
   :type:  frozenset[str]

.. py:data:: MIXIN_METHODS
   :type:  frozenset[str]

.. py:data:: RECOMMENDED_METHODS
   :type:  frozenset[str]

.. py:data:: REQUIRED_ATTRS
   :type:  frozenset[str]

