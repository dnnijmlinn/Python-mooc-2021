import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source, clear_stdout

exercise = 'src.keskiarvo'

@points('3.keskiarvo')
class KeskiarvoTest(unittest.TestCase):
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
        with patch('builtins.input', side_effect=["2"] * 10):
            try:
                clear_stdout()
                self.module.keskiarvo(1, 2, 3)
            except:
                self.assertTrue(False, f"koodistasi pitäisi löytyä funktio nimeltään keskiarvo jota pystyy seuraavasti keskiarvo(1,2,3)")

    def test_lasku_oikein(self):
         
        for l1, l2, l3 in [(5, 3, 1), (10, 1, 1), (1,1,2), (-3, 7, 21), (5, 44, 21), (0, 0, 0), (-9, 22, 1021)]:
          with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            output_alussa = get_stdout()
            clear_stdout()
            self.module.keskiarvo(l1, l2, l3)
            output_all = get_stdout().replace(output_alussa, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            inpt = ', '.join(str(i) for i in [l1, l2, l3])

            self.assertTrue(len(output_all)>0, f"Funktiokutsu keskiarvo({inpt}) ei tulosta mitään")
            acual = '\n'.join(output)
            self.assertEqual(1, len(output), f"Funktiokutsun keskiarvo({inpt}) pitäisi tulostaa vain 1 rivi, nyt se tulosti {len(output)} riviä, tulostus oli\n{acual}")
            expctd = (l1+l2+l3) / 3
            try:
                was = float(acual.strip())
            except:
                self.assertFalse(True, f"Funktiokutsun keskiarvo({inpt}) pitäisi tulostaa {expctd}, funktion tulostus\n{acual}\nei ole muutettavissa likukuluvuksi!")
           
            self.assertAlmostEqual(expctd, was, 2, f"Funktiokutsun keskiarvo({inpt}) pitäisi tulostaa {expctd}, nyt se tulosti\n{was}")

if __name__ == '__main__':
    unittest.main()
