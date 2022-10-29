import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source

exercise = 'src.risunelio'

@points('3.risunelio')
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
            self.module.risunelio(1)
        except:
            self.assertTrue(False, f"Koodistasi puuttuu funktio risunelio tai risunelion suoritus jää ikuiseen silmukkaan\n Kokeile: risunelio(1)")

    def test_nelio_kunnossa(self):
        for koko in [2, 3, 5, 7, 10, 13, 25, 80]:
          with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            output_alussa = get_stdout()
            self.module.risunelio(koko)
            output_all = get_stdout().replace(output_alussa, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            self.assertTrue(len(output_all)>0, f"Funktiokutsu risunelio({koko}) ei tulosta mitään")
            acual = '\n'.join(output)
            self.assertEqual(koko, len(output), f"Funktiokutsun risunelio({koko}) pitäisi tulostaa {koko} riviä, nyt se tulosti {len(output)} riviä, tulostus oli\n{acual}")
            for i in range(koko):
                self.assertEqual("#"*koko, output[i].strip(), f"Funktiokutsun risunelio({koko}) jokaisen rivin pitäisi olla {'#'*koko}, seuraava rivi tulostuu väärin\n{output[i]}\nfunktion koko tulostus oli\n{acual}")

if __name__ == '__main__':
    unittest.main()
