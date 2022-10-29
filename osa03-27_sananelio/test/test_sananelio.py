import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source, clear_stdout
from functools import reduce
import textwrap

exercise = 'src.sananelio'

@points('3.sananelio')
class RisunelioTest(unittest.TestCase):
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
        
    def test_funktio_olemassa(self):
        try:
            self.module.nelio("", 0)
        except:
            self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään nelio')
        try:
            clear_stdout()
            self.module.nelio("ab", 2)
        except:
            self.assertTrue(False, f'Varmista että seuraava onnistuu\nnelio("ab", 3)')

    def test_nelio(self):
        for sana, koko in [("ab", 3), ("abc", 5), ("python", 15), ('qwerty', 37), ('123456789', 100)]:
            with patch('builtins.input', side_effect=["2"] * 100):
                reload_module(self.module)
                output_alussa = get_stdout()
                clear_stdout()
                try:
                    self.module.nelio(sana, koko)
                except:
                    self.assertTrue(False, f'Varmista että seuraava onnistuu\nnelio("{sana}", {koko})')

                output_all = get_stdout().replace(output_alussa, '', 1)
                
                output = [l for l in output_all.split("\n") if len(l.strip())>0 ]
                rivit = textwrap.wrap(sana*(koko*koko), koko)[0:koko]

                self.assertTrue(len(output_all)>0, f'Funktiokutsu  nelio("{sana}", {koko}) ei tulosta mitään')
                acual = '\n'.join(output)
                self.assertEqual(len(rivit), len(output), f'Funktiokutsun  nelio("{sana}", {koko}) pitäisi tulostaa {koko} riviä, nyt se tulosti {len(output)} riviä, tulostus oli\n{acual}')
                
                for i in range(koko):
                    self.assertEqual(rivit[i], output[i].strip(), f'Funktiokutsun nelio("{sana}", {koko}) rivin {i} tulostuksen pitäisi olla {rivit[i]}, nyt se on\n{output[i]}\nfunktion koko tulostus oli\n{acual}')

if __name__ == '__main__':
    unittest.main()
