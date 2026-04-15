# type: ignore
import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from weakref import WeakKeyDictionary
def _weak_cache(name=None):
    def dec(f):
        def g(self, _=WeakKeyDictionary()): # noqa: B008
            if (r := _.get(self, s := _SlowEnumLogicMeta.MemberContainer._NOT_GENERATED)) is s: _[self] = r = f(self)
            return r
        g.__name__ = name or f.__name__; return g
    return dec
_normalized_cache, _repr_cache = map(_weak_cache, ('normalized', '__repr__'))
REQUIRED_ATTRS, FORBIDDEN = map(frozenset, (('__and__', '__or__', '__invert__'), ('__new__', 'value')))
(_singleton_new := lambda cls: _singleton_new.cache.get(cls, False) or object.__new__(cls)).cache, getcontext().prec = WeakKeyDictionary(), 100
_all, ALL_METHODS, ALL_LOGICS, FAKE_PROTOCOLS = ('ALL_METHODS', 'FORBIDDEN', 'ALL_LOGICS', 'ALL_LOGICS_TUPLE', 'FAKE_PROTOCOLS', 'FAKE_PROTOCOLS_TUPLE', 'REQUIRED_ATTRS', 'RECOMMENDED_METHODS', 'MIXIN_METHODS', 'EXTENSION_METHODS', 'protocols', 'is_logic', 'is_logic_member', 'is_builtin_logic', 'is_builtin_logic_member', 'convert', 'gödel_logic', 'łukasiewicz_logic', 'post_logic', 't_norm_logic', 'logic_from_implication', 'decimal_t_norm_logic', 'rational_t_norm_logic', 'decimal_logic_from_implication', 'rational_logic_from_implication', *(ALL_LOGICS_TUPLE := ('Unit', 'Boolean', 'K3', 'LP', 'BI3', 'RM3', 'G3', 'SmT', 'L3', 'P3', 'B4', 'Π', 'Π_aleph_0', 'G_inf', 'G_aleph_0', 'L_inf', 'L_aleph_0', 'NP', 'NP_aleph_0'))), REQUIRED_ATTRS|(RECOMMENDED_METHODS := frozenset(('implies', '__bool__', 'gullibility', 'consensus')))|(MIXIN_METHODS := frozenset(('iff', 'implies', '__pos__', '__neg__', '__xor__', 'value', 'nand', 'nor', 'xnor', 'abjunction', 'converse_implies', 'converse_abjunction')))|(EXTENSION_METHODS := frozenset(('strong_disjunction', 'strong_conjunction', 'diamond', 'box', 'doubtful', 'gullibility', 'consensus'))), frozenset(ALL_LOGICS_TUPLE), frozenset(FAKE_PROTOCOLS_TUPLE := ('MemberlessLogicBase', 'AbstractLogicBase', 'LogicBase', 'InfiniteLogicBase', 'DecimalLogicBase', 'RationalLogicBase', 'StrictLogicBase', 'GödelLogic', 'ŁukasiewiczLogic', 'PostLogic', 'TNormLogic', 'RationalTNormLogic'))
class _SubmoduleMeta(type):
    def __new__(mcls, name, bases, namespace, /, *, _supermodule_default_name_='<unknown>'):
        if bases: raise TypeError('Submodule cannot inherit from other classes')
        try: name = f'{sys._getframemodulename(1) or _supermodule_default_name_}.{name}'
        except AttributeError: name = f'{_supermodule_default_name_}.{name}'
        sys.modules[name] = r = type(sys)(name, namespace.pop('__doc__', None)); return r
