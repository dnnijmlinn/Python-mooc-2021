import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source, clear_stdout

exercise = 'src.monta_tulostusta'

@points('3.monta_tulostusta')
class MontaTulostustaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["koe","2"]):
           cls.module = load_module(exercise, 'fi')
           
    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_funktio_olemassa(self):
        with patch('builtins.input', side_effect=[AssertionError("tässä tehtävässä ei odotettu syötteen lukemista")]):
            try:
                clear_stdout()
                self.module.tulosta_monesti("testi",2)
            except:
                self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään tulosta_monesti jota pystyy kutsumaan seuraavasti tulosta_monesti("testi", 2)')

    def test_tulostukset_kunnossa(self):
        test_data = [
            ("testi", 2), ("python", 7), ("suo kuokka ja jussi", 4),  ("martti luther ja muovipussi", 12),
            ("koodistasi pitäisi löytyä funktio", 10), ("viimeinen testi", 20)
        ]

        for mj, lkm in test_data:
          with patch('builtins.input', side_effect=[AssertionError("tässä tehtävässä ei odotettu syötteen lukemista")]):
            reload_module(self.module)
            output_alussa = get_stdout()
            clear_stdout()
            self.module.tulosta_monesti( mj, lkm)
            output_all = get_stdout().replace(output_alussa, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            self.assertTrue(len(output_all)>0, f'Funktiokutsu monta_tulostusta("{mj}", {lkm}) ei tulosta mitään')
            acual = '\n'.join(output)
            self.assertEqual(lkm, len(output), f'Funktiokutsun monta_tulostusta("{mj}", {lkm}) pitäisi tulostaa {lkm} riviä, nyt se tulosti {len(output)} riviä, tulostus oli\n{acual}')
            for i in range(lkm):
                self.assertEqual(mj, output[i].strip(), f'Funktiokutsun monta_tulostusta("{mj}", {lkm}) jokaisen tulostusrivin pitäisi olla {mj}, seuraava rivi tulostuu väärin:\n{output[i]}\nfunktion koko tulostus oli:\n{acual}')

if __name__ == '__main__':
    unittest.main()
