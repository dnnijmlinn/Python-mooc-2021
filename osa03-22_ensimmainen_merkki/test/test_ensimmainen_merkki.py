import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source

exercise = 'src.ensimmainen_merkki'

@points('3.ensimmainen_merkki')
class EnsimmainenMerkkiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[1] + ["2"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_funktio_olemassa(self):
        with patch('builtins.input', side_effect=["2"] * 10):
            try:
                self.module.ensimmainen("testing...")
            except:
                self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään ensimmainen, jota pystyy kutsumaan seuraavasti:\nensimmainen("testing")')

    def test_merkit_oikein(self):
        for sana in ["python", 'javascript', 'xyz', 'koodari', 'kesäloma', 'nukkumaanmenoaika', 'ohjelmointi', 'aapinen']:
          with patch('builtins.input', side_effect=["2"] * 10):   
            reload_module(self.module)
            output_alussa = get_stdout()
            self.module.ensimmainen(sana)
            output = get_stdout().replace(output_alussa, '', 1).replace('\n', '')
            self.assertTrue(len(output)>0, f'Funktiokutsu ensimmainen("{sana}") ei tulosta mitään')
            self.assertEqual(1, len(output), f'Funktiokutsun ensimmainen("{sana}") pitäisi tulostaa vain yksi merkki, nyt se tulosti {len(output)} merkkiä, tulostus oli\n{output}')
            self.assertEqual(sana[0], output, f'Funktiokutsun ensimmainen("{sana}") pitäisi tulostaa merkki {sana[0]}, tulostus oli\n{output}')

if __name__ == '__main__':
    unittest.main()
