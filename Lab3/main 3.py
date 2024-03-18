import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

KEYWORDS = {
    'if': 'IF',
    'else': 'ELSE',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'let': 'LET',
    'true': 'TRUE',
    'false': 'FALSE'
}

OPERATOR = {
    'plus': '+',
    'minus': '-',
    'mult': '*',
    'div': '/',
    'mod': '%',
    'less': '<',
    'greater': '>',
    'equal': '==',
    'assign': '='
}

SEPARATOR = {
    'l_paren': '(',
    'r_paren': ')',
    'l_curly': '{',
    'r_curly': '}',
    'l_square': '[',
    'r_square': ']',
    'semicolon': ';',
    'comma': ','
}

class Lexer:
    def __init__(self, input):
        self.input = input
        self.index = 0

    def is_alpha(self, char):
        return re.match(r'[a-zA-Z_]', char)

    def is_digit(self, char):
        return re.match(r'\d', char)

    def is_alphanumeric(self, char):
        return self.is_alpha(char) or self.is_digit(char)

    def next_token(self):
        while self.index < len(self.input):
            current_char = self.input[self.index]

            if re.match(r'\s', current_char):
                self.index += 1
                continue

            if self.is_digit(current_char):
                num = ""
                while self.index < len(self.input) and self.is_digit(self.input[self.index]):
                    num += self.input[self.index]
                    self.index += 1
                return Token("INTEGER", num)

            if self.is_alpha(current_char):
                ident = ""
                while self.index < len(self.input) and self.is_alphanumeric(self.input[self.index]):
                    ident += self.input[self.index]
                    self.index += 1
                if ident in KEYWORDS:
                    return Token(KEYWORDS[ident], ident)
                return Token("IDENTIFIER", ident)

            for type, value in {**OPERATOR, **SEPARATOR}.items():
                if current_char.startswith(value):
                    self.index += len(value)
                    return Token(type.upper(), value)

            raise Exception(f"Unknown token: {current_char}")

        return Token("EOF", "")

    def tokenize(self):
        tokens = []
        next_token = self.next_token()
        while next_token.type != "EOF":
            tokens.append(next_token)
            next_token = self.next_token()
        return tokens

input1 = "12 + 24 - 8"
input2 = "12 + (variableName - 34) * 56 / variable_2"
input3 = "if (x > 10) { function doSomething() { return x; } }"
input4 = """function addArray(arr, n) {
    let sum = 0;
    for(int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}"""
lexer = Lexer(input4)
tokens = lexer.tokenize()

for token in tokens:
    print(token.type, token.value)