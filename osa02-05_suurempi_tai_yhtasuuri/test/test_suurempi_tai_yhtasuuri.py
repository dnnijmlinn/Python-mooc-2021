import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.suurempi_tai_yhtasuuri'

def format_tuple(d : tuple):
    return f"{d[0]}, {d[1]}"

@points('2.suurempi_tai_yhtasuuri')
class SuurempiYhtasuuriTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['0','0']):
            cls.module = load_module(exercise, 'fi')

    def test_eka_suurempi(self):
        values = [("5","1"), ("100", "0"), ("99","-99"), ("155","154"), ("211","23")]
        for valuepair in values:
            with patch('builtins.input', side_effect = list(valuepair)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")

                self.assertTrue(len(out)>0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(format_tuple(valuepair)))    
            
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä syötteellä {}".format(len(output), format_tuple(valuepair)))
                self.assertTrue(output[0].find(valuepair[0]) > -1, "Tulostuksesta\n{}\nei löydy suurempaa lukua {} kun syöte on {}".format(output[0], valuepair[0], format_tuple(valuepair)))
    
    def test_toka_suurempi(self):
        values = [("0","1"), ("100", "120"), ("-99","99"), ("151","1534"), ("23","211")]
        for valuepair in values:
            with patch('builtins.input', side_effect = list(valuepair)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")

                self.assertTrue(len(out) >0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(format_tuple(valuepair)))    
            
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä syötteellä {}".format(len(output), format_tuple(valuepair)))
                self.assertTrue(output[0].find(valuepair[1]) > -1, "Tulostuksesta\n{}\nei löydy suurempaa lukua {} kun syöte on {}".format(output[0], valuepair[1], format_tuple(valuepair)))

    def test_yhtasuuret(self):
        values = [("1","1"), ("100", "100"), ("-99","-99"), ("0","0")]
        for valuepair in values:
            with patch('builtins.input', side_effect = list(valuepair)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")

                self.assertTrue(len(out) >0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(format_tuple(valuepair)))    
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä syötteellä {}".format(len(output), format_tuple(valuepair)))
                self.assertTrue(output[0].find("yhtä suuret") > -1, "Tulostuksesta\n{}\nei löydy mainintaa 'yhtä suuret' kun syöte on {}".format(output[0], format_tuple(valuepair)))    
   
if __name__ == '__main__':
    unittest.main()
