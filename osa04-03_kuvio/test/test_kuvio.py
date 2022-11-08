import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.kuvio'

def okuvio(y_korkeus, y_merkki, a_korkeus, a_merkki):
    i = 1
    lines = []
    while i<=y_korkeus:
        lines.append(y_merkki*i)
        i += 1
    i = a_korkeus
    while i>0:
        lines.append(a_merkki*y_korkeus)
        i -= 1
    return lines

@points('4.kuvio')
class KuvioTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.kuvio import kuvio
        except:
            self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään kuvio')
        try:
            from src.kuvio import kuvio
            kuvio(5,"-", 3, "*")
        except:
            self.assertTrue(False, f'Varmista että funktion suoritus onnistuu seuraavasti\nkuvio(5, "-", 3, "*")')



    def test_2_kuvio_kunnossa(self):
        for y_korkeus, y_merkki, a_korkeus, a_merkki in [(5, "X", 3, "*"),(3, "X", 1, "*"), (4, "x", 5, "X"), (4, "x", 0, "X"),(5, "o", 3, "O"), (1, "^", 5, "|"), (3, "z", 3, "Z") ,(20, "@", 20, "$")  ]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_alussa = get_stdout()
                from src.kuvio import kuvio
                kuvio(y_korkeus, y_merkki, a_korkeus, a_merkki)
                output_all = get_stdout().replace(output_alussa, '', 1)
                
                output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

                exp = okuvio(y_korkeus, y_merkki, a_korkeus, a_merkki)

                self.assertTrue(len(output_all)>0, f'Funktiokutsu kuvio({y_korkeus}, "{y_merkki}", {a_korkeus}, "{a_merkki}") ei tulosta mitään')
                acual = '\n'.join(output)
                self.assertEqual(len(exp), len(output), f'Funktiokutsun  kuvio({y_korkeus}, "{y_merkki}", {a_korkeus}, "{a_merkki}") pitäisi tulostaa {len(exp)} riviä, nyt se tulostaa {len(output)} riviä, tulostus oli\n{acual}')
                for i in range(len(exp)):
                    self.assertEqual(exp[i], output[i].strip(), f'Funktiokutsun  kuvio({y_korkeus}, "{y_merkki}", {a_korkeus}, "{a_merkki}") tulostaman rivin {i+1} pitäisi olla:\n{exp[i]}\nmutta se on:\n{output[i]}\nFunktiosi koko tulostus oli\n{output_all}')

    def test_3_viiva_funktio_kaytossa(self):
        src_file = os.path.join('src', 'kuvio.py')
        with open(src_file) as f:
            funktiossa = False
            for line in f:
                if 'def kuvio' in line:
                    funktiossa = True
                elif 'def viiva' in line:
                    funktiossa = False
                elif line[0] != " " and line[0] != "#":
                    funktiossa = False

                if funktiossa:           
                    if '  print(' in line:
                        self.assertTrue(False, f"funktio kuvio ei saa käyttää print-komentoja tulostamiseen eli koodissasi ei saa olla riviä\n{line}")

if __name__ == '__main__':
    unittest.main()
