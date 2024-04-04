# Laboratory 4: Regular Expretions

### Course: Formal Languages & Finite Automata
### Author: Musin Vladislava

----


## Objectives:


## Theory

A regular expression (regex or regexp) is a sequence of characters that define a search pattern, usually used for string matching within text or data. Regular expressions provide a powerful and flexible way to search, manipulate, and validate text based on patterns.

Here are some common use cases for regular expressions:

Pattern Matching: Regular expressions can be used to search for specific patterns within a string. For example, searching for all email addresses in a text document or finding all occurrences of a certain word.

Validation: Regular expressions are commonly used to validate input data. For instance, ensuring that an input string matches a certain format, such as a valid email address or a phone number.

Text Manipulation: Regular expressions can be used to manipulate text by performing search and replace operations. For example, replacing all occurrences of a word with another word or removing certain characters from a string.

Lexical Analysis: Regular expressions are often used in lexical analysis, such as in lexers for programming languages, to tokenize input text into meaningful tokens.

Regular expressions consist of normal characters, which match themselves, and special characters called metacharacters, which represent classes of characters or operations. Some common metacharacters include:

. (dot): Matches any single character except newline.
*: Matches zero or more occurrences of the preceding character.
+: Matches one or more occurrences of the preceding character.
?: Matches zero or one occurrence of the preceding character.
[]: Matches any one of the characters within the brackets.
|: Alternation, matches either the expression before or after the pipe symbol.
For example, the regular expression \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b matches valid email addresses.

Regular expressions are supported in many programming languages and text processing tools, such as Python, JavaScript, Perl, Java, and Unix utilities like grep and sed. They provide a concise and powerful mechanism for handling textual data. However, they can also be complex and difficult to read and write, especially for complex patterns.


## Implementation Details
My Python script generates random strings based on predefined regular expressions and then provides a sequence of processing steps to explain how each regular expression pattern is interpreted.

Let's break down the code:

1. Regular Expression Patterns and String Generation Functions:

Three regular expression patterns (regex_1, regex_2, regex_3) are defined.
Three functions (generate_string_from_regex_1, generate_string_from_regex_2, generate_string_from_regex_3) are defined to generate random strings based on these regular expressions. 
2. show_processing_sequence Function:

This function takes a regular expression pattern as input and returns a sequence of processing steps to explain how the regex pattern is interpreted.
It iterates through each character of the regex pattern and identifies special characters or character sequences.
It generates explanations for each identified pattern or character sequence.
3. Main Execution:

The script generates random strings for each regex pattern using the corresponding string generation functions.
For each generated string, it prints the string and then generates and prints the processing sequence using the show_processing_sequence function.
4. Explanation Printing:

It prints the generated string matching the regex pattern.
It prints the sequence of processing steps explaining how the regex pattern is interpreted.
5. Character Classes and Quantifiers:

The regular expressions contain character classes (e.g., [ST], [UV]) and quantifiers (e.g., *, +, {2}) which define the rules for matching characters in the generated strings.
The random string generation functions use random.choice and random.randint functions to create strings that adhere to these regex patterns.
6. Explanation of Processing Steps:

The processing steps explain the interpretation of each component of the regular expression pattern, including character matches, character classes, quantifiers, and groupings.

### Conclusion:
While working on this laboratory work I have deepened my knowledge about regular expresions, by writing a script that generates strings according to a regex and outputs the steps that must beb taken in order to achieve that 