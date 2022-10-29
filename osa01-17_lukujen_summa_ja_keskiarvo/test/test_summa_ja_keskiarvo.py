import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.summa_ja_keskiarvo'

@points('1.summa_ja_keskiarvo')
class SummaJaKeskiarvoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1234(self):
        with patch('builtins.input', side_effect = [ '1', '2', '3', '4', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(prompt.call_count < 2, 'Ohjelman tulee pyytää neljää syötettä.')
            self.assertTrue(len(output)>0, 'Ohjelmasi ei tulosta mitään' )
            self.assertTrue('10' in output, 'Ohjelmasi ei tulosta lukujen 1, 2, 3, ja 4 summaa oikein. Odotettiin: 10'+ '\nohjelmasi tulostus oli\n'+ str(output))
            self.assertTrue('2.5' in output, 'Ohjelmasi ei tulosta lukujen 1, 2, 3, ja 4 keskiarvoa oikein. Odotettiin: 2.5'+ '\nohjelmasi tulostus oli\n'+ str(output))
            expected = "Lukujen summa on 10 ja keskiarvo 2.5"
            self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä 1, 2, 3, ja 4 ohjelmasi tulisi tulostaa\n{}\nohjelmasi tulostus oli\n{}".format(expected, output))
            

    def test_lisatestit(self):
        testset = [
            [ '3', '7', '2', '8' ],
            [ '8', '-22', '75', '5' ],
            [ '0', '0', '0', '0' ],
        ]
        for a, b, c, d in testset:
            with patch('builtins.input', side_effect = [ a, b, c, d, AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
                reload_module(self.module)
                output = get_stdout()
                summ =  int(a) + int(b) + int(c) + int(d)
                avg = summ / 4
                inputs = f"{a}, {b}, {c} ja {d}"
                self.assertTrue(str(summ) in output, 'Syötteillä {} summa laskettu väärin. Odotettiin: {}'.format(inputs, summ))
                self.assertTrue(str(avg) in output, 'Syötteillä {} keskiarvo laskettu väärin. Odotettiin: {}'.format(inputs, avg))
                expected = f"Lukujen summa on {summ} ja keskiarvo {avg}"
                self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä {} ohjelmasi tulisi tulostaa\n{}".format(inputs, expected))

if __name__ == '__main__':
    unittest.main()
