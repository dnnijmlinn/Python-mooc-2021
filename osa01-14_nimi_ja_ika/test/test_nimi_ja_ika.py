import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, assert_ignore_ws

exercise = 'src.nimi_ja_ika'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.nimi_ja_ika')
class NimiJaIkaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_keijo_keksitty(self):
        with patch('builtins.input', side_effect = [ 'Keijo Keksitty', '1990', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, 'Ohjelmasi ei tulosta mitään' )
            e = 'Moi Keijo Keksitty, olet 30 vuotta vanha vuoden 2020 lopussa'
            assert_ignore_ws(self, output, e, "Kun syöte on Keijo Keksitty 1990\n")

    def test_muita_nimia1(self):
        testset = [
            ['Pekka Python', '2019', '1'],
        ]
        for nimi, syntvuosi, ika in testset:
            with patch('builtins.input', side_effect = [nimi, syntvuosi]):
                reload_module(self.module)
                output = get_stdout()
                e = f"Moi {nimi}, olet {ika} vuotta vanha vuoden 2020 lopussa"
                assert_ignore_ws(self, output, e, f"Kun syöte on {nimi} {syntvuosi}\n")

    def test_muita_nimia2(self):
        testset = [
            ['Angela Merkel', '1954', '66'],
        ]
        for nimi, syntvuosi, ika in testset:
            with patch('builtins.input', side_effect = [nimi, syntvuosi]):
                reload_module(self.module)
                output = get_stdout()
                e = f"Moi {nimi}, olet {ika} vuotta vanha vuoden 2020 lopussa"
                assert_ignore_ws(self, output, e, f"Kun syöte on {nimi} {syntvuosi}\n")


    def test_muita_nimia3(self):
        testset = [
            ['Venla Ruuska', '2013', '7'],
        ]
        for nimi, syntvuosi, ika in testset:
            with patch('builtins.input', side_effect = [nimi, syntvuosi]):
                reload_module(self.module)
                output = get_stdout()
                e = f"Moi {nimi}, olet {ika} vuotta vanha vuoden 2020 lopussa"
                assert_ignore_ws(self, output, e, f"Kun syöte on {nimi} {syntvuosi}\n")


if __name__ == '__main__':
    unittest.main()
