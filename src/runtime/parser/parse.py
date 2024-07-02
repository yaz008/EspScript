from runtime.parser.index import Index, current
from runtime.tokenizer import Token, TokenType
from runtime.parser.types import Program, Expr, BinaryExpr, CallExpr

def parse_call_expr(token: Index[Token]) -> CallExpr:
    if current(token).type == TokenType.IDENTIFIER:
        caller: Token = next(token)
    args: list[Token] = []
    while current(token).type in (TokenType.IDENTIFIER,
                                  TokenType.NUMERIC_LITERAL,
                                  TokenType.STRING_LITERAL):
        args.append(next(token))
    return CallExpr(caller, args)

def parse_pipe_expr(token: Index[Token]) -> CallExpr | BinaryExpr:
    left: Expr = parse_call_expr(token)
    while current(token).type == TokenType.OPERATOR:
        operator: Token = next(token)
        right: CallExpr = parse_call_expr(token)
        left: BinaryExpr = BinaryExpr(left, right, operator)
    return left

def parse(tokens: list[Token]) -> Program:
    token: Index[Token] = Index(tokens)
    expr: Expr = parse_pipe_expr(token)
    return Program(root=expr)