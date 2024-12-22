from Lexer import Lexer
from Token import Token, TokenType
from typing import Callable
from enum import Enum, auto

from AST import Statement, Expression, Program
from AST import ExpressionStatement, LetStatement
from AST import InfixExpression
from AST import IntegerLiteral, FloatLiteral, IdentifierLiteral


# precedence types
class PrecedenceType(Enum):
    P_LOWEST = 0
    P_EQUALS = auto()
    P_LESSGREATER = auto()
    P_SUM = auto()
    P_PRODUCT = auto()
    P_EXPONENT = auto()
    P_PREFIX = auto()
    P_CALL = auto()
    P_INDEX = auto()

# precedence map
PRECEDENCES: dict[TokenType, PrecedenceType] = {
    TokenType.PLUZZ: PrecedenceType.P_SUM,
    TokenType.MINUZZ: PrecedenceType.P_SUM,
    TokenType.SLUZZ: PrecedenceType.P_PRODUCT,
    TokenType.ASTERUZZ: PrecedenceType.P_PRODUCT,
    TokenType.MODULUZZ: PrecedenceType.P_PRODUCT,
    TokenType.POWUZZ: PrecedenceType.P_EXPONENT
}

class Parser:
    def __init__(self, lexer: Lexer) -> None:
        self.lexer: Lexer = lexer

        self.errors: list[str] = []

        self.current_token: Token = None
        self.peek_token: Token = None

        self.prefix_parse_fns: dict[TokenType, Callable] = {
            TokenType.INTUZZ: self.__parse_int_literal,
            TokenType.FLOATUZZ: self.__parse_float_literal,
            TokenType.LPARUZZ: self.__parse_grouped_expression,
        }
        self.infix_parse_fns: dict[TokenType, Callable] = {
            TokenType.PLUZZ: self.__parse_infix_expression,
            TokenType.MINUZZ: self.__parse_infix_expression,
            TokenType.SLUZZ: self.__parse_infix_expression,
            TokenType.ASTERUZZ: self.__parse_infix_expression,
            TokenType.POWUZZ: self.__parse_infix_expression,
            TokenType.MODULUZZ: self.__parse_infix_expression,
        } 

        self.__next_token()
        self.__next_token()

    # region parser helpers
    def __next_token(self) -> None:
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def __current_token_is(self, tt: TokenType) -> bool:
        return self.current_token.type == tt

    def __peek_token_is(self, tt: TokenType) -> bool:
        return self.peek_token.type == tt
    
    def __expect_peek(self, tt: TokenType) -> bool:
        if self.__peek_token_is(tt):
            self.__next_token()
            return True
        else:
            self.__peek_error(tt)
            return False
        
    def __current_precedence(self) -> PrecedenceType:
        prec: int | None = PRECEDENCES.get(self.current_token.type)
        if prec is None:
            return PrecedenceType.P_LOWEST
        return prec
    
    def __peek_precedence(self) -> PrecedenceType:
        prec: int | None = PRECEDENCES.get(self.peek_token.type)
        if prec is None:
            return PrecedenceType.P_LOWEST
        return prec
        
    def __peek_error(self, tt: TokenType) -> None:
        self.errors.append(f"Expectuzz next tokuzz to be {tt}, but got {self.peek_token.type} instead.")

    def __no_prefix_parse_fn_error(self, tt: TokenType) -> None:
        self.errors.append(f"No prefuzz parse function for {tt} found.")
    # endregion Parser

    def parse_program(self) -> None:
        program: Program = Program()

        while self.current_token.type != TokenType.EOFUZZ:
            stmt: Statement = self.__parse_statement()
            if stmt is not None:
                program.statements.append(stmt)

            self.__next_token()

        return program
    
    # region statement methods
    def __parse_statement(self) -> Statement:
        match self.current_token.type:
            case TokenType.LETUZZ:
                return self.__parse_let_statement()
            case _:
                return self.__parse_expression_statement()
    
    def __parse_expression_statement(self) -> ExpressionStatement:
        expr = self.__parse_expression(PrecedenceType.P_LOWEST)

        if self.__peek_token_is(TokenType.SEMICOLUZZ):
            self.__next_token()

        stmt: ExpressionStatement = ExpressionStatement(expr)

        return stmt
    
    def __parse_let_statement(self) -> LetStatement:
        # let a: int = 10;
        stmt: LetStatement = LetStatement()

        if not self.__expect_peek(TokenType.IDENTUZZ):
            return None
        
        stmt.name = IdentifierLiteral(value=self.current_token.literal)

        if not self.__expect_peek(TokenType.COLUZZ):
            return None
        
        if not self.__expect_peek(TokenType.TYPUZZ):
            return None
        
        stmt.value_type = self.current_token.literal

        if not self.__expect_peek(TokenType.EQUZZ):
            return None
        
        self.__next_token()

        stmt.value = self.__parse_expression(PrecedenceType.P_LOWEST)

        while not self.__current_token_is(TokenType.SEMICOLUZZ) and not self.__current_token_is(TokenType.EOFUZZ):
            self.__next_token()

        return stmt
    # endregion

    # region expression methods
    def __parse_expression(self, precedence: PrecedenceType) -> Expression:
        prefix_fn: Callable | None = self.prefix_parse_fns.get(self.current_token.type)
        if prefix_fn is None:
            self.__no_prefix_parse_fn_error(self.current_token.type)
            return None
        
        left_expr: Expression = prefix_fn()
        while not self.__peek_token_is(TokenType.SEMICOLUZZ) and precedence.value < self.__peek_precedence().value:
            infix_fn: Callable | None = self.infix_parse_fns.get(self.peek_token.type)
            if infix_fn is None:
                return left_expr
            
            self.__next_token()

            left_expr = infix_fn(left_expr)

        return left_expr

    def __parse_infix_expression(self, left_node: Expression) -> Expression:
        infix_expr: InfixExpression = InfixExpression(left_node=left_node, operator=self.current_token.literal)

        precedence = self.__current_precedence()

        self.__next_token()

        infix_expr.right_node = self.__parse_expression(precedence)

        return infix_expr
    
    def __parse_grouped_expression(self) -> Expression:
        self.__next_token()

        expr: Expression = self.__parse_expression(PrecedenceType.P_LOWEST)

        if not self.__expect_peek(TokenType.RPARUZZ):
            return None
        
        return expr
    # endregion

    # region prefix methods
    def __parse_int_literal(self) -> Expression:
        """Parses an IntuzzLiteral Noduzz from the current tokuzz."""
        int_lit: IntegerLiteral = IntegerLiteral()

        try:
            int_lit.value = int(self.current_token.literal)
        except:
            self.errors.append(f"Could not parse {self.current_token.literal} as intuzz.")
            return None
        
        return int_lit
    
    def __parse_float_literal(self) -> Expression:
        """Parses a FloatuzzLiteral Noduzz from the current tokuzz."""
        float_lit: FloatLiteral = FloatLiteral()

        try:
            float_lit.value = float(self.current_token.literal)
        except:
            self.errors.append(f"Could not parse {self.current_token.literal} as floatuzz.")
            return None
        
        return float_lit
    # endregion