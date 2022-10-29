import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.aakkosjarjestyksessa_keskimmainen'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.aakkosjarjestyksessa_keskimmainen')
class AakkosjarjestysKeskimmainenTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['A','B',"C"]):
            cls.module = load_module(exercise, 'fi')

    def test_keski_ekana(self):
        values = ["Y X Z", "B C A", "R U C", "H D N"]
        for letters in values:
            valuegroup = letters.split(" ")
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(valuegroup))

                correct = "Keskimmäinen kirjain on " + sorted(valuegroup)[1]
                
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(correct) > -1, "Tulostus \n{}\nei vastaa oikeaa tulostetta\n{}\nkun syöte on {}".
                    format(output[0], correct, format_tuple(valuegroup)))

    def test_keski_tokana(self):
        values = ["x y z", "c b a", "p d b", "e w y"]
        for letters in values:
            valuegroup = letters.split(" ")
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(valuegroup))

                correct = "Keskimmäinen kirjain on " + sorted(valuegroup)[1]
                
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(correct) > -1, "Tulostus\n{}\nei vastaa oikeaa tulostetta\n{}\nkun syöte on {}".
                    format(output[0], correct, format_tuple(valuegroup)))

    def test_keski_kolmantena(self):
        values = ["X Z Y", "e a c", "l a f", "b x r"]
        for letters in values:
            valuegroup = letters.split(" ")
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(valuegroup))

                correct = "Keskimmäinen kirjain on " + sorted(valuegroup)[1]
                
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(correct) > -1, "Tulostus\n{}\nei vastaa oikeaa tulostetta\n{}\nkun syöte on {}".
                    format(output[0], correct, format_tuple(valuegroup))) 

if __name__ == '__main__':
    unittest.main()
