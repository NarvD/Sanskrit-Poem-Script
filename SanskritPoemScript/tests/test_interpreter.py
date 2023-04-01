import unittest
import io
import sys
from sanskrit_poem_script.interpreter import SanskritPoemScriptInterpreter

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = SanskritPoemScriptInterpreter()

    def test_interpret(self):
        # Test the interpreter for correct interpretation and output
        code = '''
        prathamam()
            vani("Namaste, Jagat!")
        '''

        # Redirect stdout to a string buffer
        buffer = io.StringIO()
        sys.stdout = buffer

        self.interpreter.run(code)

        # Reset stdout
        sys.stdout = sys.__stdout__

        output = buffer.getvalue()
        expected_output = "Namaste, Jagat!\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
