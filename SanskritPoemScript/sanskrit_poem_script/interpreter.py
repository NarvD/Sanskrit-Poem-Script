from .parser import SanskritPoemScriptParser
from .stdlib import SanskritPoemScriptStdlib

class SanskritPoemScriptInterpreter:
    def __init__(self):
        self.parser = SanskritPoemScriptParser()
        self.parser.build()
        self.stdlib = SanskritPoemScriptStdlib()

    def interpret(self, ast, environment=None):
        if environment is None:
            environment = self.stdlib.get_global_environment()

        for node in ast:
            self._interpret_node(node, environment)

    def _interpret_node(self, node, environment):
        # Handle different node types in the AST.
        pass  # Implement the logic for interpreting each node type here.

    def run(self, code):
        ast = self.parser.parse(code)
        self.interpret(ast)

if __name__ == '__main__':
    interpreter = SanskritPoemScriptInterpreter()
    code = '''
    prathamam()
        vani("Namaste, Jagat!")
    '''
    interpreter.run(code)
