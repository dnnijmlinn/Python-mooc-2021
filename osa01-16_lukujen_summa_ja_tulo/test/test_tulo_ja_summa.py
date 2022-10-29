import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.tulo_ja_summa'

@points('1.tulo_ja_summa')
class TuloJaSummaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_kolme_ja_seitseman(self):
        with patch('builtins.input', side_effect = [ '3', '7', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.failIf(prompt.call_count < 2, 'Ohjelman tulee pyytää kahta syötettä.')
            self.assertTrue(len(output)>0, 'Ohjelmasi ei tulosta mitään' )
            self.assertTrue('10' in output, 'Ohjelmasi ei tulosta lukujen 3 ja 7 summaa oikein. Odotettiin: 10'+ '\nohjelmasi tulostus oli\n'+ str(output))
            self.assertTrue('21' in output, 'Ohjelmasi ei tulosta lukujen 3 ja 7 tuloa oikein. Odotettiin: 21'+ '\nohjelmasi tulostus oli\n'+ str(output))
            expected = f"Lukujen summa 10"

            self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä 3 ja 7 ohjelmasi tulostuksessa pitäisi olla rivi\n{}\nohjelmasi tulostus oli\n{}".format(expected, output))
            expected = f"Lukujen tulo 21"
            self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä 3 ja 7 ohjelmasi tulostuksessa pitäisi olla rivi\n{}\nohjelmasi tulostus oli\n{}".format(expected, output))
            
    def test_lisatestit(self):
        testset = [
            ['0', '0'],
            ['0', '1'],
            ['13', '4'],
            ['7', '191'],
            ['716', '28213']
        ]
        for a, b in testset:
            with patch('builtins.input', side_effect = [ a, b, AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
                reload_module(self.module)
                output = get_stdout()
                summ =  int(a) + int(b) 
                prod = int(a) * int(b) 
                inputs = f"{a} ja {b}"
                self.assertTrue(str(summ) in output, 'Syötteillä {} summa laskettu väärin. Odotettiin: {}'.format(inputs, summ))
                self.assertTrue(str(prod) in output, 'Syötteillä {} tulo laskettu väärin. Odotettiin: {}'.format(inputs, prod))
                expected = f"Lukujen summa {summ}"
                self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä {} ohjelmasi tulisi tulostaa: {}".format(inputs, expected))
                expected = f"Lukujen tulo {prod}"
                self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä {} ohjelmasi tulisi tulostaa: {}".format(inputs, expected))

if __name__ == '__main__':
    unittest.main()
