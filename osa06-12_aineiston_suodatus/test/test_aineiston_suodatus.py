import os
import os.path
import textwrap
import unittest
from functools import reduce
from random import choice, randint
from unittest.mock import patch

from tmc import points
from tmc.utils import (check_source, get_stdout, load, load_module,
                       reload_module)

exercise = 'src.aineiston_suodatus'
function = "suodata_laskut"
datafile1 = 'oikeat.csv'
datafile2 = 'vaarat.csv'

import os
from shutil import copyfile


def get_correct() -> dict:
    pass

def clear_files():
    with open(datafile1, "w"), open(datafile2, "w"):
        pass

def get_content():
    with open(datafile1) as f, open(datafile2) as f2:
        return ([x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0],
               [x.replace("\n","") for x in f2.readlines() if len(x.strip()) > 0]) 

def format(f):
    return "\n".join(f)

def file_exists(f: str):
    try:
        open(f)
        return True
    except:
        return False

def read(fname: str):
    with open(fname) as f:
        return [x.strip() for x in f.readlines() if len(x.strip()) > 0]

@points('6.aineiston_suodatus')
class AineistonSuodatusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            filename = "laskut.csv"
            data_file = os.path.join('src', filename)
            copyfile(data_file, filename)
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
        os.remove("laskut.csv")

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)
    
    def test_1_funktio_olemassa(self):
        try:
            from src.aineiston_suodatus import suodata_laskut
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä suodata_laskut()")

    def test_2_luo_tiedoston_1(self):
        suodata_laskut = load(exercise, function, 'fi')
        suodata_laskut()
        self.assertTrue(file_exists('oikeat.csv'), "Ohjelma ei luo tiedostoa oikeat.csv ollenkaan.")

    def test_3_luo_tiedoston_2(self):
        suodata_laskut = load(exercise, function, 'fi')
        suodata_laskut()
        self.assertTrue(file_exists('vaarat.csv'), "Ohjelma ei luo tiedostoa vaarat.csv ollenkaan.")

    def test_4_testaa_oikeat_pituus(self):
        suodata_laskut = load(exercise, function, 'fi')
        suodata_laskut()

        try:
            content = read("oikeat.csv")
        except: 
            self.assertTrue(False, "Tiedoston oikeat.csv sisällön lukeminen aiheuttaa virheen")

        self.assertEqual(len(content), 42, f"Kun suoritetaan koodi suodata_laskut() tiedostossa oikeat.csv pitäisi olla 42 riviä, nyt siinä on {len(content)} riviä.")

    def test_5_testaa_vaarat_pituus(self):
        suodata_laskut = load(exercise, function, 'fi')
        suodata_laskut()

        try:
            content = read("vaarat.csv")
        except: 
            self.assertTrue(False, "Tiedoston vaarat.csv sisällön lukeminen aiheuttaa virheen")

        self.assertEqual(len(content), 47, f"Kun suoritetaan koodi suodata_laskut() tiedostossa vaarat.csv pitäisi olla 47 riviä, nyt siinä on {len(content)} riviä.")

    def test_6_testaa_oikeat_sisaltoa(self):
        suodata_laskut = load(exercise, function, 'fi')
        suodata_laskut()

        try:
            content = read("oikeat.csv")
        except: 
            self.assertTrue(False, "Tiedoston oikeat.csv sisällön lukeminen aiheuttaa virheen")

        corr = ["Tony;48+66;114","Emilia;23+30;53","Tuula;99-42;57","Arto;26+81;107","Antti;85+38;123","Toni;71-19;52"]
        for c in corr:
            self.assertTrue(c in content, f"Kun suoritetaan koodi suodata_laskut() tiedostosta oikeat.csv pitäisi löytyä rivi {c} mutta sitä ei löydy.")

    def test_7_testaa_vaarat_sisaltoa(self):
        suodata_laskut = load(exercise, function, 'fi')
        suodata_laskut()

        try:
            content = read("vaarat.csv")
        except: 
            self.assertTrue(False, "Tiedoston vaarat.csv sisällön lukeminen aiheuttaa virheen")

        corr = ["Mia;93-27;38","Matti;71-7;74","Matti;80-48;6","Pekka;68-44;22","Erkki;1+90;42","Tuula;61-37;85","Antti;37+64;5","Kirsi;74-47;85"]
        for c in corr:
            self.assertTrue(c in content, f"Kun suoritetaan koodi suodata_laskut() tiedostosta vaarat.csv pitäisi löytyä rivi {c} mutta sitä ei löydy.")
              
if __name__ == '__main__':
    unittest.main()
