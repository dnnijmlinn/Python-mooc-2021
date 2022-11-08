import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.arvosanatilasto'

def f(d):
    return '\n'.join(d)
 
@points('4.arvosanatilasto')
class ArvosteluasteikkoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["20 100", "12 34",""]):
            cls.module = load_module(exercise, 'fi')

    def test_toiminnallisuus_3(self):
            words = "18 80;15 60;".split(";")         
            expected = """Tilasto:
Pisteiden keskiarvo: 23.5
Hyväksymisprosentti: 100.0
Arvosanajakauma:
  5:
  4: *
  3: *
  2:
  1:
  0:""".split('\n')
        
            with patch('builtins.input', side_effect = words + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")

                self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")   
                output = [line for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(len(expected), len(output), f"Ohjelmasi tulostaa 10 rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}")   
                for i in range(len(expected)):
                    e = expected[i].strip()
                    line = output[i].strip()
                    self.assertEqual(line, e, f"Ohjelmasi tulostama rivi {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\ntulostus on:\n{output_all}\nsyötteellä:\n{f(words)}")

    def test_toiminnallisuus_4(self):
            words = "20 100;10 50;5 10;".split(";")         
            expected = """Tilasto:
Pisteiden keskiarvo: 17.0
Hyväksymisprosentti: 66.7
Arvosanajakauma:
5: *
4:
3:
2:
1: *
0: *""".split('\n')
        
            with patch('builtins.input', side_effect = words + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")

                self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")   
                output = [line for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(len(expected), len(output), f"Ohjelmasi tulostaa 10 rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}")   
                for i in range(len(expected)):
                    e = expected[i].strip()
                    line = output[i].strip()
                    self.assertEqual(line, e, f"Ohjelmasi tulostama rivi {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\ntulostus on:\n{output_all}\nsyötteellä:\n{f(words)}")

if __name__ == '__main__':
    unittest.main()
