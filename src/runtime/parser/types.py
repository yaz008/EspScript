from dataclasses import dataclass, field
from enum import IntEnum
from abc import ABC
from runtime.tokenizer import Token

class NodeType(IntEnum):
    PROGRAM: int = 0
    BINARY_EXPR: int = 1
    CALL_EXPR: int = 2

@dataclass(slots=True)
class Node(ABC):
    type: NodeType = field(init=False)

class Expr(Node):
    def __init__(self):
        raise NotImplementedError

@dataclass(slots=True)
class BinaryExpr(Expr):
    left: Expr
    right: Expr
    operator: Token

    def __post_init__(self):
        self.type = NodeType.BINARY_EXPR

@dataclass(slots=True)
class CallExpr(Expr):
    caller: Token
    args: list[Token]

    def __post_init__(self):
        self.type = NodeType.CALL_EXPR

@dataclass(slots=True)
class Program(Node):
    root: Expr

    def __post_init__(self):
        self.type = NodeType.PROGRAM