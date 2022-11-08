import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.paivakirja'
datafile = 'paivakirja.txt'

def get_correct() -> dict:
    pass

def clear_file():
    with open(datafile, "w"):
        pass

def get_content():
    with open(datafile) as f:
        return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0]

def format(f):
    return "\n".join(f)

@points('6.paivakirja')
class PaivakirjaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_poistu_heti(self):
        syote = "0"
        with patch('builtins.input', side_effect=["0"]):
            reload_module(self.module)
            output = get_stdout()
            correct = "Heippa"

            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
"""
            #\n{mssage}") 

            self.assertFalse(len(output) == 0, f"Syötteellä\n{syote}\nohjelmasi pitäisi tulostaa kaksi riviä, nyt se ei tulosta mitään\n{mssage}") 
            self.assertTrue(len(output.split("\n")) == 2, f"Syötteellä\n{syote}\nohjelmasi pitäisi tulostaa kaksi riviä, nyt tulostus on \n{output}")
            self.assertTrue(correct in output, f"Ohjelman tulisi tulostaa lopuksi {correct}, nyt tulostus on \n{output}")

    def test_2_tyhjenna_lisaa_rivi_ja_poistu(self):
        clear_file()
        with patch('builtins.input', side_effect=["1", "heräsin yhdeksältä", "0"]):
            reload_module(self.module)
            output = get_stdout()
            
            content = get_content()
            correct = ["heräsin yhdeksältä"]
            syote = "\n".join(["1", "heräsin yhdeksältä", "0"])

            self.assertTrue(len(content) > 0, f"Jos tiedosto on aluksi tyhjä, syötteellä\n{syote}\ntiedostossa paivakirja.txt pitäisi olla yksi rivi, tiedoston on kuitenkin tyhjä")
            self.assertTrue(len(content) == len(correct), f"Jos tiedosto on aluksi tyhjä, syötteellä\n{syote}\ntiedostossa paivakirja.txt pitäisi olla yksi rivi, tiedoston sisältö on kuitenkin:\n{format(content)}")
            self.assertEqual(content, correct, f"Jos tiedosto on aluksi tyhjä, syötteellä\n{syote} tiedoston paivakirja.txt sisällön pitäisi olla \n{format(correct)}\nmutta se on \n{format(content)}")

    def test_3_tyhjenna_lisaa_2_rivia_ja_poistu(self):
        clear_file()
        with patch('builtins.input', side_effect=["1", "tänään oli helle", "1", "opin lisää pythonista", "0"]):
            reload_module(self.module)
            output = get_stdout()
            
            syote = "\n".join(["1", "tänään oli helle", "1", "opin lisää pythonista", "0"])

            content = get_content()
            correct = ["tänään oli helle", "opin lisää pythonista"]

            self.assertTrue(len(content) == len(correct), f"Jos tiedosto on aluksi tyhjä, syötteellä\n{syote}\ntiedostossa paivakirja.txt pitäisi olla nyt 2 riviä:\n{format(correct)}\ntiedoston sisältö on kuitenkin:\n{format(content)}")
            self.assertEqual(content, correct, f"Jos tiedosto on aluksi tyhjä, syötteellä\n{syote}\ntiedoston paivakirja.txt sisällön pitäisi olla \n{format(correct)}\nmutta se on \n{format(content)}")

    def test_4_tulosta_sisalto(self):
        with patch('builtins.input', side_effect=["2", "0"]):
            reload_module(self.module)
            output = get_stdout().split("\n")
            output = [x.strip() for x in output if "1 - " not in x and "eippa" not in x and not "erkinn" in x]
            output = [x for x in output if len(x)>0]

            correct = ["tänään oli helle", "opin lisää pythonista"]

            syote1 = "\n".join(["1", "tänään oli helle", "1", "opin lisää pythonista", "0"])
            syote = "\n".join(["2", "0"])

            self.assertTrue(len(output)>0, f"Suorittettaessa ohjelma ensin syötteellä\n{syote1}\nTämän tämän jälkeen ohjelma käynnistetän uudelleen ja suoritetaan syötteellä:\n{syote}\nohjelman tulisi tulostaa merkinnät\n{format(correct)}\nmutta se ei tulosta päiväkirjamerkintöjä")
            self.assertTrue(output == correct, f"Suorittettaessa ohjelma ensin syötteellä\n{syote1}\nja tämän jälkeen syötteellä\n{syote}\nohjelman tulisi tulostaa merkinnät:\n{format(correct)}\nmutta se tulostaa:\n{format(output)}")
    
    def test_5_lisaa_1rivi_peraan_ja_poistu(self):
        with patch('builtins.input', side_effect=["1", "alkaispa jo kesäloma", "0"]):
            reload_module(self.module)
            output = get_stdout().split("\n")
            output = [x.strip() for x in output if "1 - " not in x and "eippa" not in x and not "erkinn" in x]
            output = [x for x in output if len(x)>0]

            content = get_content()
            correct = ["tänään oli helle", "opin lisää pythonista", "alkaispa jo kesäloma"]    

            syote1 = "\n".join(["1", "tänään oli helle", "1", "opin lisää pythonista", "0"])
            syote = "\n".join(["1", "alkaispa jo kesäloma", "0"])

            #self.assertTrue(len(content) == len(correct), f"Suorittettaessa ohjelma ensin syötteellä\n{syote1}\nTämän tämän jälkeen ohjelma käynnistetän uudelleen ja suoritetaan syötteellä:\n{syote}\ntiedostossa paivakirja.txt pitäisi olla nyt 3 riviä:\n{format(correct)}, tiedoston sisältö on kuitenkin:\n{format(content)}")
            #self.assertEqual(output, correct, f"Tiedoston paivakirja.txt sisällön pitäisi olla \n{format(correct)}\nmutta se on:\n{format(content)}")
            #self.assertTrue(output == correct, f"Suorittettaessa ohjelma ensin syötteellä\n{syote1}\nja tämän jälkeen syötteellä\n{syote}\nohjelman tulisi tulostaa merkinnät:\n{format(correct)}\nmutta se tulostaa:\n{format(output)}")

    def test_6_tulosta_sisalto2(self):
        with patch('builtins.input', side_effect=["2", "0"]):
            reload_module(self.module)
            output = get_stdout().split("\n")
            output = [x.strip() for x in output if "1 - " not in x and "eippa" not in x and not "erkinn" in x]
            output = [x for x in output if len(x)>0]

            correct = ["tänään oli helle", "opin lisää pythonista", "alkaispa jo kesäloma"]

            syote1 = "\n".join(["1", "tänään oli helle", "1", "opin lisää pythonista", "0"])
            syote2 = "\n".join(["1", "alkaispa jo kesäloma", "0"])
            syote = "\n".join(["2", "0"])

            self.assertTrue(output == correct, f"Suorittettaessa ohjelma ensin syötteellä\n{syote1}\nsitten syötteellä \n{syote1}\nja tämän jälkeen syötteellä\n{syote}\nohjelman tulisi tulostaa merkinnät:\n{format(correct)}\nmutta se tulostaa:\n{format(output)}")
          
if __name__ == '__main__':
    unittest.main()
