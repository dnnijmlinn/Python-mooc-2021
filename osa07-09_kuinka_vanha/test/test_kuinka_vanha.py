import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from fractions import Fraction

exercise = 'src.kuinka_vanha'

def x(t):
    return "\n"+"\n".join(t)

@points('7.kuinka_vanha')
class KuinkaVanhaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["30","12","1999"]):
           cls.module = load_module(exercise, 'fi')


    def test1_import_lause_mukana(self):
        with open("src/kuinka_vanha.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "datetime" in cont, 
                f"Ohjelmassasi ei tuoda datetime-kirjastoa käyttöön import-lauseella.")

    def test2_testaa_vanhemmilla(self):
        f = Fraction
        test_cases = {("1","1","1900"): "36523", ("10","9","1977"): "8147", ("30","12","1999"): 1, ("6","5","1995"): "1700"}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list(test_case)):
                try:
                    reload_module(self.module)
                except:
                    self.fail(f"Kokeile suorittaa ohjelmasi syötteillä {x(test_case)}")

                output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])
                lines = len(output.split("\n"))
                correct = f"Olit {test_cases[test_case]} päivää vanha"
                msg = 'Huomaa, että tässä ohjelmassa koodia ei tule kirjoittaa if __name__ == "main" -lohkon sisälle.'

                self.assertTrue(lines > 0, f"Ohjelmasi ei tulosta mitään, {msg}")

                self.assertTrue(lines == 1,                     
                    f"Ohjelmasi tulisi tulostaa 1 rivi, nyt se tulostaa {lines} riviä: \n{output}\nkun syöte on {x(test_case)}")

                self.assertTrue(correct in output, 
                    f"Ohjelmasi tulosteesta tulisi löytyä rivi {correct} kun syöte on {x(test_case)}\nnyt tuloste on \n{output}")

    def test3_testaa_nuoremmilla(self):
        f = Fraction
        test_cases = [("1","1","2100"), ("10","9","2019"), ("1","1","2000")]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list(test_case)):
                try:
                    reload_module(self.module)
                except:
                    self.fail(f"Kokeile suorittaa ohjelmasi syötteillä {x(test_case)}")

                output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])
                lines = len(output.split("\n"))
                correct = "Et ollut syntynyt"

                self.assertTrue(lines == 1,                     
                    f"Ohjelmasi tulisi tulostaa 1 rivi, nyt se tulostaa {lines} riviä: \n{output}\nkun syöte on {x(test_case)}")

                self.assertTrue(correct in output, 
                    f"Ohjelmasi tulosteesta tulisi löytyä rivi {correct} kun  syöte on {x(test_case)}\nnyt tuloste on \n{output}")
              
if __name__ == '__main__':
    unittest.main()
