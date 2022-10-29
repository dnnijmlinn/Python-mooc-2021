import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.huomisen_vaatteet'

housut_tpaita = "Pue housut ja t-paita"
pitkahih = "Ota myös pitkähihainen paita"
takki = "Pue päälle takki"
lammin_takki = "Suosittelen lämmintä takkia"
hanskat = "Kannattaa ottaa myös hanskat"
sateenvarjo = "Muista sateenvarjo!"


@points('1.huomisen_vaatteet')
class VaatteetTest(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_25(self):
        with patch('builtins.input', side_effect = [ '25', 'ei', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "25, ei"
            self.assertFalse(prompt.call_count < 1, 'Ohjelman tulee pyytää kahta syötettä.')
            self.assertTrue(housut_tpaita in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + housut_tpaita+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(pitkahih in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + pitkahih+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(takki in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(lammin_takki in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + lammin_takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(hanskat in output, f"Syötteellä:\n{syote}\nohjelmanEI pitäisi tulostaa riviä\n" + hanskat+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(sateenvarjo in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + sateenvarjo+ "\nohjelmasi tulostaa\n"+ output)
    
    def test_21_sade(self):
        with patch('builtins.input', side_effect = [ '21', 'kyllä', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "21, kyllä"
            self.assertFalse(prompt.call_count < 1, 'Ohjelman tulee pyytää kahta syötettä.')
            self.assertTrue(housut_tpaita in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + housut_tpaita+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(pitkahih in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + pitkahih+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(takki in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(lammin_takki in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + lammin_takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(hanskat in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + hanskat+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(sateenvarjo in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + sateenvarjo+ "\nohjelmasi tulostaa\n"+ output)
    
    def test_15(self):
        with patch('builtins.input', side_effect = [ '15', 'ei', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "15, ei"
            self.assertFalse(prompt.call_count < 1, 'Ohjelman tulee pyytää kahta syötettä.')
            self.assertTrue(housut_tpaita in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + housut_tpaita+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(pitkahih in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + pitkahih+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(takki in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(lammin_takki in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + lammin_takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(hanskat in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + hanskat+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(sateenvarjo in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + sateenvarjo+ "\nohjelmasi tulostaa\n"+ output)
    
    def test_20_sade(self):
        with patch('builtins.input', side_effect = [ '20', 'kyllä', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "20, kyllä"
            self.assertFalse(prompt.call_count < 1, 'Ohjelman tulee pyytää kahta syötettä.')
            self.assertTrue(housut_tpaita in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + housut_tpaita+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(pitkahih in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + pitkahih+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(takki in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(lammin_takki in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + lammin_takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(hanskat in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + hanskat+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(sateenvarjo in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + sateenvarjo+ "\nohjelmasi tulostaa\n"+ output)
    
    def test_10(self):
        with patch('builtins.input', side_effect = [ '10', 'ei', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "10, ei"
            self.assertFalse(prompt.call_count < 1, 'Ohjelman tulee pyytää kahta syötettä.')
            self.assertTrue(housut_tpaita in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + housut_tpaita+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(pitkahih in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + pitkahih+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(takki in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(lammin_takki in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + lammin_takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(hanskat in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + hanskat+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(sateenvarjo in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + sateenvarjo+ "\nohjelmasi tulostaa\n"+ output)
    
    def test_3(self):
        with patch('builtins.input', side_effect = [ '3', 'ei', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "3, ei"
            self.assertFalse(prompt.call_count < 1, 'Ohjelman tulee pyytää kahta syötettä.')
            self.assertTrue(housut_tpaita in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + housut_tpaita+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(pitkahih in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + pitkahih+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(takki in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(lammin_takki in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + lammin_takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(hanskat in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + hanskat+ "\nohjelmasi tulostaa\n"+ output)
            self.assertFalse(sateenvarjo in output, f"Syötteellä:\n{syote}\nohjelman EI pitäisi tulostaa riviä\n" + sateenvarjo+ "\nohjelmasi tulostaa\n"+ output)
    
    def test_5_sade(self):
        with patch('builtins.input', side_effect = [ '5', 'kyllä', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "5, kyllä"
            self.assertFalse(prompt.call_count < 1, 'Ohjelman tulee pyytää kahta syötettä.')
            self.assertTrue(housut_tpaita in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + housut_tpaita+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(pitkahih in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + pitkahih+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(takki in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(lammin_takki in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + lammin_takki+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(hanskat in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + hanskat+ "\nohjelmasi tulostaa\n"+ output)
            self.assertTrue(sateenvarjo in output, f"Syötteellä:\n{syote}\nohjelman pitäisi tulostaa rivi\n" + sateenvarjo+ "\nohjelmasi tulostaa\n"+ output)
    

if __name__ == '__main__':
    unittest.main()
