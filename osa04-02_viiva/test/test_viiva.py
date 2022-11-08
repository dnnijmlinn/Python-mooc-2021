import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.viiva'

@points('4.viiva')
class ViivaTest(unittest.TestCase):
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
            from src.viiva import viiva
        except:
            self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään viiva')
        try:
            from src.viiva import viiva
            viiva(5,"-")
        except:
            self.assertTrue(False, f'Varmista että funktion suoritus onnistuu seuraavasti\nviiva(5, "-")')



    def test_2_funktiota_voi_kutsua_tyhjalla_merkkijonolla(self):
        try:
            from src.viiva import viiva
            viiva(5,"")
        except:
            self.assertTrue(False, f'funktiota pitäisi pystyä kutsumaan seuraavasti viiva(5, "")')

    def test_3_viiva_kunnossa_1(self):
        for koko, merkki in [(5, "-"), (12, "-"), (3, "x"), (14, "x"), (19, "%"), (1, "%"), (5, "XXX"),(19, "<3"), (1, "<3"), (5, ":-)")]:
          with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            output_alussa = get_stdout()
            from src.viiva import viiva
            viiva(koko, merkki)
            output_all = get_stdout().replace(output_alussa, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            if len(merkki)==0:
                merkki = "*"
            self.assertTrue(len(output_all)>0, f'Funktiokutsu viiva({koko}, "{merkki}") ei tulosta mitään')
            acual = '\n'.join(output)
            self.assertEqual(1, len(output), f'Funktiokutsun viiva({koko}, "{merkki}") pitäisi tulostaa vain yksi rivi, nyt se tulostaa {len(output)} riviä, tulostus oli\n{acual}')
            self.assertEqual(merkki[0]*koko, output[0].strip(), f'Funktiokutsun viiva({koko}, "{merkki}") tulostaman rivin pitäisi olla:\n{merkki[0]*koko}\nmutta se on:\n{output[0]}')

    def test_4_viiva_kunnossa_2(self):
        for koko, merkki in [ (3, ""), (5, ""), (12, ""), (14, "")]:
          with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            output_alussa = get_stdout()
            from src.viiva import viiva
            viiva(koko, merkki)
            output_all = get_stdout().replace(output_alussa, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            if len(merkki)==0:
                merkki = "*"
            self.assertTrue(len(output_all)>0, f'Funktiokutsu viiva({koko}, "") ei tulosta mitään')
            acual = '\n'.join(output)
            self.assertEqual(1, len(output), f'Funktiokutsun viiva({koko}, "") pitäisi tulostaa vain yksi rivi, nyt se tulostaa {len(output)} riviä, tulostus oli\n{acual}')
            self.assertEqual(merkki[0]*koko, output[0].strip(), f'Funktiokutsun viiva({koko}, "") tulostaman rivin pitäisi olla:\n{merkki[0]*koko}\nmutta se on:\n{output[0]}')


if __name__ == '__main__':
    unittest.main()