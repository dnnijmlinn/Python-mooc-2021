import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.lista_kahdesti'

def getcor(values: tuple):
    s = []
    l = []
    for v in values[:-1]:
        l.append(int(v))
        s.append(f"Lista: {l}")
        s.append(f"Järjestettynä: {sorted(l)}")
    return s + ["Moi!"]

@points('4.lista_kahdesti')
class ListaKahdestiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["0"]):
            cls.module = load_module(exercise, 'fi')

    def test_syotteet1(self):
        values = tuple("1 2 3 0".split())
        with patch('builtins.input', side_effect = list(values)):
            reload_module(self.module)
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
                    f"Ohjelmasi tulisi tulostaa rivillä {r} \n{l2} \nmutta nyt se tulostaa \n{l1}\nkun syöte on {values}")
                r += 1

    def test_syotteet2(self):
        values = tuple("9 8 7 0".split())
        with patch('builtins.input', side_effect = list(values)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertTrue(len(output.strip())>0, f"Ohjelmasi ei tulosta mitään kun syöte on {values}")
            self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa syötteiden kysymisen lisäksi {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"Ohjelmasi tulisi tulostaa rivillä {r} \n{l2} \nmutta nyt se tulostaa \n{l1}\nkun syöte on {values}")
                r += 1

    def test_syotteet3(self):
        values = tuple("9 1 8 2 7 3 11 12 22 21 0".split())
        with patch('builtins.input', side_effect = list(values)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertTrue(len(output.strip())>0, f"Ohjelmasi ei tulosta mitään kun syöte on {values}")
            self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa syötteiden kysymisen lisäksi {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"Ohjelmasi tulisi tulostaa rivillä {r} \n{l2} \nmutta nyt se tulostaa \n{12}\nkun syöte on {values}")
                r += 1

if __name__ == '__main__':
    unittest.main()
