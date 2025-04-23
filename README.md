# A Simple Compiler

This is a prototype of a simple compiler. The objective of this project is practice
the concepts of compilers. 

This project are made with Python and a library for regular expressions.

### Arquives
list_tok.txt  -> contains the output from lexical analyzer.

teste.txt     -> contains a source code to tests.

lex.py   -> contains the lexical analyzer.


## Specifications

### Lexical Analyzer
The first step of the compiler. Here we need to recognize the tokens and guarantee that each word of 
source code are defined at the aim language. In this project, when an error are find, the lexical analizer don't 
crash, it's continue with the intention to assess whether there are more erros.
As a basic compiler, follow a table with restrict symbols we're accept:

| Symbol | Token |
|--------|-------|
|NUM|NUM|
|ID|ID|
|+|PLUS|
|-|MINUS|
|*|MULT|
|/|DIV|
|>|GT|
|<|LT|
|>=|GE|
|<=|LE|
|==|EQUAL|
|=|ASSIGN|
|!=|NEQ|
|(|LBRACE|
|)|RBRACE|
|{|LBRACKET|
|}|RBRACKET|
|;|SEMI|
|,|COMMA|
|.|POINT|
