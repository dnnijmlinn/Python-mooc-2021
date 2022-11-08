import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.sama_sana_kahdesti'

def f(d):
    return '\n'.join(d)
 
@points('4.sama_sana_kahdesti')
class SamaSanaKahdestiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["python", "testi","python"]):
            cls.module = load_module(exercise, 'fi')

    def test_1_pysahtyy(self):
        words = "python testi python".split(" ")
    
        with patch('builtins.input', side_effect = words + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")

    def test_2_toiminnallisuus_kunnossa(self):
        for string in [
                "python testi python",
                "alussa oli suo kuokka ja jussi oli",
                "olipa kerran ohjelmoija kerran",
                "eka toka kolmas neljäs viides toka",
                "bugi bugi",
                "koodi toimii hyvin aina kun koodaan hyvin",
                "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua elit"
            ]:
            words = string.split(" ")
        
            with patch('builtins.input', side_effect = words + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")

                mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
                """
                #\n{mssage}")     
                self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}\n{mssage}")  
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(1, len(output), f"Ohjelmasi tulostaa yhden rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}")
                correct = "Annoit "+str(len(words)-1)+" eri sanaa"
                self.assertTrue(output[0].rstrip() == correct, f"Ohjelmasi tulostus on väärä, sen pitäisi olla\n{correct}\nrivi on\n{output[0]}\nkun syöte om:\n{f(words)}")

if __name__ == '__main__':
    unittest.main()
