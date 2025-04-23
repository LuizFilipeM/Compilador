import re
import sys

# Palavras-chave da linguagem
KEYWORDS = {
    'if': 'IF',
    'while': 'WHILE',
    'var': 'VAR',
    'main': 'MAIN',
    'return': 'RETURN',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    
}

# Definição dos tokens com expressões regulares
TOKEN_REGEX = [
    ('NUM', r'\d+'),
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),

    #Operadores aritméticos
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULT', r'\*'),
    ('DIV', r'/'),

    #Pontuacao
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACKET', r'\{'),
    ('RBRACKET', r'\}'),
    ('SEMI', r';'),
    ('ASSIGN', r'='),
    ('WHITESPACE',r'[ \t\n]+'),

    #Operadores relacioanais
    ('EQ', r'=='),
    ('LE', r'=='),
    ('LE', r'<='),
    ('GE', r'>='),
    ('LT', r'<'),
    ('GT', r'>'),
    ('NEQ', r'!=')
]

def get_line_col(code, pos):
    linha = code.count('\n', 0, pos) + 1
    ultima_quebra = code.rfind('\n', 0, pos)
    coluna = pos - ultima_quebra
    return linha, coluna

token_re = [(name, re.compile(pattern)) for name, pattern in TOKEN_REGEX]

def lexer(code):
    pos = 0
    tokens = []

    while pos < len(code):
        match = None
        for token_name, pattern in token_re:
            match = pattern.match(code, pos)
            if match:
                lexeme = match.group()
                if token_name == 'ID' and lexeme in KEYWORDS:
                    tokens.append((KEYWORDS[lexeme], lexeme))
                elif token_name != 'WHITESPACE':
                    tokens.append((token_name, lexeme))
                pos = match.end()
                break
        if not match:
            linha, coluna = get_line_col(code, pos)
            print(f"Caractere inesperado: '{code[pos]}' na linha {linha}, coluna {coluna}")
            pos = pos + 1
            continue

    return tokens


def main():
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        codigo = f.read()

    resultado = lexer(codigo)
    with open('list_tok.txt', 'w', encoding='utf-8') as lt:
        for token in resultado:
            lt.write(f"{token}\n")
    
main()