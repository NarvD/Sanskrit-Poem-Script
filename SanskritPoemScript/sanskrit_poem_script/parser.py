import ply.yacc as yacc
from .lexer import SanskritPoemScriptLexer

class SanskritPoemScriptParser:
    tokens = SanskritPoemScriptLexer.tokens

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
    )

    def p_program(self, p):
        'program : statements'
        p[0] = p[1]

    def p_statements(self, p):
        '''statements : statement
                      | statements statement'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_statement(self, p):
        '''statement : expression
                     | assignment
                     | if_statement
                     | while_statement
                     | function_definition
                     | function_call'''
        p[0] = p[1]

    # Add your grammar rules for the different statement types here.

    def p_error(self, p):
        if p:
            print(f"Syntax error at '{p.value}'.")
        else:
            print("Syntax error at EOF.")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, data):
        return self.parser.parse(data, lexer=SanskritPoemScriptLexer().lexer)

if __name__ == '__main__':
    parser = SanskritPoemScriptParser()
    parser.build()
    code = '''
    prathamam()
        vani("Namaste, Jagat!")
    '''
    ast = parser.parse(code)
    print(ast)
