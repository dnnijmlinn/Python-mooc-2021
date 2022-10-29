import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.alleviivaus'

def format_tuple(d : tuple):
    return str(d).replace("'","")

def f(d):
    return ' '.join(d) + " (tyhjä)"

@points('3.alleviivaus')
class AlleviivausTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["ei", '']):
            cls.module = load_module(exercise, 'fi')

    def test_1_pysähtyy_tyhjaan(self):
        words = "python kokeilu".split(" ")
    
        with patch('builtins.input', side_effect = words+ ['', AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, "Varmista, että ohjelma pysähtyy syötteellä {}".format(f(words)))

    def test_2_kaksi_sanaa(self):
        words = "python kokeilu".split(" ")
    
        with patch('builtins.input', side_effect = words+ ['', AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            reload_module(self.module)
            output_all = get_stdout()
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
    
            self.assertEqual(len(words)*2, len(output), f"Ohjelmasi tulostaa syötteellä {f(words)} {len(words)*2} rivin sijasta {len(output)} riviä:\n{output_all}")
            for i in range(len(output)):
                line = output[i]
                if i%2==1:
                    e = '-'*len(words[i//2])
                    self.assertEqual(line, e, f"Ohjelmasi tulostama rivi {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\ntulostus on:\n{output_all}")

    def test_3_monta_sanaa(self):
        words = "testi heippa simsalabim zorro viuh!".split(" ")
    
        with patch('builtins.input', side_effect = words+ ['', AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            reload_module(self.module)
            output_all = get_stdout()
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
    
            self.assertEqual(len(words)*2, len(output), f"Ohjelmasi tulostaa syötteellä {f(words)} {len(words)*2} rivin sijasta {len(output)} riviä:\n{output_all}")
            for i in range(len(output)):
                line = output[i]
                if i%2==1:
                    e = '-'*len(words[i//2])
                    self.assertEqual(line, e, f"Ohjelmasi tulostama rivi {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\ntulostus on:\n{output_all}")

    def test_4_monta_lausetta(self):
        words = ["Moi kaikki", "Hei sun heipparallaa!", "Tämä on pidempi testilause", "Onnistuuko tämäkin - kohtahan se nähdään...", "Vielä yksi testi: testi!!"]
    
        with patch('builtins.input', side_effect = words+ ['', AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            reload_module(self.module)
            output_all = get_stdout()
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
    
            self.assertEqual(len(words)*2, len(output), f"Ohjelmasi tulostaa syötteellä {f(words)} {len(words)*2} rivin sijasta {len(output)} riviä:\n{output_all}")
            for i in range(len(output)):
                line = output[i]
                if i%2==1:
                    e = '-'*len(words[i//2])
                    self.assertEqual(line, e, f"Ohjelmasi tulostama rivi {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\ntulostus on:\n{output_all}")


if __name__ == '__main__':
    unittest.main()
