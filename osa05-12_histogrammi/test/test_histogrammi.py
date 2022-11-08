import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.histogrammi'
function = 'histogrammi'

@points('5.histogrammi')
class VanhinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
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
            from src.histogrammi import histogrammi
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä histogrammi(merkkijono: str)')
    
        try:
            histogrammi = load(exercise, function, 'fi')
            koodi = """histogrammi("abba")"""
            histogrammi("abba")
        except:
            self.assertTrue(False, f'Tarkista että funktiota voi kutsua seuraavasti:\n{koodi}')


    def test_2_abba_toimii(self):
        histogrammi = load(exercise, function, 'fi')
        
        sana = "abba"
        with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            koodi = F'histogrammi("{sana}")'

            output_alussa = get_stdout()

            histogrammi(sana)

            output_all = get_stdout().replace(output_alussa, '', 1)

            output = [l for l in output_all.split("\n") if len(l)>0 ]

            self.assertTrue(len(output_all)>0, f'Funktiokutsu {koodi} ei tulosta mitään')
            exp = ["a **", "b **"]
            self.assertEqual(len(exp), len(output),  f'Funktiokutsun {koodi} pitäisi tulostaa {len(exp)} riviä, se tulosti {len(output)} riviä. Tulostus oli\n{output_all}')
            for rivi in exp:
                self.assertTrue(rivi in output, f'Funktiokutsun {koodi} pitäisi tulostaa rivi \n{rivi}\nSitä ei löytynyt. Tulostus oli\n{output_all}')          

    def test_3_saippia_toimii(self):
        histogrammi = load(exercise, function, 'fi')
        
        sana = "saippua"
        with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            koodi = F'histogrammi("{sana}")'

            output_alussa = get_stdout()

            histogrammi(sana)

            output_all = get_stdout().replace(output_alussa, '', 1)

            output = [l for l in output_all.split("\n") if len(l)>0 ]

            self.assertTrue(len(output_all)>0, f'Funktiokutsu {koodi} ei tulosta mitään')
            exp = [ "s *", "a **", "i *", "p **", "u *" ]
            self.assertEqual(len(exp), len(output),  f'Funktiokutsun {koodi} pitäisi tulostaa {len(exp)} riviä, se tulosti {len(output)} riviä. Tulostus oli\n{output_all}')
            for rivi in exp:
                self.assertTrue(rivi in output, f'Funktiokutsun {koodi} pitäisi tulostaa rivi \n{rivi}\nSitä ei löytynyt. Tulostus oli\n{output_all}')          

    def test_3_histogrammi_toimii(self):
        histogrammi = load(exercise, function, 'fi')
        
        sana = "histogrammi"
        with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            koodi = F'histogrammi("{sana}")'

            output_alussa = get_stdout()

            histogrammi(sana)

            output_all = get_stdout().replace(output_alussa, '', 1)

            output = [l for l in output_all.split("\n") if len(l)>0 ]

            self.assertTrue(len(output_all)>0, f'Funktiokutsu {koodi} ei tulosta mitään')
            exp = """h *
i **
s *
t *
o *
g *
r *
a *
m **""".split('\n')
            self.assertEqual(len(exp), len(output),  f'Funktiokutsun {koodi} pitäisi tulostaa {len(exp)} riviä, se tulosti {len(output)} riviä. Tulostus oli\n{output_all}')
            for rivi in exp:
                self.assertTrue(rivi in output, f'Funktiokutsun {koodi} pitäisi tulostaa rivi \n{rivi}\nSitä ei löytynyt. Tulostus oli\n{output_all}')          


if __name__ == '__main__':
    unittest.main()
