import unittest
from sanskrit_poem_script.parser import SanskritPoemScriptParser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = SanskritPoemScriptParser()
        self.parser.build()

    def test_parse(self):
        # Test the parser for correct parsing
        ast = self.parser.parse('prathamam() vani("Namaste, Jagat!")')
        expected = [
            ('prathamam', [], [
                ('vani', ['Namaste, Jagat!'])
            ])
        ]
        self.assertEqual(ast, expected)

if __name__ == '__main__':
    unittest.main()
