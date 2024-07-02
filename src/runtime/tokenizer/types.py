from dataclasses import dataclass
from enum import IntEnum

class TokenType(IntEnum):
    IDENTIFIER: int = 0
    NUMERIC_LITERAL: int = 1
    STRING_LITERAL: int = 2
    OPERATOR: int = 3

@dataclass(slots=True)
class Token:
    type: TokenType
    value: str