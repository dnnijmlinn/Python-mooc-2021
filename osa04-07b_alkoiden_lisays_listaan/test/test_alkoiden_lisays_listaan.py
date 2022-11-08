import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.alkioiden_lisays_listaan'

@points('4.alkoiden_lisays_listaan')
class AlkioidenLisaysListaanTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["1","1"]):
            cls.module = load_module(exercise, 'fi')
   
    def test_syotteet1(self):
        values = (2,100,200)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = str(list(values[1:]))
            self.assertEqual(len(output_list), 1, f"Ohjelmasi tulisi tulostaa syötteiden kysymisen lisäksi 1 rivi, nyt se tulostaa {len(output_list)} riviä kun syöte on: {values}")
            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
            """
            #\n{mssage}")             
            
            self.assertTrue(len(output.strip())>0, f"Ohjelmasi ei tulosta mitään kun syöte on {values}\n{mssage}")  
            self.assertEqual(output.strip(), cor, f"Ohjelmasi tulisi tulostaa \n{cor} \nmutta nyt se tulostaa \n{output}\nkun syöte on {values}")

    def test_syotteet2(self):
        values = (5,55,33,44,22,66)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = str(list(values[1:]))
            self.assertEqual(len(output_list), 1, f"Ohjelmasi tulisi tulostaa syötteiden kysymisen lisäksi 1 rivi, nyt se tulostaa {len(output_list)} riviä kun syöte on: {values}")
            self.assertEqual(output.strip(), cor, f"Ohjelmasi tulisi tulostaa \n{cor} \nmutta nyt se tulostaa \n{output}\n kun syöte on {values}")

    def test_syotteet3(self):
        values = (7,-9,-6,-11,-24,45,23,0)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = str(list(values[1:]))
            self.assertEqual(len(output_list), 1, f"Ohjelmasi tulisi tulostaa syötteiden kysymisen lisäksi 1 rivi, nyt se tulostaa {len(output_list)} riviä kun syöte on: {values}")
            self.assertEqual(output.strip(), cor, f"Ohjelmasi tulisi tulostaa \n{cor} \nmutta nyt se tulostaa \n{output}\n kun syöte on {values}")
    
if __name__ == '__main__':
    unittest.main()
