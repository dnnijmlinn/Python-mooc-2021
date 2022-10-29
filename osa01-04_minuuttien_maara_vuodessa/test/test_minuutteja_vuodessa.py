import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.minuutteja_vuodessa'

@points('1.minuutteja_vuodessa')
class MinuuttejaVuodessaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_tulostus(self):
        reload_module(self.module)
        output = get_stdout()
        split_output = output.split('\n')

        # self.assertEqual(len(split_output), 1, "Tulostuksessa on ylimääräisiä rivejä.")
        self.assertTrue(output.find("525600") > -1, "Tulostukseen ei sisälly oikeaa minuuttimäärää.")

if __name__ == '__main__':
    unittest.main()
