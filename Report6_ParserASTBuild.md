# Topic: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: Musin Vladislava

----

## Overview
&ensp;&ensp;&ensp; The process of gathering syntactical meaning or doing a syntactical analysis over some text can also be called parsing. It usually results in a parse tree which can also contain semantic information that could be used in subsequent stages of compilation, for example.

&ensp;&ensp;&ensp; Similarly to a parse tree, in order to represent the structure of an input text one could create an Abstract Syntax Tree (AST). This is a data structure that is organized hierarchically in abstraction layers that represent the constructs or entities that form up the initial text. These can come in handy also in the analysis of programs or some processes involved in compilation.


## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens.
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description
### Classes:
#### TokenType (Enum):
This class defines an enumeration for different token types used in the lexer. It includes INTEGER, PLUS, MINUS, and EOF (End Of File) tokens.

#### Token:
This class represents a token in the input text. It contains information about the token type and its corresponding value.

#### Lexer:
The Lexer class takes an input text and tokenizes it, breaking it down into tokens. It uses regular expressions to match token patterns defined by the TokenType enum.

#### AST (Abstract Syntax Tree):
This is a base class for representing abstract syntax trees. It doesn't have specific functionality but serves as a base for other AST nodes.

#### BinOp:
This class represents binary operations in the abstract syntax tree. It consists of a left operand, an operator, and a right operand.

#### Num:
This class represents numeric literals in the abstract syntax tree. It holds the value of the numeric token.

#### Parser:
The Parser class takes tokens produced by the lexer and builds an abstract syntax tree (AST) representing the structure of the input expression. It defines methods for parsing different components of the input text, such as terms and expressions.

This parser accepts a very simple arithmetic language with the following syntax:

* Integers: The language supports integer literals, such as 0, 123, -45, etc.
* Operators: The language supports addition (+) and subtraction (-) operators.
* Expressions: Expressions in this language are composed of integer literals and arithmetic operators. They can be simple (e.g., 5, -10, etc.) or complex (e.g., 3 + 4 - 2, 10 - 5 + 2, etc.).
* Whitespace: The parser ignores whitespace characters in the input text.


Here are some examples of valid expressions in this language:

* 5
* 10 - 3
* 2 + 7 - 4
* -8 + 15
* 100

Invalid expressions would include anything that doesn't adhere to this syntax, like 5 * 2 (multiplication is not supported, as well as division), 1 + (missing operand), or 3 + - (missing second operand).

## Results
 The input "7 + 10 - 5" generates the following output in the cmd:
Tokens:
Token(INTEGER, 7)
Token(PLUS, '+')
Token(INTEGER, 10)
Token(MINUS, '-')
Token(INTEGER, 5)
Token(EOF, '')
Token(EOF, None)

AST:
BinOp:
  Left:
    BinOp:
      Left:
        Num: 7
      Op: +
      Right:
        Num: 10
  Op: -
  Right:
    Num: 5
