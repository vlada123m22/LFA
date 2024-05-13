from enum import Enum
import re


# Define token types using Enum
class TokenType(Enum):
    INTEGER = 'INTEGER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    EOF = 'EOF'


# Token class using TokenType enum
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type.name}, {repr(self.value)})'


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.tokens = []

    def error(self):
        raise Exception('Invalid character')

    def tokenize(self):
        # Regular expressions for tokens
        token_specification = [
            (TokenType.INTEGER, r'\d+'),
            (TokenType.PLUS, r'\+'),
            (TokenType.MINUS, r'\-'),
            (TokenType.EOF, r'\Z')
        ]

        # Create a regex that matches the token specifications
        token_regex = '|'.join(f'(?P<{tok.name}>{pattern})' for tok, pattern in token_specification)
        for mo in re.finditer(token_regex, self.text):
            kind = mo.lastgroup
            value = mo.group()
            tok_type = TokenType[kind]
            if tok_type == TokenType.INTEGER:
                value = int(value)  # Convert to integer
            self.tokens.append(Token(tok_type, value))

        self.tokens.append(Token(TokenType.EOF, None))


class AST:
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


def print_ast(node, level=0):
    indent = '  ' * level
    if isinstance(node, BinOp):
        print(f'{indent}BinOp:')
        print(f'{indent}  Left:')
        print_ast(node.left, level + 2)
        print(f'{indent}  Op: {node.op.value}')
        print(f'{indent}  Right:')
        print_ast(node.right, level + 2)
    elif isinstance(node, Num):
        print(f'{indent}Num: {node.value}')


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokens
        self.current_token = None
        self.pos = -1
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token(TokenType.EOF, None)

    def error(self):
        raise Exception('Invalid syntax')

    def parse(self):
        if self.current_token.type == TokenType.EOF:
            return None

        left = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token
            self.advance()
            right = self.term()
            left = BinOp(left=left, op=op, right=right)
        return left

    def term(self):
        token = self.current_token
        if token.type == TokenType.INTEGER:
            self.advance()
            return Num(token)
        else:
            self.error()


#Main program
text = "7 + 10 - 5"
lexer = Lexer(text)
lexer.tokenize()
parser = Parser(lexer)
ast = parser.parse()

print("Tokens:")
for token in lexer.tokens:
    print(token)

print("\nAST:")
print_ast(ast)