import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.tulostukset_samalle_riville'

@points('1.tulostukset_samalle_riville')
class TulostuksetSamalleRivilleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        reload_module(self.module)
        output = get_stdout().split("\n")
        correct = "5 + 8 - 4 = 9"

        self.assertTrue(len(output) == 1, "Ohjelmasi ei tulostanut kaikkea yhdelle rivlle, vaan se tulosti " + str(len(output)) + " riviä.")
        self.assertEqual(output[0], correct, "Tuloste  on väärin: pitäisi olla\n{}\nmutta ohjelmasi tulostaa\n{}".format(correct, output[0]))            
   
if __name__ == '__main__':
    unittest.main()
