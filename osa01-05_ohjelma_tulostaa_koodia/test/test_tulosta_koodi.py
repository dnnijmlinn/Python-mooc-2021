import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.tulosta_koodi'

@points('1.tulosta_koodi')
class TulostaKoodiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_tulostus(self):
        reload_module(self.module)
        output = get_stdout()
        split_output = output.split('\n')
        oikea = 'print("Moi kaikki!")'

        self.assertFalse(len(output) == 0, "Et tulostanut mitään :(")
        self.assertEqual(len(split_output), 1, "Tulostuksessa on ylimääräisiä rivejä.")
        self.assertTrue(output.count('print') == 1, f"Tulostuksesta puuttuu print-komento. Tulostus oli\n{output}\nsen odotettiin olevan\n{oikea}")
        self.assertTrue(output.count('"') == 2, f"Lainausmerkit puuttuvat tulostuksesta. Tulostus oli\n{output}\nsen odotettiin olevan\n{oikea}")
        self.assertEqual(output, oikea , f"Tulostus ei ole oikein. Tulostus oli\n{output}\nsen odotettiin olevan\n{oikea}")

if __name__ == '__main__':
    unittest.main()
