import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.virheelliset_lottonumerot'
function = "suodata_virheelliset"
datafile = "korjatut_numerot.csv"

def clear_files():
    with open(datafile, "w"):
        pass

def get_content():
    with open(datafile) as f:
        return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0]
                
def format(f):
    return "\n".join(f)

def file_exists(f: str):
    try:
        open(f)
        return True
    except:
        return False

filename = "lottonumerot.csv"

import os
from shutil import copyfile

@points('6.virheelliset_lottonumerot')
class VirheellisetLottonumerotTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            data_file = os.path.join('src', filename)
            copyfile(data_file, filename)  
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
         os.remove(filename)

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.virheelliset_lottonumerot import suodata_virheelliset
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä suodata_virheelliset()')
 
    def test_2_luo_tiedoston(self):
        suodata_virheelliset = load(exercise, function, 'fi')
        try:
            suodata_virheelliset()
        except:
            self.assertTrue(False, 'Varmista että pystyt kutsumaan funktiotasi suodata_virheelliset()')
        self.assertTrue(file_exists(datafile), f"Ohjelma ei luo tiedostoa {datafile} ollenkaan.")

    def test_3_oikeaa_sisaltoa(self):
        suodata_laskut = load(exercise, function, 'fi')
        suodata_laskut()

        try:
            content = get_content()
        except: 
            self.assertTrue(False, f"Tiedoston {datafile} sisällön lukeminen aiheuttaa virheen")

        corr = ["viikko 1;17,19,35,23,8,20,36","viikko 4;21,2,22,14,4,28,38","viikko 9;8,13,25,12,33,34,35",
                "viikko 10;29,27,30,13,7,38,26","viikko 11;34,3,7,24,16,20,38","viikko 20;32,28,25,19,4,2,3",
                "viikko 22;10,23,24,33,31,21,2","viikko 23;34,28,14,33,18,6,9","viikko 26;8,17,26,9,28,25,27",
                "viikko 34;11,4,33,17,37,1,8","viikko 36;16,4,12,32,19,34,28",
                "viikko 49;31,22,11,6,33,38,35","viikko 50;35,5,7,24,8,22,21"]
        for c in corr:
            self.assertTrue(c in content, f"Tiedostosta {datafile} pitäisi löytyä rivi {c} mutta sitä ei löydy.")

    def test_4_vaaraa_sisaltoa(self):
        suodata_laskut = load(exercise, function, 'fi')
        suodata_laskut()
        try:
            content = get_content()
        except: 
            self.assertTrue(False, f"Tiedoston {datafile} sisällön lukeminen aiheuttaa virheen")

        corr = ["viikko x;23,29,38,1,35,18,25","viikko 8;32,21,26,1,15aa,14,17","viikko 1a5;17,8,38,18,9,32,25",
                    "viikko 21;25,8,18,33,13,11","viikko xx24;37,8,25,30,23,24,19","viikko 27;11,1,Ccy,31,9,20,24",
                    "viikko rrrsas;29,20,19,5,26,11,36","viikko **.';32,25,36,28,21,15,9",
                    "viikko cca:mC;12,32,30,28,4,16,20","viikko 51;rxXX,17,20,27,11,30,5",
                    "viikko 52;29,26,11,21,20,29,5", "viikko 31;6,38,4,-26,32,24,34", "viikko 25;2,25,27,310,8,7,4"]
        for c in corr:
            self.assertFalse(c in content, f"Tiedostosta {datafile} ei pitäisi löytyä virheellistä riviä {c}.")


    def test_5_testaa_tiedoston_pituus(self):
        suodata_virheelliset = load(exercise, function, 'fi')
        suodata_virheelliset()

        try:
            content = get_content()
        except: 
            self.assertTrue(False, f"Tiedoston {datafile} sisällön lukeminen aiheuttaa virheen")

        self.assertEqual(len(content), 37, f"Tiedostossa {datafile} pitäisi olla 37 riviä, nyt siinä on {len(content)} riviä.")


if __name__ == '__main__':
    unittest.main()
