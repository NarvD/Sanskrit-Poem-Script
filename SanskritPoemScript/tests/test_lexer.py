import unittest
from sanskrit_poem_script.lexer import SanskritPoemScriptLexer

class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = SanskritPoemScriptLexer()

    def test_tokens(self):
        # Test the lexer for correct tokenization
        self.lexer.input('prathamam() vani("Namaste, Jagat!")')
        tokens = [t.type for t in self.lexer]
        expected = ['PRATHAMAM', 'LPAREN', 'RPAREN', 'VANI', 'LPAREN', 'STRING', 'RPAREN']
        self.assertEqual(tokens, expected)

if __name__ == '__main__':
    unittest.main()
