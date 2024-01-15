from antlr4 import *
from Parser.c_srcLexer import c_srcLexer
import sys

TOKEN_NAMES = {
    1: '#include',
    2: '<',
    3: '>',
    4: '{',
    5: '}',
    6: ';',
    7: ',',
    8: '(',
    9: ')',
    10: '=',
    11: '[',
    12: ']',
    13: 'for',
    14: 'if',
    15: 'else',
    16: 'while',
    17: 'return',
    18: '!',
    19: '*',
    20: '/',
    21: '%',
    22: '+',
    23: '-',
    24: '==',
    25: '!=',
    26: '<=',
    27: '>=',
    28: 'struct',
    29: '.',
    30: 'void',
    31: 'string',
    32: 'int',
    33: 'char',
    34: 'double',
    35: 'scanf',
    36: '&',
    37: 'gets',
    38: 'atoi',
    39: 'printf',
    40: 'strlen',
    41: 'VAR',
    42: 'INT',
    43: 'DOUBLE',
    44: 'CHAR',
    45: 'STRING',
    46: 'LIB',
    47: 'Logical',
    48: 'Operator',
    49: 'LineComment',
    50: 'BlockComment',
    51: 'WS'
}





def print_tokens(input_file):
    lexer = c_srcLexer(FileStream(input_file))
    token_stream = CommonTokenStream(lexer)

    # 填充Token流
    token_stream.fill()

    # 获取Token列表
    all_tokens = token_stream.getTokens(start=0, stop=len(token_stream.tokens) - 1)

    # 打印Token信息
    for token in all_tokens:
        print(f"Token: {token.text}, Type: {TOKEN_NAMES[token.type]}, Line: {token.line}, Column: {token.column}")

if __name__ == "__main__":
    c_source_file_path = "test/quickSort.c"
    if len(sys.argv) >= 2:
        c_source_file_path = sys.argv[1]

    # 输出Token流列表
    print_tokens(c_source_file_path)
