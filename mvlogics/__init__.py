# type: ignore
from .base import ALL_LOGICS, ALL_LOGICS_TUPLE, ALL_METHODS, EXTENSION_METHODS, FAKE_PROTOCOLS, FAKE_PROTOCOLS_TUPLE, FORBIDDEN, MIXIN_METHODS, RECOMMENDED_METHODS, REQUIRED_ATTRS, Decimal, Fraction, _AllLogicMeta, _DecimalLogicMeta, _FakeProtocolMeta, _FastEnumLogicMeta, _RationalLogicMeta, _singleton_new, _SubmoduleMeta, _all as __all__
def is_logic(typ): return isinstance(typ, _AllLogicMeta)
def is_logic_member(obj): return is_logic(type(obj))
def is_builtin_logic(typ): return typ.__name__ in ALL_LOGICS and typ.__module__ == __name__
def is_builtin_logic_member(obj): return is_builtin_logic(type(obj))
def convert(member, cls):
    if isinstance(member, type): cls, member = member, cls
    return member.convert_to(cls)
class Unit(metaclass=_AllLogicMeta):
    __new__ = _singleton_new; box = diamond = __invert__ = lambda self: self; __and__ = __or__ = implies = gullibility = consensus = lambda self, _, /: self
    def __bool__(self): raise TypeError('cannot convert Unit to bool')
    def __repr__(self): return 'Unit.T'
    def normalized(self): return Fraction(1) # noqa: PLR6301
    @classmethod
    def from_normalized(cls, val):
        if val == Fraction(1): return cls()
        raise ValueError(f'could not construct instance from val {val}')
    def __reduce__(self): return type(self), ()
Unit.T = Unit()
class Boolean(metaclass=_FastEnumLogicMeta):
    members = {'F': False, 'T': True}
    box = diamond = lambda self: self
    def __and__(self, other, /): return self and other
    def __or__(self, other, /): return self or other
    def __invert__(self): return type(self)(not self)
    def __reduce__(self): return type(self), (self.value,)
K3, LP = map(lambda n, g: _FastEnumLogicMeta(n, (), {'members': {'F': -1, 'I': 0, 'T': 1}, '__and__': lambda self, other, /: min(self, other), '__or__': lambda self, other, /: max(self, other), '__invert__': lambda self: type(self)(-self.value), '__bool__': lambda self: self.value >= (n == 'K'), 'gullibility': g, 'consensus': lambda self, other, /: self if self is other else other if self is (I := type(self).I) else self if other is I else I, 'normalized': lambda self: Fraction(self.value+1, 2), 'from_normalized': classmethod(lambda cls, val: cls(int(val*2-1)))}), ('K3', 'LP'), (lambda self, other, /: self if self is other else type(self).I, lambda self, other, /: self if self is other else other if self is (I := type(self).I) else self if other is I else type(self).F))
class BI3(metaclass=_FastEnumLogicMeta):
    members = {'F': -1, 'I': 0, 'T': 1}
    def __and__(self, other, /): return I if (I := __class__.I) in {self, other} else type(self)(min(self.value, other.value))
    def __or__(self, other, /): return I if (I := __class__.I) in {self, other} else type(self)(max(self.value, other.value))
    def __invert__(self): return type(self)(-self.value)
    def implies(self, other, /): return I if (I := __class__.I) in {self, other} else __class__.F if self is (T := __class__.T) and other is __class__.F else T
    def gullibility(self, other, /): return self if self is other else __class__.I
    def consensus(self, other, /): return self if len(s := {self, other}) == 1 else s.discard(__class__.I) or (s.pop() if len(s) == 1 else __class__.I)
    def normalized(self): return Fraction(self.value+1, 2)
    @classmethod
    def from_normalized(cls, val): return cls(int(val*2-1))
    def __reduce__(self): return type(self), (self.value,)
