mvlogics.protocols
==================

.. py:module:: mvlogics.protocols


Classes
-------

.. autoapisummary::

   mvlogics.protocols.AbstractLogicBase
   mvlogics.protocols.DecimalLogicBase
   mvlogics.protocols.GödelLogic
   mvlogics.protocols.InfiniteLogicBase
   mvlogics.protocols.LogicBase
   mvlogics.protocols.MemberlessLogicBase
   mvlogics.protocols.PostLogic
   mvlogics.protocols.RationalLogicBase
   mvlogics.protocols.RationalTNormLogic
   mvlogics.protocols.StrictLogicBase
   mvlogics.protocols.TNormLogic
   mvlogics.protocols.ŁukasiewiczLogic


Module Contents
---------------

.. py:class:: AbstractLogicBase[T]

   Bases: :py:obj:`MemberlessLogicBase`


   .. py:property:: value
      :type: T



.. py:class:: DecimalLogicBase

   Bases: :py:obj:`InfiniteLogicBase`\ [\ :py:obj:`decimal.Decimal`\ ]


.. py:class:: GödelLogic

   Bases: :py:obj:`LogicBase`\ [\ :py:obj:`fractions.Fraction`\ ]


.. py:class:: InfiniteLogicBase[R]

   Bases: :py:obj:`AbstractLogicBase`\ [\ :py:obj:`R`\ ]


   .. py:attribute:: F
      :type:  ClassVar[Self]


   .. py:attribute:: T
      :type:  ClassVar[Self]


   .. py:attribute:: falsum
      :type:  ClassVar[Self]


   .. py:attribute:: members
      :type:  Final[dict[R, Self]]


   .. py:attribute:: verum
      :type:  ClassVar[Self]


.. py:class:: LogicBase[T]

   Bases: :py:obj:`AbstractLogicBase`\ [\ :py:obj:`T`\ ]


   .. py:class:: MemberContainer[R: LogicBase](values: dict[str, T])

      .. py:method:: __iter__() -> _collections_abc.Generator[R]


      .. py:method:: __set_name__(owner: type, name: str, /) -> None


      .. py:method:: from_name(name: str) -> R


      .. py:method:: generate(value: T) -> R


      .. py:method:: member_values() -> _collections_abc.Generator[T]


      .. py:method:: name_from_value(value: T, /) -> str


      .. py:method:: value_from_name(name: str, /) -> T


      .. py:property:: names
         :type: tuple[str, Ellipsis]


         Is not a property at runtime.




   .. py:attribute:: members
      :type:  Final[LogicBase.MemberContainer[Self]]


.. py:class:: MemberlessLogicBase

   .. py:method:: __and__(other: Self, /) -> Self


   .. py:method:: __invert__() -> Self


   .. py:method:: __neg__() -> Self


   .. py:method:: __or__(other: Self, /) -> Self


   .. py:method:: __pos__() -> Self


   .. py:method:: __xor__(other: Self, /) -> Self


   .. py:method:: abjunction(other: Self, /) -> Self


   .. py:method:: converse_abjunction(other: Self, /) -> Self


   .. py:method:: converse_implies(other: Self, /) -> Self


   .. py:method:: convert_to[L: MemberlessLogicBase](cls: type[L]) -> L


   .. py:method:: from_logic_member(member: MemberlessLogicBase) -> Self
      :classmethod:



   .. py:method:: from_normalized(val: fractions.Fraction) -> Self
      :classmethod:



   .. py:method:: iff(other: Self, /) -> Self


   .. py:method:: implies(other: Self, /) -> Self


   .. py:method:: nand(other: Self, /) -> Self


   .. py:method:: nor(other: Self, /) -> Self


   .. py:method:: normalized() -> fractions.Fraction


   .. py:method:: xnor(other: Self, /) -> Self


.. py:class:: PostLogic

   Bases: :py:obj:`LogicBase`\ [\ :py:obj:`fractions.Fraction`\ ]


.. py:class:: RationalLogicBase

   Bases: :py:obj:`InfiniteLogicBase`\ [\ :py:obj:`fractions.Fraction`\ ]


.. py:class:: RationalTNormLogic

   Bases: :py:obj:`RationalLogicBase`


   .. py:method:: strong_conjunction(other: Self, /) -> Self


.. py:class:: StrictLogicBase[T]

   Bases: :py:obj:`LogicBase`\ [\ :py:obj:`T`\ ]


   .. py:method:: consensus(other: Self, /) -> Self


   .. py:method:: gullibility(other: Self, /) -> Self


.. py:class:: TNormLogic

   Bases: :py:obj:`DecimalLogicBase`


   .. py:method:: strong_conjunction(other: Self, /) -> Self


.. py:class:: ŁukasiewiczLogic

   Bases: :py:obj:`LogicBase`\ [\ :py:obj:`fractions.Fraction`\ ]


   .. py:method:: box() -> Self


   .. py:method:: diamond() -> Self


   .. py:method:: doubtful() -> Self


   .. py:method:: strong_conjunction(other: Self, /) -> Self


   .. py:method:: strong_disjunction(other: Self, /) -> Self


