import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.hymio'
@points('1.hymio')
class HymioTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_print_hymio(self):
        reload_module(self.module)
        output = get_stdout()
        self.assertTrue(output.startswith(":"), "Varmista että et tulosta ennen hymiön alkua ylimääräisiä merkkejä")
        self.assertTrue(output.endswith(")"), "Varmista että et tulosta hymiön loppuun ylimääräisiä merkkejä")
        self.assertEqual(output, ":-)", "Epämuodostunut hymiö.")

if __name__ == '__main__':
    unittest.main()
    