class RM3(metaclass=_FastEnumLogicMeta):
    members = {'F': -1, 'B': 0, 'T': 1}
    def __and__(self, other, /): return type(self)(min(self.value, other.value))
    def __or__(self, other, /): return type(self)(max(self.value, other.value))
    def __invert__(self): return type(self)(-self.value)
    def implies(self, other, /): return self if self is other else T if (self is (F := __class__.F))^(other is (T := __class__.T)) else F
    def normalized(self): return Fraction(self.value+1, 2)
    @classmethod
    def from_normalized(cls, val): return cls(int(val*2-1))
    def __reduce__(self): return type(self), (self.value,)
def _check_names(n, k, p):
    if k is None: k = len(n)
    elif n: raise ValueError('do not pass k with names')
    if k < 2: raise ValueError('k should be >= 2')
    return k, iter(n or map((p+'%s').__mod__, range(k)))
def _to_members(K, N): return {x: Fraction(i, K-1) for i, x in enumerate(N)}
def gödel_logic(*names, k=None, prefix='x_', clsname=None): K, N = _check_names(names, k, prefix); return _FastEnumLogicMeta(clsname or f'G{K}', (), {'members': _to_members(K, N), '__and__': lambda self, other, /: type(self)(min(self.value, other.value)), '__or__': lambda self, other, /: type(self)(max(self.value, other.value)), '__invert__': lambda self: type(self)(self.value == 0), 'implies': lambda self, other, /: type(self)(1) if self.value <= other.value else other, '__doc__': f"Godel's {K}-valued logic. See https://plato.stanford.edu/entries/logic-manyvalued/#GodLog."})
G3, SmT = gödel_logic('F', 'NF', 'T'), gödel_logic('F', 'NF', 'T', clsname='SmT')
def łukasiewicz_logic(*names, k=None, prefix='x_', clsname=None): K, N = _check_names(names, k, prefix); return _FastEnumLogicMeta(clsname or f'L{K}', (), {'members': _to_members(K, N), 'implies': (f := lambda self, other, /: type(self)(1+min(0, other.value-self.value))), '__invert__': lambda self: type(self)(1-self.value), '__and__': lambda self, other, /: f(f(self, other), other), '__or__': lambda self, other, /: ~(~self&~other), 'strong_disjunction': lambda self, other, /: f(~self, other), 'strong_conjunction': lambda self, other, /: ~f(self, ~other), 'diamond': (d := lambda self: f(~self, self)), 'box': lambda self: ~d(~self), 'doubtful': lambda self: self.iff(~self)})
L3 = łukasiewicz_logic('F', 'U', 'T')
def post_logic(*names, k=None, prefix='x_', clsname=None): K, N = _check_names(names, k, prefix); U = Fraction(1, K-1); return _FastEnumLogicMeta(clsname or f'P{K}', (), {'members': _to_members(K, N), '__invert__': lambda self: type(self)(v-U if (v := self.value) else 1), '__and__': lambda self, other, /: type(self)(min(self.value, other.value)), '__or__': lambda self, other, /: type(self)(max(self.value, other.value))})
P3 = post_logic('F', 'U', 'T')
class B4(metaclass=_FastEnumLogicMeta):
    members = {'F': 0, 'N': 1, 'B': 2, 'T': 3}
    def __invert__(self): return self if self in {__class__.B, __class__.N} else type(self)(3-self.value)
    def __bool__(self): return self.value >= 2
    def __and__(self, other, /):
        if (F := __class__.F) in {self, other}: return F
        if self is (T := __class__.T): return other
        if other is T: return self
        return self if self is other else F
    def __or__(self, other, /):
        if (T := __class__.T) in {self, other}: return T
        if self is (F := __class__.F): return other
        if other is F: return self
        return self if self is other else T
    def implies(self, other, /): return ~self|other
    def gullibility(self, other, /): return self if self is other else __class__.N
    def consensus(self, other, /): return self if len(s := {self, other}) == 1 else s.discard(__class__.N) or (s.pop() if len(s) == 1 else __class__.B)
    def normalized(self): return Fraction(self.value, 3)
    @classmethod
    def from_normalized(cls, val): return cls(int(val*3))
