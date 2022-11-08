import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
import os

exercise = 'src.joulukuusi'

def okuvio(korkeus):
    lines = ["joulukuusi!"]
    for i in range(1, korkeus+1):
        lines.append(" "*(korkeus-i)+"*"*(i*2-1))

    lines.append(" "*(korkeus-1)+"*")
    return lines

@points('4.joulukuusi')
class KuusiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_funktio_olemassa(self):
        try:
            from src.joulukuusi import joulukuusi
        except:
            self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään joulukuusi')
        try:
            from src.joulukuusi import joulukuusi
            joulukuusi(3)
        except:
            self.assertTrue(False, f'Varmista että funktion suoritus onnistuu seuraavasti\njoulukuusi(3)')

    def test_kuvio_kunnossa(self):
        for korkeus in [3, 4, 5, 7, 10, 14, 18, 20, 25, 50]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_alussa = get_stdout()
                from src.joulukuusi import joulukuusi
                joulukuusi(korkeus)
                output_all = get_stdout().replace(output_alussa, '', 1)
                
                output = [l for l in output_all.split("\n") if len(l)>0 ]

                exp = okuvio(korkeus)

                self.assertTrue(len(output_all)>0, f'Funktiokutsu joulukuusi({korkeus}) ei tulosta mitään')
                acual = '\n'.join(output)
                self.assertEqual("joulukuusi!", output[0].rstrip(), f'Funktiokutsun joulukuusi({korkeus}) tulostaman ensimmäisen rivin pitäisi olla:\njoulukuusi!\nmutta se on:\n{output[0]}')
                self.assertEqual(len(exp), len(output), f'Funktiokutsun joulukuusi({korkeus}) pitäisi tulostaa {len(exp)} riviä, nyt se tulostaa {len(output)} riviä, tulostus oli\n{acual}')
                self.assertEqual("joulukuusi!", output[0].rstrip(), f'Funktiokutsun joulukuusi({korkeus}) tulostaman ensimmäisen rivin pitäisi olla:\njoulukuusi!\nmutta se on:\n{output[0]}')
                acual_kuusi = "\n".join(exp)
                for i in range(len(exp)):
                    self.assertEqual(exp[i], output[i].rstrip(), f'Funktiokutsun joulukuusi({korkeus}) tulostaman rivin {i+1} pitäisi olla:\n{exp[i]}\nmutta se on:\n{output[i]}\nOle tarkkana rivin alun väliolyöntien määrän kanssa!\nFunktiosi koko tulostus oli:\n{output_all}\noikeaoppinen joulukuusi:\n{acual_kuusi}')

if __name__ == '__main__':
    unittest.main()
