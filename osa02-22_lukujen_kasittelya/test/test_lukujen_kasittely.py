import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.lukujen_kasittelya'

def pp(a):
    return "\n".join(a)

testset = [
    [str(i) for i in [1, 2, 3, 0, 3, 6, 2.0, 3, 0]],
    [str(i) for i in [5, 0, 1, 5, 5.0, 1, 0]],
    [str(i) for i in [5, 45, -3, 65, 3, 34, -9, 0,  7, 140, 20.0, 5, 2]],
    [str(i) for i in [3, -76, -7, 4, 55, 0, 5, -21, -4.2, 3, 2]]
]

class LukujenKasittelyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[1] + ["0"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0(self):
        values = "1 0".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelma lopettaa toiminnan syötteellä\n{}".format(pp(values)))

    @points('2.lukujen_kasittelya-osa1')
    def test_1_alku(self):
        with patch('builtins.input', side_effect=['1', '2', '3', '0', AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(['1', '2', '3', '0']) 

            self.assertFalse(len(output)==0, f"Ohjelmasi ei tulostaunut mitään syötteellä\n{inpt}" )
            expected = "Syötä kokonaislukuja, 0 lopettaa:"
            self.assertEqual(expected, output.split('\n')[0].strip(), f"Ohjelmasi pitäisi tulostaa alussa:\n{expected}\nohjelmasi tulosti:\n{output}" )

    @points('2.lukujen_kasittelya-osa1')
    def test_2_lkm(self):
        for *inpt, lkm, summa, ka, p, n  in testset: 
            with patch('builtins.input', side_effect=[*inpt, AssertionError("Syötettä pyydetään liian monta kertaa.") ],  ) as prompt:
                reload_module(self.module)
                output = get_stdout()  
                expected = f'Lukuja yhteensä {lkm}'     
                self.assertFalse(len(output)==0, f"Syötteellä \n{inpt}\nohjelmasi pitäisi tulostaa\n{expected}\nohjelmasi ei tulostaunut mitään" )
                self.assertTrue(sanitize(expected) in sanitize(output), f"Syötteellä \n{pp(inpt)}\nohjelmasi pitäisi tulostaa\n{expected}\nohjelmasi tulosti\n{output}" )

    @points('2.lukujen_kasittelya-osa2')
    def test_3_summa(self):
        for *inpt, lkm, summa, ka, p, n  in  testset:
            with patch('builtins.input', side_effect=[*inpt, AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
                reload_module(self.module)
                output = get_stdout()  
                expected = f'Lukujen summa {summa}'     
                self.assertTrue(sanitize(expected) in sanitize(output), f"Syötteellä \n{pp(inpt)}\nohjelmasi pitäisi tulostaa\n{expected}\nohjelmasi tulosti\n{output}" )

    @points('2.lukujen_kasittelya-osa3')
    def test_4_ka(self):
        for *inpt, lkm, summa, ka, p, n in  testset: #[testset[0]]:
            with patch('builtins.input', side_effect=[*inpt, AssertionError("Syötettä pyydetään liian monta kertaa.") ], )  as prompt:
                reload_module(self.module)
                output = get_stdout()  
                expected = f'Lukujen keskiarvo {ka}'     
                self.assertTrue(sanitize(expected) in sanitize(output), f"Syötteellä \n{pp(inpt)}\n ohjelmasi pitäisi tulostaa\n{expected}\nohjelmasi tulosti\n{output}" )

    @points('2.lukujen_kasittelya-osa4')
    def test_5_posneg(self):
        for *inpt, lkm, summa, ka, p, n in  testset: #[testset[0]]:
            with patch('builtins.input', side_effect=[*inpt, AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
                reload_module(self.module)
                output = get_stdout()  
                expected = f'Positiivisia {p}'     
                self.assertTrue(sanitize(expected) in sanitize(output), f"Syötteellä\n{pp(inpt)}\nohjelmasi pitäisi tulostaa\n{expected}\nohjelmasi tulosti\n{output}" )
                expected = f'Negatiivisia {n}'     
                self.assertTrue(sanitize(expected) in sanitize(output), f"Syötteellä\n{pp(inpt)}\nohjelmasi pitäisi tulostaa\n{expected}\nohjelmasi tulosti\n{output}" )

if __name__ == '__main__':
    unittest.main()
