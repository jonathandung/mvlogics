# Creating your own logic

This module does not technically offer a public interface to create custom logic classes. The protocols in the `protocols` submodule are not for subclassing, and will not provide the mixin methods for you. The resulting subclasses will not even be recognized as logic classes by the indicator functions provided by this module.

If you find an omission in the implementations of this library for a somewhat useful logic type, you are encouraged to open an issue using the logic
request template. To acknowledge your contributions, your name will be included in the docstring of the new class; you can opt out if you want.

However, if you do not want to do so for any reason, follow the template below:

```python
from fractions import Fraction
from mvlogics.base import _FastEnumLogicMeta # the metaclass
class MyLogic(metaclass=_FastEnumLogicMeta):
    members = {'member_name_0': 0, 'member_name_1': 1, 'member_name_2': 2} # Required; dictionary mapping truth value names to values
    # values do not have to be integers
    # By default, only the member with truth value 1 (if any) will evaluate to True in a boolean context.
    # You can override this in the __bool__ method:
    def __bool__(self): return self.value == 2
    # below are required
    def __and__(self, other, /): return (self.value, other.value) == (1, 2)
    def __or__(self, other, /): return {self.value, other.value} == {1, 2}
    def __invert__(self): return type(self)((self.value+1)%3)
    # no need to define __init_subclass__ since all logic classes must be unsubclassable
    # below are optional
    def normalized(self): return Fraction((3, 1, 0.5)[self.value])
    # return a fractions.Fraction
    @classmethod
    def from_normalized(cls, val, /):
        # val is an instance of `fractions.Fraction` taking its value between 0 and 1 inclusive
        return cls(min(max(int(1/val), 0), 2))
    def __reduce__(self): return type(self), (self.value,) # if you want pickling support
    # other methods; see OPERATOR_REFERENCE.md
```

and in the corresponding stub file:

```python
from fractions import Fraction
from typing import Self
from mvlogics.protocols import LogicBase
class MyLogic(LogicBase[int]):
    def __and__(self, other: Self, /) -> Self: ...
    def __or__(self, other: Self, /) -> Self: ...
    def __invert__(self) -> Self: ...
    def __bool__(self) -> bool: ...
    def normalized(self) -> Fraction: ...
    @classmethod
    def from_normalized(cls, val: int, /) -> Self: ...
    def __reduce__(self) -> tuple[type[Self], tuple[int]]: ...
```

For help in typing or implementing the logic, let us know in the discussions page; we will be happy to help.

Note:

- The private API of this library may change between minor versions, so be sure to keep yourself updated whenever bumping dependencies.
- The convention of this project is to include docstrings in .pyi files only, and you are encouraged to do so too.
- This is considered bad practice, and we are not accountable for unexpected behaviour in the resultant class if your implementation can be proved to
be faulty.
