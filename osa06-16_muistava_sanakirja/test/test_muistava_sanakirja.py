import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.muistava_sanakirja'
datafile = 'sanakirja.txt'

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

def f(f):
    return "\n".join(f)

@points('6.muistava_sanakirja')
class MuistavaSanakirjaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        clear_file()
        with patch('builtins.input', side_effect=["3"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_poistu_heti(self):
        syote = ["3"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertFalse(True, f"Varmista että ohjelman voi suorittaa syötteellä:\n{f(syote)}")
            output = get_stdout()
            correct = "Moi"
            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
"""
            #\n{mssage}") 
            self.assertTrue(len(output)>0, f"Ohjelmasi pitäisi tulostaa syötteellä:\n{f(syote)}\nkaksi riviä, nyt se ei tulosta mitään\n{mssage}") 
            self.assertTrue(len(output.split("\n")) == 2, f"Ohjelmasi pitäisi tulostaa syötteellä\n{f(syote)} kaksi riviä, nyt tulostus on \n{output}")
            self.assertTrue(correct in output, f"Ohjelman tulisi tulostaa lopuksi {correct}, nyt tulostus on \n{output}")

    def test_2_tyhjenna_lisaa_sanapari_ja_poistu(self):
        clear_file()
        syote = ["1", "auto", "car", "3"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertFalse(True, f"Varmista että ohjelman voi suorittaa syötteellä:\n{f(syote)}")
            output = get_stdout()
            
            correct = "Moi"

            self.assertTrue(len(output.split("\n")) == 4, f"Ohjelmasi pitäisi tulostaa syötteellä:\n{f(syote)}\nneljä riviä, nyt tulostus on \n{output}")
            self.assertTrue(correct in output, f"Ohjelman tulisi tulostaa lopuksi {correct} nyt tulostus on \n{output}")

    def test_3_tyhjenna_lisaa_sanapari_ja_tulosta(self):
        clear_file()
        syote = ["1", "tietokone", "computer", "2", "tietokone", "3"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertFalse(True, f"Varmista että ohjelman voi suorittaa syötteellä:\n{f(syote)}")
            output = get_stdout()
            
            correct = "tietokone - computer"
            self.assertTrue(correct in output, f"Kun syöte on:\n{f(syote)}\nohjelman tulisi tulostaa \n{correct}\nnyt tulostus on \n{output}")

    def test_4b_lataa_uudestaan_ja_tulosta(self):
        syote1 = ["1", "tietokone", "computer", "2", "tietokone", "3"]
        syote = ["2", "tietokone", "3"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertFalse(True, f"Varmista että ohjelman voi suorittaa syötteellä:\n{f(syote)}")
            output = get_stdout()
            
            correct = "tietokone - computer"
            self.assertTrue(correct in output, f"Kun ohjelma on ensin suoritettu syötteellä\n{f(syote1)}\nja sen jälkeen syötteellä:\n{f(syote)}\nohjelman tulisi tulostaa \n{correct}\nnyt tulostus on \n{output}")

    def test_5_lisaa_sanapareja_ja_tulosta(self):
        syote1 = ["1", "tietokone", "computer", "3"]
        syote = ["1", "tieto", "knowledge", "1", "tietoisuus", "conscience", "2", "tieto","3"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertFalse(True, f"Varmista että ohjelman voi suorittaa syötteellä:\n{f(syote)}")
            output = get_stdout()
            
            corrects = ["tietokone - computer", "tieto - knowledge", "tietoisuus - conscience"]
            for correct in corrects:
                self.assertTrue(correct in output, f"Kun ohjelma on ensin suoritettu syötteellä\n{f(syote1)}\nja sen jälkeen syötteellä:\n{f(syote)}\nohjelman tulostuksessa pitäisi olla\n{correct}\nnyt tulostus on \n{output}")

    def test_6_lisaa_sanapareja_ja_tulosta_en(self):
        clear_file()
        syote = ["1", "uida", "swim", "1", "uimari", "swimmer", "1", "uimapuku", "swimsuit", "2", "swim", "3"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertFalse(True, f"Varmista että ohjelman voi suorittaa syötteellä:\n{f(syote)}")
            output = get_stdout()
            
            corrects = ["uida - swim", "uimari - swimmer", "uimapuku - swimsuit"]
            for correct in corrects:
                self.assertTrue(correct in output, f"Kun ohjelma suoritetaan syötteellä:\n{f(syote)}\nohjelman tulostuksessa pitäisi olla mukana rivi\n{correct}\nnyt tulostus on \n{output}")

    def test_7_tulosta_1(self):
        syote1 = ["1", "uida", "swim", "1", "uimari", "swimmer", "1", "uimapuku", "swimsuit", "3"]
        syote = ["2", "swim", "3"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.assertFalse(True, f"Varmista että ohjelman voi suorittaa syötteellä:\n{f(syote)}")
            output = get_stdout()
            
            corrects = ["uida - swim", "uimari - swimmer", "uimapuku - swimsuit"]
            for correct in corrects:
                self.assertTrue(correct in output, f"Kun ohjelma on ensin suoritettu syötteellä\n{f(syote1)}\nja sen jälkeen syötteellä:\n{f(syote)}\nohjelman tulostuksessa pitäisi olla mukana rivi\n{correct}\nnyt tulostus on \n{output}")

if __name__ == '__main__':
    unittest.main()
