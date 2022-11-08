import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.henkilotunnus_oikein'
function = "onko_validi"

@points('7.henkilotunnus_oikein')
class HeTuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test1_funktio_olemassa(self):
        try:
            from src.henkilotunnus_oikein import onko_validi
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä onko_validi(hetu: str)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.henkilotunnus_oikein import onko_validi
            val = onko_validi("230827-906F")
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == bool, f"Funktion onko_validi pitäisi palauttaa arvo, joka on tyyppiä bool, nyt se palauttaa arvon {val} joka on tyyppiä {taip} kun sitä kutsutaan parametrilla '230827-906F'")
        except:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrien arvoilla ('230827-906F')")

    def test3_import_lause_mukana(self):
        with open("src/henkilotunnus_oikein.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "datetime" in cont , 
                f"Ohjelmassasi ei tuoda datetime-kirjastosta rutiinia käyttöön import-lauseella.")

    def test4_testaa_kelvot(self):
        test_cases = ["080842-720N","110986+713J","200614+561E","050882-437X",
                    "280360+081K","130767-6199","140216+523M","270561-080S",
                    "260168+0989","080283+440C","290531+1054","100400A644E",
                    "160340-670N","140375-767J","200872+5301","200642-4481",
                    "090790+214K","160759-346B","110874+273E","210420-183U",
                    "290103A605T","110705A4064","201106A660L","040705A810M",
                    "030103A493D","280905A4548","290200A1239"]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                onko_validi = load(exercise, function, 'fi')

                try:
                    val = onko_validi(test_case)
                except:
                    self.fail(f"Varmista että funktio toimii parametrin arvolla '{test_case}'")


                self.assertTrue(val, f"Funktio palauttaa arvon '{val}' parametrin arvolla '{test_case}' vaikka henkilötunnus on validi.")

    def test5_testaa_huonot_paivat(self):
        test_cases = ["081842-720N","310286+713J","290200-1239","290200+1239"]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                onko_validi = load(exercise, function, 'fi')

                try:
                    val = onko_validi(test_case)
                except:
                    self.fail(f"Varmista että funktio toimii parametrin arvolla '{test_case}'")

                self.assertFalse(val, f"Funktio palauttaa arvon '{val}' parametrin arvolla '{test_case}' vaikka henkilötunnuksen päivämäärä ei ole validi.")

    def test5_testaa_huonot_tarkastusmerkit(self):
        test_cases = ["081142-720N","310186+713J","230200+1234"]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                onko_validi = load(exercise, function, 'fi')

                try:
                    val = onko_validi(test_case)
                except:
                    self.fail(f"Varmista että funktio toimii parametrin arvolla '{test_case}'")

                self.assertFalse(val, f"Funktio palauttaa arvon '{val}' parametrin arvolla '{test_case}' vaikka henkilötunnuksen tarkastusmerkki ei ole validi.")

    def test6_testaa_vaara_pituus(self):
        test_cases = ["230827-906F1","030103A493DD"]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                onko_validi = load(exercise, function, 'fi')

                try:
                    val = onko_validi(test_case)
                except:
                    self.fail(f"Varmista että funktio toimii parametrin arvolla '{test_case}'")

                self.assertFalse(val, f"Funktio palauttaa arvon '{val}' parametrin arvolla '{test_case}' vaikka henkilötunnuksen pituus on väärä.")

if __name__ == '__main__':
    unittest.main()
