import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.vanhempi'

def format_tuple(d : tuple):
    return '\n'.join(list(d))
    
def p(a):
    return "\n".join(a)

@points('2.vanhempi')
class VanhempiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['0','0','0','0']):
            cls.module = load_module(exercise, 'fi')

    def test_eka_vanhempi(self):
        values = [("Jarmo","20","Aino","19"), ("Paula","29","Pate","16"), ("Mikko","54","Maija","49"), ("Anna","23","Maija","9")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                try:
                    reload_module(self.module)
                except:
                    self.assertTrue(False, f"Varmista että ohjelmasi toimii syötteellä\n{format_tuple(valuegroup)}")
                    pass

                # Poista otsikot
                out = [x for x in get_stdout().split("\n") if len(x)>0 ]
                output = [x for x in out if not x.startswith("Henkil") ]

                self.assertFalse(len(output) == 0, "Ohjelmasi ei tulosta mitän syötteellä:\n{}".
                    format(format_tuple(valuegroup)))
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa kyselyjen jälkeen yhden rivin sijasta {} riviä: {} syötteellä:\n{}".
                    format(len(output), p(output), format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[0]) > -1, "Tulostuksesta\n{}\nei löydy vanhemman henkilön nimeä {} kun syöte on:\n{}".
                    format(output[0], valuegroup[0], format_tuple(valuegroup)))
                self.assertFalse(output[0].find(valuegroup[2]) > -1, "Tulostuksesta\n{}\löytyi nuoremman henkilön nimi {} kun syöte on\n{}".
                    format(output[0], valuegroup[2], format_tuple(valuegroup)))

    def test_toka_vanhempi(self):
        values = [("Leena","20","Petri","39"), ("Simo","29","Antero","46"), ("Alma","1","Maarit","49"), ("Maija","9","Anna","23")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Poista otsikot
                out = [x for x in get_stdout().split("\n") if len(x)>0 ]
                output = [x for x in out if not x.startswith("Henkil") ] 

                self.assertFalse(len(output) == 0, "Ohjelmasi ei tulosta mitän syötteellä:\n{}".
                    format(format_tuple(valuegroup)))
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa kyselyjen jälkeen yhden rivin sijasta {} riviä: {} syötteellä:\n{}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[2]) > -1, "Tulostuksesta\n{}\nei löydy vanhemman henkilön nimeä {} kun syöte on:\n{}".
                    format(output[0], valuegroup[2], format_tuple(valuegroup)))
                self.assertFalse(output[0].find(valuegroup[0]) > -1, "Tulostuksesta\n{}\mlöytyi nuoremman henkilön nimi {} kun syöte on:\n{}".
                    format(output[0], valuegroup[0], format_tuple(valuegroup)))

    def test_yhta_vanhat(self):
        values = [("Lasse","20","Petri","20"), ("Simeon","11","Li","11")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Poista otsikot
                out = [x for x in get_stdout().split("\n") if len(x)>0 ]
                output = [x for x in out if not x.startswith("Henkil") ]
                
                self.assertFalse(len(output) == 0, "Ohjelmasi ei tulosta mitän syötteellä:\n{}".
                    format(format_tuple(valuegroup)))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa kyselyjen jälkeen yhden rivin sijasta {} riviä: {} syötteellä:\n{}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[0]) > -1, "Tulostuksesta\n{}\nei löydy nimeä {} kun syöte on:\n{}".
                    format(output[0], valuegroup[0], format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[2]) > -1, "Tulostuksesta\n{}\nei löydy nimeä {} kun syöte on:\n{}".
                    format(output[0], valuegroup[2], format_tuple(valuegroup)))
                self.assertTrue(output[0].find("yhtä vanhoja") > -1, "Tulostuksesta\n{}\nei löydy mainintaa 'yhtä vanhoja'".format(output[0]))
        
if __name__ == '__main__':
    unittest.main()
