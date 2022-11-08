import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.lisays_ja_poisto'

def getcor(values: tuple):
    s = []
    l = []
    for v in values:
        s.append(f"Lista on nyt {l}")
        if v == "l":
            l.append(len(l) + 1)
        elif v == "p":
            l.pop(len(l) - 1)
        else:
            s.append("Moi!")
    return s

@points('4.lisays_ja_poisto')
class LisaysJaPoistoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["x"]):
            cls.module = load_module(exercise, 'fi')

    def test_syotteet1(self):
        values = tuple("l l l x".split())
        with patch('builtins.input', side_effect = list(values)):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista että ohjelmasi toimii kun syöte on {values}")                
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)

            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
            """
            #\n{mssage}")     
            self.assertTrue(len(output.strip())>0, f"Ohjelmasi ei tulosta mitään kun syöte on {values}\n{mssage}")   
            self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa syötteiden kysymisen lisäksi {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"Ohjelmasi tulisi tulostaa rivillä {r} \n{l2}\nmutta nyt se tulostaa \n{l1}\nkun syöte on {values}")
                r += 1

    def test_syotteet2(self):
        values = tuple("l p l l l p p x".split())
        with patch('builtins.input', side_effect = list(values)):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista että ohjelmasi toimii kun syöte on {values}")      
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa syötteiden kysymisen lisäksi {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"Ohjelmasi tulisi tulostaa rivillä {r} \n{l2}\nmutta nyt se tulostaa \n{l1}\nkun syöte on {values}")
                r += 1

    def test_syotteet3(self):
        values = tuple("l l l l l p l p l x".split())
        with patch('builtins.input', side_effect = list(values)):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Varmista että ohjelmasi toimii kun syöte on {values}")      
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa syötteiden kysymisen lisäksi {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"Ohjelmasi tulisi tulostaa rivillä {r} \n{l2}\nmutta nyt se tulostaa \n{l1}\nkun syöte on {values}")
                r += 1

if __name__ == '__main__':
    unittest.main()
