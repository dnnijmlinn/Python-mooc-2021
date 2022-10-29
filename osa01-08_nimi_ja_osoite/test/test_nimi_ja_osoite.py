import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.nimi_ja_osoite'

@points('1.nimi_ja_osoite')
class NimiJaOsoiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        test_input = "Pekka,Python,Pythonpolku 1,12345 Pythonila"
        test_output = "Pekka Python,Pythonpolku 1,12345 Pythonila".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            out = get_stdout()
            self.assertTrue(len(out)>0, "Ohjelmasi ei tulosta mitään") 
            output = out.split("\n")
            self.assertTrue(len(output) == 3, "Ohjelmasi ei tulostanut 3 riviä vaan " + str(len(output)))
            self.assertTrue(sanitize(output[0]) == sanitize(test_output[0]), f"Ensimmäinen rivi ei tulostunut oikein.\nOdotettiin\n{test_output[0]}\nrivi oli\n{output[0]}\nOhjelman syöte oli\n{test_input}")
            for i in range(1,3):
                self.assertEqual(output[i], test_output[i], '{}. rivi ei tulostunut oikein oikein syötteillä {}'.format((i + 1), test_input))
    
    def test_tulostus_2(self):
        test_input = "Keijo,Keksitty,Keksikuja 123 A 1,98765,Keksilä"
        test_output = "Keijo Keksitty,Keksikuja 123 A 1,98765,Keksilä".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertTrue(len(output) == 3, "Ohjelmasi ei tulostanut 3 riviä vaan " + str(len(output)))            
            self.assertTrue(sanitize(output[0]) == sanitize(test_output[0]), f"Ensimmäinen rivi ei tulostunut oikein.\nOdotettiin\n{test_output[0]}\nrivi oli\n{output[0]}\nOhjelman syöte oli\n{test_input}")
            for i in range(1, 3):
                self.assertEqual(output[i], test_output[i], '{}. rivi ei tulostunut oikein oikein syötteillä {}'.format((i + 1), test_input))
 
    def test_tulostus_3(self):
        test_input = "Maija Marjukka,Mielikuvitushahmo,Mielikuja 555 as. 234,12121,Tampere"
        test_output = "Maija Marjukka Mielikuvitushahmo,Mielikuja 555 as. 234,12121,Tampere".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertTrue(len(output) == 3, "Ohjelmasi ei tulostanut 3 riviä vaan " + str(len(output)))            
            self.assertTrue(sanitize(output[0]) == sanitize(test_output[0]), f"Ensimmäinen rivi ei tulostunut oikein.\nOdotettiin\n{test_output[0]}\nrivi oli\n{output[0]}\nOhjelman syöte oli\n{test_input}")
            for i in range(1, 3):
                self.assertEqual(output[i], test_output[i], '{}. rivi ei tulostunut oikein oikein syötteillä {}'.format((i + 1), test_input))
            
if __name__ == '__main__':
    unittest.main()
