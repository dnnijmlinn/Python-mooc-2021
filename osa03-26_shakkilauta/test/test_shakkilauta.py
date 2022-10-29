import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source, clear_stdout

exercise = 'src.shakkilauta'

@points('3.shakkilauta')
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
            clear_stdout()
            self.module.shakkilauta(2)
        except:
            self.assertTrue(False, f"koodistasi pitäisi löytyä funktio nimeltään shakkilauta jota pystyy kutsumaan seuraavasti shakkilauta(2)")
    
    def test_lauta(self):
        with patch('builtins.input', side_effect=["2"] * 100):
            for koko in range(3, 60):
                reload_module(self.module)
                output_alussa = get_stdout()
                clear_stdout()
                self.module.shakkilauta(koko)
                output_all = get_stdout().replace(output_alussa, '', 1)
                
                output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

                self.assertTrue(len(output_all)>0, f"Funktiokutsu shakkilauta({koko}) ei tulosta mitään")
                acual = '\n'.join(output)
                self.assertEqual(koko, len(output), f"Funktiokutsun shakkilauta({koko}) pitäisi tulostaa {koko} riviä, nyt se tulosti {len(output)} riviä, tulostus oli\n{acual}")
                for i in range(koko):
                    rivi = "10"*koko if i%2==0 else "01"*koko
                    rivi = rivi[0:koko] 
                    self.assertEqual(rivi, output[i].strip(), f"Funktiokutsun shakkilauta({koko}) rivin {i} pitäisi olla {rivi}, nyt se on\n{output[i]}\nfunktion koko tulostus oli\n{acual}")

if __name__ == '__main__':
    unittest.main()