class _AllLogicMeta(type):
    __defaults, __repr__ = None, _repr_cache(lambda cls: f'logics.{cls.__name__}')
    def __new__(mcls, name, bases, namespace, /, **k):
        if bases: raise ValueError('logics cannot inherit from anything')
        if not REQUIRED_ATTRS.issubset(namespace): raise TypeError('missing methods for logic class')
        return super().__new__(mcls, name, bases, mcls.__default_factory__()|namespace, **k)
    @classmethod
    def __default_factory__(mcls):
        if (r := mcls.__defaults) is None: mcls.__defaults = r = {'__xor__': lambda self, other, /: (self&~other)|(other&~self), 'implies': lambda self, other, /: ~self|other, 'iff': (g := lambda self, other: self.implies(other)&other.implies(self)), 'nand': lambda self, other, /: ~(self&other), 'nor': lambda self, other, /: ~(self|other), 'xnor': g, 'abjunction': lambda self, other, /: ~self.implies(other), 'converse_implies': lambda self, other, /: self|~other, 'converse_abjunction': lambda self, other, /: other&~self, '__bool__': lambda self: self.value == 1, '__pos__': lambda self: self, 'normalized': _normalized_cache(lambda self: Fraction(self.value)), 'from_normalized': classmethod(lambda cls, val: cls(val)), 'from_logic_member': classmethod(lambda cls, member: cls.from_normalized(member.normalized())), 'convert_to': lambda self, cls: cls.from_normalized(self.normalized())}
        return r
class _InfLogicMetaBase(_AllLogicMeta):
    @property
    def T(cls): return cls.from_normalized(Fraction(1))
    @property
    def F(cls): return cls.from_normalized(Fraction())
    verum, falsum = T, F
    @classmethod
    def _ret_new_and_value(mcls): raise NotImplementedError
    @classmethod
    def __default_factory__(mcls): return _AllLogicMeta.__default_factory__()|{'members': {}, '__repr__': _repr_cache(lambda self: f'{type(self).__name__}({self.value})')}|mcls._ret_new_and_value()
class _DecimalLogicMeta(_InfLogicMetaBase):
    @classmethod
    def _ret_new_and_value(mcls):
        _ = WeakKeyDictionary()
        def __new__(cls, val='0', /, _=_):
            if (v := (c := cls.members).get(d := Decimal(val), None)) is None: c[d] = v = object.__new__(cls); _[v] = d
            return v
        return {'__new__': __new__, 'value': property(_.__getitem__)}
class _RationalLogicMeta(_InfLogicMetaBase):
    @classmethod
    def _ret_new_and_value(mcls):
        _ = WeakKeyDictionary()
        def __new__(cls, /, *a, _=_):
            if (v := (c := cls.members).get(f := Fraction(*a), None)) is None: c[f] = v = object.__new__(cls); _[v] = f
            return v
        return {'__new__': __new__, 'value': property(_.__getitem__)}
class _SlowEnumLogicMeta(_AllLogicMeta):
    class MemberContainer:
        __cache, __cache2, _NOT_GENERATED = WeakKeyDictionary(), WeakKeyDictionary(), type('NotGenerated', (), {'__new__': _singleton_new, '__repr__': lambda _, /: '<not generated>'})()
        def __init__(self, values): self.__values, self.value_from_name, self.name_from_value, self.names = dict.fromkeys(values.values(), self._NOT_GENERATED), values.__getitem__, {v: k for k, v in values.items()}.__getitem__, tuple(values)
        def generate(self, value):
            if (x := self.__values[value]) is self._NOT_GENERATED: self.__values[value] = x = object.__new__(self.typ); self.__cache[x], self.__cache2[x] = value, self.name_from_value(value)
            return x
        def from_name(self, name):
            if (x := self.__values[v := self.value_from_name(name)]) is self._NOT_GENERATED: self.__values[v] = x = object.__new__(self.typ); self.__cache[x], self.__cache2[x] = v, name
            return x
        def member_values(self): yield from self.__values
        def __set_name__(self, owner, name, /):
            if name != 'members': raise AttributeError(f"MemberContainer must be assigned to an attribute named 'members', not {name!r}")
            self.typ = owner
        @_repr_cache
        def __repr__(self): return f'({", ".join(str(self.generate(i)) for i in self.__values)})'
        def __iter__(self): yield from map(self.generate, self.__values)
    def __getattr__(cls, name, /):
        if name in cls.members.names: super().__setattr__(name, r := cls(name)); return r
        raise AttributeError(f'class {cls.__name__} has no attribute {name!r}')
    def __setattr__(cls, name, value, /):
        if name in cls.members.names: raise TypeError(f'attribute {name!r} is read-only')
        super().__setattr__(name, value)
    def __new__(mcls, name, bases, namespace, /, **k):
        if FORBIDDEN.intersection(namespace): raise TypeError('attempted to override forbidden attributes')
        c = mcls.MemberContainer(namespace['members']); return super().__new__(mcls, name, bases, {'__repr__': _repr_cache(lambda self: f'{type(self).__name__}.{self.name}'), 'value': property(c._MemberContainer__cache.__getitem__), 'name': property(c._MemberContainer__cache2.__getitem__), '__neg__': namespace['__invert__']}|namespace|{'members': c, '__new__': lambda cls, v, /: c.from_name(v) if isinstance(v, str) else c.generate(v)}, **k) # noqa: ARG005
