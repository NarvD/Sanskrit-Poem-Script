import ply.lex as lex

class SanskritPoemScriptLexer:
    tokens = (
        'IDENTIFIER', 'STRING', 'NUMBER', 'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
        'IF', 'ELSE', 'WHILE', 'ENDIF', 'ENDWHILE'
    )

    literals = ('(', ')', '{', '}', ',')

    t_EQUALS = r'='
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_IF = r'if'
    t_ELSE = r'else'
    t_WHILE = r'while'
    t_ENDIF = r'endif'
    t_ENDWHILE = r'endwhile'

    t_ignore = ' \t'

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        return t

    def t_STRING(self, t):
        r'"[^"]*"'
        t.value = t.value[1:-1]
        return t

    def t_NUMBER(self, t):
        r'\d+(\.\d+)?'
        t.value = float(t.value) if '.' in t.value else int(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def tokenize(self, data):
        self.lexer.input(data)
        return iter(self.lexer)

if __name__ == '__main__':
    lexer = SanskritPoemScriptLexer()
    lexer.build()
    code = '''
    prathamam()
        vani("Namaste, Jagat!")
    '''
    for token in lexer.tokenize(code):
        print(token)
