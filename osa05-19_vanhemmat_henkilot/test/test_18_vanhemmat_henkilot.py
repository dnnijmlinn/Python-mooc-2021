import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.vanhemmat_henkilot'
function = 'vanhemmat'


@points('5.vanhemmat_henkilot')
class VanhinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.vanhemmat_henkilot import vanhemmat
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä vanhemmat(henkilot: list, vuosi: int)')
        try:
            vanhemmat = load(exercise, function, 'fi')
            koodi = """hlista = [("Arto", 1977), ("Milla", 2014)]
vanhemmat(hlista, 2000)"""

            hlista = [("Arto", 1977), ("Milla", 2014)]
            vanhemmat(hlista, 2000)

        except:
            self.assertTrue(False, f'Varmista että funktiotasi voidaan kutsua seuraavasti:\n{koodi}')

    def test_2_paluuarvon_tyyppi(self):
        vanhemmat = load(exercise, function, 'fi')
        koodi = """hlista = [("Arto", 1977), ("Milla", 2014)]
vastaus = vanhemmat(hlista, 2000)"""

        hlista = [("Arto", 1977), ("Milla", 2014)]
        vastaus = vanhemmat(hlista, 2000)

        self.assertTrue(type(vastaus) == list, f"Funktio {function} ei palauta listaa kun suoritetaan koodi:\n{koodi}")

    def test_3_toiminnallisuus(self):
        vanhemmat = load(exercise, function, 'fi')
        for hlista in [ 
                [("Arto", 1977), ("Milla", 2014)],
                [("Milla", 2014), ("Arto", 1977)],
                [("Milla", 2014), ("Arto", 1977), ("Einari", 1985),  ("Maija", 1953), ("Essi", 1997)],
                [("Leevi", 2016), ("Elias", 2019), ("Eero", 2012),  ("Venla", 2013), ("Jane Doe", 2020)],
                [("Donald", 1982), ("Daisy", 1892), ("Angela", 1965),  ("Vladimir", 2000), ("Dunja", 1919), ("Tellervo", 1921)]
            ]:

            for vuosi in [2010, 2000, 1990, 1980, 1970, 1950, 1900]:

                koodi = f"hlista = {hlista}\n"+f"vastaus = vanhemmat(hlista, {vuosi})"
                vastaus = vanhemmat(hlista, vuosi)
                oikea = [ n for n, i in hlista if i < vuosi]

                self.assertEqual(vastaus, oikea, f"Funktino {function} palauttama {vastaus} on väärin, sen pitäisi palauttaa {oikea} kun suoritetaan koodi\n{koodi}")

if __name__ == '__main__':
    unittest.main()
