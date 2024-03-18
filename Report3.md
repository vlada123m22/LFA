# Laboratory 1: Lexer

### Course: Formal Languages & Finite Automata
### Author: Musin Vladislava

----


## Objectives:
1. Understand what lexical analysis [1] is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Implementation Description

#### Token Class:
This class represents a token. Each token has a type and a value associated with it.

#### KEYWORDS, OPERATOR, and SEPARATOR Dictionaries:
These dictionaries map specific strings (like keywords, operators, and separators) to their corresponding token types and values.

#### Lexer Class:
This class is responsible for tokenizing the input source code.
1. The constructor __init__ initializes the lexer with the input source code and sets the index to 0.
2. The methods is_alpha, is_digit, and is_alphanumeric are helper methods to check if a character is an alphabet, digit, or alphanumeric character respectively.
3. The method next_token is the core of the lexer. It scans through the input character by character and returns the next token it encounters. It handles integers, identifiers, keywords, operators, and separators.
4. The method tokenize repeatedly calls next_token until it reaches the end of the input, collecting all tokens in a list and returning them.

#### Input Strings:
Four input strings input1, input2, input3, and input4 are provided to demonstrate tokenization.

#### Tokenization:
1. The lexer is instantiated with one of the input strings.
2. The tokenize method is called to tokenize the input string.
3. The resulting tokens are then printed out, showing their types and values.

#### Printing Tokens:
After tokenization, the script prints out each token's type and value.

## Results:
#### A sequence from the output message:
```
BEGGINING OF ELSE BLOCK:  else
RETURN STATEMENT:  return
MINUS -
INTEGER 1
R_CURLY }
```

## Conclusion:
By implementing a lexer in this laboratory work, I have deepened my understanding of lexers and language compilers