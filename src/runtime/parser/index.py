from dataclasses import dataclass, field
from typing import Sequence

@dataclass(slots=True)
class Index[T]:
    sequence: Sequence[T]
    __index: int = field(default=0, init=False)

    def __current__(self) -> T:
        return self.sequence[self.__index]
    
    def __next__(self) -> T:
        item: T = self.sequence[self.__index]
        self.__index += 1
        return item

def current[T](index: Index[T]) -> T:
    return index.__current__()