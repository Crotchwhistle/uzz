from enum import Enum
from typing import Any

class TokenType(Enum):
    # special tokens
    EOFUZZ = 'EOFUZZ' # eof = end of file
    ILLEGUZZ = 'ILLEGUZZ' # illegal

    # data types
    IDENTUZZ = 'IDENTUZZ' # identifier
    INTUZZ = 'INTUZZ' # integer
    FLOATUZZ = 'FLOATUZZ' # float

    # arithmetic symbols
    PLUZZ = 'PLUZZ' # plus, addition
    MINUZZ = 'MINUZZ' # minus, subtraction
    ASTERUZZ = 'ASTERUZZ' # asterisk, multiplication
    SLUZZ = 'SLUZZ' # slash, division
    POWUZZ = 'POWUZZ' # power, exponentiation
    MODULUZZ = 'MODULUZZ' # modulo, remainder, percent

    # assignment
    EQUZZ = 'EQUZZ' # equals, assignment

    # comparison
    LTUZZ = '<'
    GTUZZ = '>'
    EQUZZ_EQUZZ = '=='
    NEQUZZ = '!='
    LT_EQUZZ = '<='
    GT_EQUZZ = '>='
    
    # symbols
    COLUZZ = 'COLUZZ' # colon, signifies type"
    COMMUZZ = 'COMMUZZ' # comma, separates arguments
    SEMICOLUZZ = 'SEMICOLUZZ' # semicolon, end of line/statement
    ARRUZZ = 'ARRUZZ' # arrow, function return type
    LPARUZZ = 'LPARUZZ' # left parenthesis
    RPARUZZ = 'RPARUZZ' # right parenthesis
    LBRACUZZ = 'LBRACUZZ' # left brace
    RBRACUZZ = 'RBRACUZZ' # right brace

    # keywords
    LETUZZ = 'LETUZZ' # let keyword
    FNUZZ = 'FNUZZ' # function keyword
    RETURNUZZ = 'RETURNUZZ' # return keyword
    IFUZZ = 'IFUZZ' # if keyword
    ELSUZZ = 'ELSUZZ' # else keyword
    TRUZZ = 'TRUZZ' # true keyword
    FALUZZ = 'FALUZZ' # false keyword

    # typing
    TYPUZZ = 'TYPUZZ' 

class Token:
    def __init__(self, type: TokenType, literal: Any, line_no: int, position: int) -> None:
        self.type = type
        self.literal = literal
        self.line_no = line_no
        self.position = position

    def __str__(self) -> str:
        return f"Token[{self.type} : {self.literal} : Line {self.line_no} : Position {self.position}]"

    def __repr__(self) -> str:
        return str(self)
    
KEYWORDS: dict[str, TokenType] = {
    "let": TokenType.LETUZZ,
    "fn": TokenType.FNUZZ,
    "return": TokenType.RETURNUZZ,
    "if": TokenType.IFUZZ,
    "else": TokenType.ELSUZZ,
    "true": TokenType.TRUZZ,
    "false": TokenType.FALUZZ
}

ALT_KEYWORDS: dict[str, TokenType] = {
    "ts": TokenType.LETUZZ,
    "so": TokenType.EQUZZ,
    "ahh": TokenType.SEMICOLUZZ,
    "bruzz": TokenType.FNUZZ,
    "huzz": TokenType.RETURNUZZ,
    "jugg": TokenType.ARRUZZ,
    "nettspend": TokenType.IFUZZ,
    "osamason": TokenType.ELSUZZ,
    "slime": TokenType.TRUZZ,
    "opp": TokenType.FALUZZ 
}

TYPE_KEYWORDS: list[str] = ['int', 'float']

def lookup_ident(ident: str) -> TokenType:
    tt: TokenType | None = KEYWORDS.get(ident)
    if tt is not None:
        return tt
    
    tt: TokenType | None = ALT_KEYWORDS.get(ident)
    if tt is not None:
        return tt
    
    if ident in TYPE_KEYWORDS:
        return TokenType.TYPUZZ
    
    return TokenType.IDENTUZZ