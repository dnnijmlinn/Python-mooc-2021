import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.nelio'

def okuvio(y_korkeus, y_merkki):
    i = 1
    lines = []
    while i<=y_korkeus:
        lines.append(y_merkki*y_korkeus)
        i += 1

    return lines

@points('4.nelio')
class NelioTest(unittest.TestCase):
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
            from src.nelio import nelio
        except:
            self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään nelio')
        try:
            from src.nelio import nelio
            nelio(5,"-")
        except:
            self.assertTrue(False, f'Varmista että funktion suoritus onnistuu seuraavasti\nnelio(5, "-")')


    def test_2_nelio_kunnossa(self):
        for y_korkeus, y_merkki in [(5, "+"),(3, "X"), (4, "x"), (4, "x"),(5, "o"), (1, "^"), (3, "z") ,(20, "@") ]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_alussa = get_stdout()
                from src.nelio import nelio
                nelio(y_korkeus, y_merkki)
                output_all = get_stdout().replace(output_alussa, '', 1)
                
                output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

                exp = okuvio(y_korkeus, y_merkki)

                self.assertTrue(len(output_all)>0, f'Funktiokutsu nelio({y_korkeus}, "{y_merkki}") ei tulosta mitään')
                acual = '\n'.join(output)
                self.assertEqual(len(exp), len(output), f'Funktiokutsun nelio({y_korkeus}, "{y_merkki}") pitäisi tulostaa {len(exp)} riviä, nyt se tulostaa {len(output)} riviä, tulostus oli\n{acual}')
                for i in range(len(exp)):
                    self.assertEqual(exp[i], output[i].strip(), f'Funktiokutsun nelio({y_korkeus}, "{y_merkki}") tulostaman rivin {i+1} pitäisi olla:\n{exp[i]}\nmutta se on:\n{output[i]}\nFunktiosi koko tulostus oli\n{output_all}')

    def test_viiva_funktio_kaytossa(self):
        src_file = os.path.join('src', 'nelio.py')
        with open(src_file) as f:
            funktiossa = False
            for line in f:
                if 'def nelio' in line:
                    funktiossa = True
                elif 'def viiva' in line:
                    funktiossa = False
                elif line[0] != " " and line[0] != "#":
                    funktiossa = False

                if funktiossa:           
                    if '  print(' in line:
                        self.assertTrue(False, f"funktio nelio ei saa käyttää print-komentoja tulostamiseen eli koodissasi ei saa olla riviä\n{line}")

if __name__ == '__main__':
    unittest.main()
