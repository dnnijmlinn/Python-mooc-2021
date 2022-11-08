import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import choice

exercise = 'src.hello_visualstudio_code'

def f(d):
    return '\n'.join(d)

@points('4.hello_visualstudio_code')
class VsCodeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["emacs", "visual studio code"]):
            cls.module = load_module(exercise, 'fi')

    def test_1_pysähtyy(self):
        words = "emacs;visual studio code".split(";")
    
        with patch('builtins.input', side_effect = words + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")

    def test_2_toiminnallisuus_kunnossa(self):
        for string in [
                "emacs;visual studio code", "word;emacs;notepad;visual studio code"
            ]:
            words = string.split(";")
        
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
                self.assertEqual(len(words), len(output), f"Ohjelmasi tulostaa syötteellä {len(words)} rivin sijasta {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}")   
                for i in range(len(words)-2):
                    e = "ei ole hyvä" if not words[i] in ["word", "notepad"] else "surkea"
                    line = output[i]
                    self.assertEqual(line, e, f"Ohjelmasi tulostama rivi {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\nsyötteellä:\n{f(words)}\ntulostus on:\n{output_all}")
                
                e = "loistava valinta!"
                line = output[-1]
                self.assertEqual(line, e, f"Ohjelmasi tulostama viimeinen rivi on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\nsyötteellä:\n{f(words)}\tulostus on:\n{output_all}")
                
    def test_3_case_insensitive(self):
        for i in range(20):
            vsdc = ""
            for l in "visual studio code":
                vsdc += choice([l, l.upper()])
            words = ["emacs", vsdc]
    
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
                self.assertEqual(len(words), len(output), f"Ohjelmasi tulostaa syötteellä {len(words)} rivin sijasta {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}")   
                for i in range(len(words)-2):
                    e = "ei ole hyvä" if not words[i] in ["word", "notepad"] else "surkea"
                    line = output[i]
                    self.assertEqual(line, e, f"Ohjelmasi tulostama rivi {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\nsyötteellä:\n{f(words)}\ntulostus on:\n{output_all}")
                
                e = "loistava valinta!"
                line = output[-1]
                self.assertEqual(line, e, f"Ohjelmasi tulostama viimeinen rivi on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\nsyötteellä:\n{f(words)}\tulostus on:\n{output_all}")
               

if __name__ == '__main__':
    unittest.main()
