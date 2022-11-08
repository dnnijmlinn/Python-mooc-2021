import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.puhelinluettelo_versio2'

def f(d):
    return '\n'.join(d)
def s(d):
    return d.split('\n')

@points('5.puhelinluettelo_versio2')
class PuhelinluetteloVersio2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["3"]):
            cls.module = load_module(exercise, 'fi')

    def test_1_pysähtyy(self):

        with patch('builtins.input', side_effect = ["3", AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n3")
    
    def test_2_lisaamaton_ei_loydy(self):
        syote="""1
maija
3"""
        words = s(syote)
        with patch('builtins.input', side_effect = s(syote) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")
        
            exp = """ei numeroa
lopetetaan..."""

            expWordrs = exp.split('\n')

            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
            """
            #\n{mssage}") 
            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expWordrs), len(output), f"Ohjelmasi tulostaa {len(expWordrs)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi olla\n{exp}")
            for i in range(len(expWordrs)):
                e = expWordrs[i]
                line = output[i]
                self.assertEqual(line, e, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nsen tulostama rivi numero {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\nOhjelman koko tulostus on:\n{output_all}\nTulostuksen pitäisi olla\n{exp}")

    def test_3_lisaatty_loytyy(self):
        syote="""2
maija
040-234567
1
maija
3"""
        words = s(syote)
        with patch('builtins.input', side_effect = s(syote) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")
        
            exp = """ok!
040-234567
lopetetaan..."""

            expWordrs = exp.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expWordrs), len(output), f"Ohjelmasi tulostaa {len(expWordrs)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi olla\n{exp}")
            for i in range(len(expWordrs)):
                e = expWordrs[i]
                line = output[i]
                self.assertEqual(line, e, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nsen tulostama rivi numero {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\nOhjelman koko tulostus on:\n{output_all}\nTulostuksen pitäisi olla\n{exp}")

    def test_4_uusi_numero_lisataan(self):
        syote="""2
maija
040-234567
2
maija
09-334455
1
maija
3"""
        words = s(syote)
        with patch('builtins.input', side_effect = s(syote) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")
        
            exp1 = """ok!
ok!
040-234567
09-334455
lopetetaan..."""

            exp2 = """ok!
ok!
09-334455
040-234567
lopetetaan..."""

            expWordrs1 = exp1.split('\n')
            expWordrs2 = exp2.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expWordrs1), len(output), f"Ohjelmasi tulostaa {len(expWordrs1)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nMuista että tässä tehtävässä uusi numero ei saa korvata vanhaa!")
            for i in range(len(expWordrs1)):
                e = expWordrs1[i]
                e2 = expWordrs2[i]
                line = output[i]
                if expWordrs1[i] == expWordrs2[i]:
                    self.assertEqual(line, e, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nsen tulostama rivi numero {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\nOhjelman koko tulostus on:\n{output_all}\nTulostuksen pitäisi olla\n{exp1}")
                else:
                    self.assertTrue(line==e or line==e2, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nsen tulostama rivi numero {i+1} on väärä, sen pitäisi olla\n{e}\ntai\n{e}\nrivi on\n{line}\nOhjelman koko tulostus on:\n{output_all}\nTulostuksen pitäisi olla\n{exp1}")

    def test_5_monta_komentoa(self):
        syote="""2
mikko
040-234567
2
maija
09-334455
1
maija
1
mikko
1
pekka
2
mikko
045-554433
1
mikko
3"""
        words = s(syote)
        with patch('builtins.input', side_effect = s(syote) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")
        
            exp1 = """ok!
ok!
09-334455
040-234567
ei numeroa
ok!
045-554433
040-234567
lopetetaan..."""
        
            exp2 = """ok!
ok!
09-334455
040-234567
ei numeroa
ok!
040-234567
045-554433
lopetetaan..."""

            expWordrs1 = exp1.split('\n')
            expWordrs2 = exp2.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expWordrs1), len(output), f"Ohjelmasi tulostaa {len(expWordrs1)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nMuista että tässä tehtävässä uusi numero ei saa korvata vanhaa!")
            for i in range(len(expWordrs1)):
                e = expWordrs1[i]
                e2 = expWordrs2[i]
                line = output[i]
                if expWordrs1[i] == expWordrs2[i]:
                    self.assertEqual(line, e, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nsen tulostama rivi numero {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\nOhjelman koko tulostus on:\n{output_all}\nTulostuksen pitäisi olla\n{exp1}")
                else:
                    self.assertTrue(line==e or line==e2, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nsen tulostama rivi numero {i+1} on väärä, sen pitäisi olla\n{e}\ntai\n{e}\nrivi on\n{line}\nOhjelman koko tulostus on:\n{output_all}\nTulostuksen pitäisi olla\n{exp1}")

    def test_6_monta_komentoa(self):
        syote="""2
leevi
040-1212334
2
venla
09-334455
2
eero
050-2255433
1
maija
1
venla
1
eero
2
leevi
045-554433
1
leevi
3"""
        words = s(syote)
        with patch('builtins.input', side_effect = s(syote) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelma pysähtyy syötteellä\n{f(words)}")
        
            exp1 = """ok!
ok!
ok!
ei numeroa
09-334455
050-2255433
ok!
040-1212334
045-554433
lopetetaan..."""

            exp2 = """ok!
ok!
ok!
ei numeroa
09-334455
050-2255433
ok!
045-554433
040-1212334
lopetetaan..."""

            expWordrs1 = exp1.split('\n')
            expWordrs2 = exp2.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expWordrs1), len(output), f"Ohjelmasi tulostaa {len(expWordrs1)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nMuista että tässä tehtävässä uusi numero ei saa korvata vanhaa!")
            for i in range(len(expWordrs1)):
                e = expWordrs1[i]
                e2 = expWordrs2[i]
                line = output[i]
                if expWordrs1[i] == expWordrs2[i]:
                    self.assertEqual(line, e, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nsen tulostama rivi numero {i+1} on väärä, sen pitäisi olla\n{e}\nrivi on\n{line}\nOhjelman koko tulostus on:\n{output_all}\nTulostuksen pitäisi olla\n{exp1}")
                else:
                    self.assertTrue(line==e or line==e2, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nsen tulostama rivi numero {i+1} on väärä, sen pitäisi olla\n{e}\ntai\n{e}\nrivi on\n{line}\nOhjelman koko tulostus on:\n{output_all}\nTulostuksen pitäisi olla\n{exp1}")

if __name__ == '__main__':
    unittest.main()
