import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.lausahdukset'

@points('1.lausahdukset')
class LausahduksetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        pieces = "simsala bimsala bim"
        plist = pieces.split()
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output.split("\n")) == 1, "Ohjelmasi ei tulostanut 1 riviä vaan " + str(len(output)))            
            self.assertTrue(output.count("-") == 2, f"Tulostuksessa pitäisi olla kaksi väliviivaa (-), nyt niitä oli {output.count('-')} kpl")
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Tulostuksesta ei löytynyt palaa " + piece +f" kun syöte on {pieces}")
            self.assertTrue(output.strip().count(" ") == 0, "Tulostuksessa on ylimääräisiä välilyöntejä.")
            vast = pieces.replace(" ", "-")+"!"
            self.assertTrue(output == vast, f"Tulostus ei ole esimerkin mukainen.\nTulostus oli\n{output}\nSen olisi pitänyt olla\n{vast}\nKun syöte on\n{pieces}")

    def test_tulostus_2(self):
        pieces = "hali tuli jallaa"
        plist = pieces.split()
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output.split("\n")) == 1, "Ohjelmasi ei tulostanut 1 riviä vaan " + str(len(output)))            
            self.assertTrue(output.count("-") == 2, "Tulostuksesta ei löytynyt kahta väliviivaa (-).")
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Tulostuksesta ei löytynyt palaa " + piece)
            self.assertTrue(output.strip().count(" ") == 0, "Tulostuksessa on ylimääräisiä välilyöntejä.")
            
            self.assertEqual(output, pieces.replace(" ", "-")+"!", "Tulostus ei ole esimerkin mukainen.")
    
    def test_tulostus_3(self):
        pieces = "jokeri pokeri poks"
        plist = pieces.split()
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output.split("\n")) == 1, "Ohjelmasi ei tulostanut 1 riviä vaan " + str(len(output)))            
            self.assertTrue(output.count("-") == 2, "Tulostuksesta ei löytynyt kahta väliviivaa (-).")
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Tulostuksesta ei löytynyt palaa " + piece)
            self.assertTrue(output.strip().count(" ") == 0, "Tulostuksessa on ylimääräisiä välilyöntejä.")
            
            self.assertEqual(output, pieces.replace(" ", "-")+"!", "Tulostus ei ole esimerkin mukainen.")
    
if __name__ == '__main__':
    unittest.main()
