from re import findall
from runtime.tokenizer.types import Token, TokenType

def make_token(match: tuple[str]) -> Token:
    match match:
        case [value, '', '', '']:
            return Token(type=TokenType.IDENTIFIER, value=value)
        case ['', value, '', '']:
            return Token(type=TokenType.NUMERIC_LITERAL, value=value)
        case ['', '', value, '']:
            return Token(type=TokenType.STRING_LITERAL, value=value)
        case ['', '', '', value]:
            return Token(type=TokenType.OPERATOR, value=value)

def tokenize(src: str) -> list[Token]:
    pattern: str = r'([a-zA-Z_][a-zA-Z0-9_]*)|(\d+(?:\.\d+)?)|(\'.*\')|([|])'
    matches: list[tuple[str]] = findall(pattern=pattern, string=src)
    return [make_token(match=match) for match in matches]