class _FastEnumLogicMeta(_SlowEnumLogicMeta):
    class MemberContainer(_SlowEnumLogicMeta.MemberContainer):
        @_repr_cache
        def __repr__(self): return f'({(n := self.typ.__name__)}.{f", {n}.".join(self.names)})'
class _FakeProtocolMeta(type):
    _cache, _meta_map, _requirement_map, _prefix_map, _mcont_allowed = [None]*12, (_AllLogicMeta, _AllLogicMeta, _SlowEnumLogicMeta, _InfLogicMetaBase, _DecimalLogicMeta, _RationalLogicMeta, _SlowEnumLogicMeta, _FastEnumLogicMeta, _FastEnumLogicMeta, _FastEnumLogicMeta, _DecimalLogicMeta, _RationalLogicMeta), tuple(map(frozenset, ((), ('values',), ('members', 'values'), (), (), (), ('gullibility', 'consensus'), (), ('strong_disjunction', 'strong_conjunction', 'diamond', 'box', 'doubtful'), (), ('strong_conjunction',), ('strong_conjunction',)))), ('', '', '', '', '', '', '', 'G', 'L', 'P', '', ''), frozenset((2, 6, 7, 8, 9))
    def __new__(mcls, name, bases=(), namespace=None, /, **k):
        try: r = (c := mcls._cache)[i := FAKE_PROTOCOLS_TUPLE.index(name)]
        except ValueError: raise TypeError(f'cannot create protocol class with name {name!r}') from None
        def __init_subclass__(_, /): raise TypeError(f'cannot inherit from protocol class {name!r}')
        def __new__(*_): raise TypeError(f'cannot create instance of protocol {name!r}')
        if namespace is None: namespace = {}
        namespace['__init_subclass__'], namespace['__new__'] = __init_subclass__, __new__
        if r is None: c[i] = r = super().__new__(mcls, name, bases, namespace, **k); r._idx, r._meth_cache = i, {}
        return r
    def __getattr__(cls, name, /):
        if name == 'MemberContainer' and cls._idx in cls._mcont_allowed:
            class MemberContainer(_FastEnumLogicMeta.MemberContainer):
                def __new__(cls, values): raise TypeError(f'cannot instantiate MemberContainer with values {values!r}')
                def __init_subclass__(cls): raise TypeError('cannot subclass MemberContainer')
            cls.MemberContainer = MemberContainer; return MemberContainer
        if name in ALL_METHODS:
            if (r := (c := cls._meth_cache).get(name)) is None: exec('@property\n'*(name == 'value')+f'def {name}(*_): raise NotImplementedError("method {name!r} of protocol {cls.__name__!r} is abstract")', locals=c); r = c[name] # noqa: S102
            return r
        raise AttributeError(f'class {cls.__name__!r} has no attribute {name!r}')
    def __init_subclass__(mcls, /, **_): raise TypeError('cannot subclass _FakeProtocolMeta')
    def __instancecheck__(cls, instance): return cls.__subclasscheck__(type(instance))
    def __subclasscheck__(cls, sub): return isinstance(sub, cls._meta_map[i := cls._idx]) and sub.__name__.startswith(cls._prefix_map[i]) and (cls._requirement_map[i]|MIXIN_METHODS).issubset(sub.__dict__)