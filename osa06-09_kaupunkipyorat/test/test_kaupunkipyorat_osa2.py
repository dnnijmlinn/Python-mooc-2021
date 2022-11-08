import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.kaupunkipyorat'

def f(d):
    return '\n'.join(d)

function1 = "hae_asematiedot"
function2 = "suurin_etaisyys"

import os
from shutil import copyfile

testdata = [f"stations{i}.csv" for i in range(1,10)]

def close(a, b):
   return abs(a-b)<0.001

@points('6.kaupunkipyorat_osa2')
class KaupunkipyoratOsa2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)  
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_1_suurin_etaisyys_funktio_olemassa(self):
        try:
            from src.kaupunkipyorat import suurin_etaisyys
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä suurin_etaisyys(asemat: dict)')
       
        try:
            koodi = """asemat = hae_asematiedot("stations1.csv")
suurin_etaisyys(asemat)"""
            hae_asematiedot = load(exercise, function1, 'fi')
            asemat = hae_asematiedot("stations1.csv")
            val = suurin_etaisyys(asemat)

        except Exception as ioe:
            self.assertTrue(False, f'Funktiokutsu {koodi} aiheutti virheen')

    def test_2_suurin_etaisyys_paluuarvon_tyyppi(self):
        koodi = """asemat = hae_asematiedot("stations1.csv")
suurin_etaisyys(asemat)"""
        hae_asematiedot = load(exercise, function1, 'fi')
        suurin_etaisyys = load(exercise, function2, 'fi')
        asemat = hae_asematiedot("stations1.csv")
        val = suurin_etaisyys(asemat)

        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == tuple, f"Funktion {function2} pitäisi palauttaa tuple nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")
        taip = str(type(val[0])).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val[0]) == str, f"Funktion {function2} palauttaman tuplen ensimmäisen arvon pitäisi olla tyypiltään merkkijono, nyt se on tyyypiä {taip}\npaluuarvo oli {val}")
        taip = str(type(val[1])).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val[1]) == str, f"Funktion {function2} palauttaman tuplen ensimmäisen arvon pitäisi olla tyypiltään merkkijono, nyt se on tyyypiä {taip}\npaluuarvo oli {val}")
        taip = str(type(val[2])).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val[2]) == float or type(val[2]) == int , f"Funktion {function2} palauttaman tuplen ensimmäisen arvon pitäisi olla tyypiltään float, nyt se on tyyypiä {taip}\npaluuarvo oli {val}")

    def test_3_suurin_etaisuus_1(self):
        for tiedosto, vast in [
            ("stations1.csv", ("Laivasillankatu", "Hietalahdentori", 1.478708873076181)),
            ("stations2.csv", ("Puistokaari", "Karhulantie", 14.817410024304905)),
            ("stations3.csv", ("Puotinkylan kartano", "Friisilanaukio", 21.971314423058754)),
            ("stations4.csv", ("Kaivopuisto", "Linnuntie", 11.569340603194116)),
            ("stations5.csv", ("Puotinkylan kartano", "Etuniementie", 21.8490934564622)),
            ("stations6.csv", ("Karhulantie", "Haukilahdenranta", 19.566890288851994)),
            ("stations7.csv", ("Karhulantie", "Tiistinkallio", 21.848686409979116)),
            ("stations8.csv", ("Puotinkylan kartano", "Etuniementie", 21.8490934564622)),
            ("stations9.csv", ("Voikukantie", "Friisilanaukio", 20.834906297083204)),
        ]:
            koodi = f'asemat = hae_asematiedot("{tiedosto}")\nsuurin_etaisyys(asemat)'
            hae_asematiedot = load(exercise, function1, 'fi')
            suurin_etaisyys = load(exercise, function2, 'fi')
            asemat = hae_asematiedot(tiedosto)
            a1, a2, et = suurin_etaisyys(asemat)
            pal = (a1, a2, et)
            ma1, ma2, met = vast

            self.assertTrue((a1 == ma1 and a2 == ma2) or (a2 == ma1 and a1 == ma2), f'Vastaus on väärä kun suoritetaan koodi\n{koodi}\nKauimpana toisistaan olevat asemat ovat {ma1} ja {ma2}\nfunktiosi palautti {pal}')
            self.assertTrue(close(et, met), f'Vastaus on väärä kun suoritetaan koodi\n{koodi}\nKauimpien etäisuus on {met}\nfunktiosi palautti {pal}')

if __name__ == '__main__':
    unittest.main()
