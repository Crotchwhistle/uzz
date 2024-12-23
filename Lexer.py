from Token import Token, TokenType, lookup_ident
from typing import Any

class Lexer:
    def __init__(self, source: str) -> None:
        self.source = source

        self.position: int = -1
        self.read_position: int = 0
        self.line_no: int = 1

        self.current_char: str | None = None

        self.__read_char()

    def __read_char(self) -> None:
        if self.read_position >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def __peek_char(self) -> str | None:
        """Peeks to the upcoming character without advancing the lexer position"""
        if self.read_position >= len(self.source):
            return None
        
        return self.source[self.read_position]

    def __skip_whitespace(self) -> None:
        while self.current_char in [' ', '\t', '\n', '\r']:
            if self.current_char == '\n':
                self.line_no += 1

            self.__read_char()
    
    def __new_token(self, tt: TokenType, literal: Any) -> Token:
        return Token(type=tt, literal=literal, line_no=self.line_no, position=self.position)
    
    def __is_digit(self, ch: str) -> bool:
        return '0' <= ch <= '9'
    
    def __is_letter(self, ch: str) -> bool:
        return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or ch == '_'
    
    def __read_number(self) -> Token:
        start_pos: int = self.position
        dot_count: int = 0

        output: str = ''
        while self.__is_digit(self.current_char) or self.current_char == '.':
            if self.current_char == '.':
                dot_count += 1

            if dot_count > 1:
                print(f"Too many decimuzz in numbuzz on line {self.line_no}, position {self.position}")
                return self.__new_token(TokenType.ILLEGUZZ, self.source[start_pos:self.position])

            output += self.source[self.position]
            self.__read_char()

            if self.current_char == None:
                break

        if dot_count == 0:
            return self.__new_token(TokenType.INTUZZ, int(output))
        else:
            return self.__new_token(TokenType.FLOATUZZ, float(output))

    def __read_identifier(self) -> str:
        position = self.position
        while self.current_char is not None and (self.__is_letter(self.current_char) or self.current_char.isalnum()):
            self.__read_char()

        return self.source[position:self.position]
    
    def next_token(self) -> Token:
        tok: Token = None

        self.__skip_whitespace()

        match self.current_char:
            case '+':
                tok = self.__new_token(TokenType.PLUZZ, self.current_char)
            case '-':
                # handle ->
                if self.__peek_char() == '>':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.ARRUZZ, ch + self.current_char)
                else:
                    tok = self.__new_token(TokenType.MINUZZ, self.current_char)
            case '*':
                tok = self.__new_token(TokenType.ASTERUZZ, self.current_char)
            case '/':
                tok = self.__new_token(TokenType.SLUZZ, self.current_char)
            case '^':
                tok = self.__new_token(TokenType.POWUZZ, self.current_char)
            case '%':
                tok = self.__new_token(TokenType.MODULUZZ, self.current_char)
            case '<':
                # handle <=
                if self.__peek_char() == '=':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.LT_EQUZZ, ch + self.current_char)
                else:
                    tok = self.__new_token(TokenType.LTUZZ, self.current_char)
            case '>':
                # handle >=
                if self.__peek_char() == '=':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.GT_EQUZZ, ch + self.current_char)
                else:
                    tok = self.__new_token(TokenType.GTUZZ, self.current_char)
            case '=':
                # handle ==
                if self.__peek_char() == '=':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.EQUZZ_EQUZZ, ch + self.current_char)
                else:
                    tok = self.__new_token(TokenType.EQUZZ, self.current_char)
            case '!':
                # handle !=
                if self.__peek_char() == '=':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.NEQUZZ, ch + self.current_char)
                else:
                    # TODO implement bang
                    tok = self.__new_token(TokenType.ILLEGUZZ, self.current_char)
            case ':':
                tok = self.__new_token(TokenType.COLUZZ, self.current_char)
            case ',':
                tok = self.__new_token(TokenType.COMMUZZ, self.current_char)
            case '(':
                tok = self.__new_token(TokenType.LPARUZZ, self.current_char)
            case ')':
                tok = self.__new_token(TokenType.RPARUZZ, self.current_char)
            case '{':
                tok = self.__new_token(TokenType.LBRACUZZ, self.current_char)
            case '}':
                tok = self.__new_token(TokenType.RBRACUZZ, self.current_char)
            case ';':
                tok = self.__new_token(TokenType.SEMICOLUZZ, self.current_char)
            case None:
                tok = self.__new_token(TokenType.EOFUZZ, '')
            case _:
                if self.__is_letter(self.current_char):
                    literal: str = self.__read_identifier()
                    tt: TokenType = lookup_ident(literal)
                    tok = self.__new_token(tt=tt, literal=literal)
                    return tok
                elif self.__is_digit(self.current_char):
                    tok = self.__read_number()
                    return tok
                else:
                    tok = self.__new_token(TokenType.ILLEGUZZ, self.current_char)
                    
        self.__read_char()
        return tok