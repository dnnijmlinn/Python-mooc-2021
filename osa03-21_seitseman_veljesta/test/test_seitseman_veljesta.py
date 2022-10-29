import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, get_stdout, check_source, clear_stdout

exercise = 'src.seitseman_veljesta'

@points('3.seitseman_veljesta')
class SeitsemanoTest(unittest.TestCase):
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
        try:
            clear_stdout()
            self.module.seitseman_veljesta()
        except:
            self.assertTrue(False, f"koodistasi pitäisi löytyä funktio nimeltään seitseman_veljesta jota pystyy kutsumaan seuraavasti:\nseitseman_veljesta()")

    def test_seitseman(self):
        veljekset = [
            "Aapo",
            "Eero",
            "Juhani",
            "Lauri",
            "Simeoni",
            "Timo",
            "Tuomas"
        ]
        clear_stdout()
        self.module.seitseman_veljesta()
        output_all = get_stdout()
        output = output_all.split('\n')
        self.assertTrue(len(output_all)>0, f"Funktion seitseman_veljesta kutsuminen ei tulosta mitään")
        self.assertEqual(7, len(output), f"Funktion seitseman_veljesta kutsumisen pitäisi tulostaa 7 riviä, nyt se tulosti {len(output)} riviä, tulostus oli\n{output_all}")
        for i in range(7):
             self.assertEqual(veljekset[i], output[i].strip(), f"Funktion seitseman_veljesta kutsumisen rivin {i+1} tulostuksen pitäisi olla\n{veljekset[i]}\ntulostus oli\n{output[i]}")

if __name__ == '__main__':
    unittest.main()