Π, Π_aleph_0 = map(lambda name, meta: meta(name, (), {'__and__': lambda self, other, /: type(self)(self.value*other.value), '__or__': lambda self, other, /: type(self)(min(self.value, other.value)), '__invert__': lambda self: self.implies(type(self).F), 'implies': lambda self, other, /: type(self)(b/a if (a := self.value) > (b := other.value) else 1)}), ('Π', 'Π_aleph_0'), (_DecimalLogicMeta, _RationalLogicMeta))
G_inf, G_aleph_0 = map(lambda name, meta: meta(name, (), {'__and__': lambda self, other, /: type(self)(self.value*other.value), '__or__': lambda self, other, /: type(self)(min(self.value, other.value)), '__invert__': lambda self: type(self)(self.value == 0), 'implies': lambda self, other, /: type(self).T if self.value <= other.value else other}), ('G_inf', 'G_aleph_0'), (_DecimalLogicMeta, _RationalLogicMeta))
L_inf, L_aleph_0 = map(lambda name, meta: meta(name, (), {'implies': lambda self, other, /: type(self)(1+min(0, other.value-self.value)), '__invert__': lambda self: type(self)(1-self.value), '__and__': lambda self, other, /: self.implies(other).implies(other), '__or__': lambda self, other, /: ~(~self&~other), 'strong_disjunction': lambda self, other, /: (~self).implies(other), 'strong_conjunction': lambda self, other, /: ~self.implies(~other), 'diamond': lambda self: (~self).implies(self), 'box': lambda self: ~(~self).diamond(), 'doubtful': lambda self: self.iff(~self)}), ('L_inf', 'L_aleph_0'), (_DecimalLogicMeta, _RationalLogicMeta))
def t_norm_logic(*, name=None, rational=False, **k):
    def dec(strong_conjunctionf):
        x, y, z = map(Decimal, ('0.3', '0.7', '0.5'))
        if strong_conjunctionf(x, y) != strong_conjunctionf(y, x): raise ValueError('t-norm must be commutative')
        if strong_conjunctionf(x, Decimal(1)) != x: raise ValueError('degree 1 must be neutral element')
        if strong_conjunctionf(Decimal('0.2'), z) > strong_conjunctionf(x, z): raise ValueError('t-norm must be non-decreasing')
        def implies(self, other, /):
            f = Decimal('0.001').__mul__
            if self is (_ := type(self)).F: return _.T
            s, u, v = 0, self.value, other.value
            for i in range(1001):
                if strong_conjunctionf(u, z := f(i)) <= v: s = z
            return type(self)(s)
        return (_RationalLogicMeta if rational else _DecimalLogicMeta)(name or strong_conjunctionf.__name__, (), {'strong_conjunction': lambda self, other, /: type(self)(strong_conjunctionf(self.value, other.value)), 'implies': implies, '__invert__': lambda self: self.implies(self.F), '__and__': lambda self, other: type(self)(min(self.value, other.value)), '__or__': lambda self, other, /: type(self)(max(self.value, other.value))}|k)
    return dec
def logic_from_implication(*, name=None, rational=False, **k): return lambda impliesf: (_RationalLogicMeta if rational else _DecimalLogicMeta)(name or impliesf.__name__, (), {'implies': impliesf, '__invert__': lambda self: self.implies(self.F), '__and__': lambda self, other: type(self)(min(self.value, other.value)), '__or__': lambda self, other, /: type(self)(max(self.value, other.value))}|k)
decimal_t_norm_logic, rational_t_norm_logic, decimal_logic_from_implication, rational_logic_from_implication = t_norm_logic(), t_norm_logic(rational=True), logic_from_implication(), logic_from_implication(rational=True)
NP, NP_aleph_0 = t_norm_logic(name='NP')(f := lambda u, v: min(u, v) if u+v > 1 else Decimal()), t_norm_logic(name='NP_aleph_0', rational=True)(f)
class protocols(metaclass=_SubmoduleMeta, _supermodule_default_name_='logics'): __all__, __dir__ = FAKE_PROTOCOLS_TUPLE, lambda: FAKE_PROTOCOLS_TUPLE # noqa: F811
for _ in FAKE_PROTOCOLS_TUPLE: setattr(protocols, _, _FakeProtocolMeta(_))