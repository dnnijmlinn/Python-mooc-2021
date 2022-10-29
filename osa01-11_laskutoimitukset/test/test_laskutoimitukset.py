import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.laskutoimitukset'

@points('1.laskutoimitukset')
class LaskutoimituksetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        reload_module(self.module)
        output = get_stdout().split("\n")
        correct = self.generate(27,15)

        self.assertTrue(len(output) == 4, "Ohjelmasi ei tulostanut 4 riviä vaan " + str(len(output)) + " riviä.")
        for i in range(4):
            self.assertEqual(output[i].rstrip(), correct[i], "Tuloste rivillä {} on väärä: pitäisi olla\n{}\nmutta ohjelmasi tulostaa\n{}".format((i + 1), correct[i], output[i]))            
        
    def generate(self, x, y):
        s = [""] * 4
        s[0] = "{} + {} = {}".format(x, y, (x + y))
        s[1] = "{} - {} = {}".format(x, y, (x - y))
        s[2] = "{} * {} = {}".format(x, y, (x * y))
        s[3] = "{} / {} = {}".format(x, y, (x / y))
        return s
   

if __name__ == '__main__':
    unittest.main()
