import unittest
from unittest.mock import patch, MagicMock

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint
import json

exercise = 'src.kurssistatistiikka'

class Mok:
    def __init__(self, n):
        self.n = n
        fail = "test/data/courses.json" if n==1 else "test/data/courses2.json"
        with open(fail) as f:
            self.s = f.read()

    def read(self):
        return self.s

class MokCourse:
    def __init__(self, n):
        with open(f"test/data/{n}.json" ) as f:
            self.s = f.read()

    def read(self):
        return self.s

@points('7.kurssistatistiikka_osa2')
class KurssiStatistiikkaOsa2Test(unittest.TestCase):

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

    def test1_funktio_hae_kurssi_olemassa(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("docker2019")]):
            try:
                from src.kurssistatistiikka import hae_kurssi
            except:
                self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio hae_kurssi(kurssi: str)')
            
            try:
                vastaus = hae_kurssi("docker2019")
            except:
                self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu hae_kurssi("docker2019")')

            self.assertTrue(type(vastaus) == dict, f'Funktiokutsun hae_kurssi("docker2019") pitää palauttaa dict, se palautti nyt arvon {vastaus}')

    def test2_funktio_hae_kurssi_toimii_1(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("docker2019")]):
            from src.kurssistatistiikka import hae_kurssi
            
            koodi = 'hae_kurssi("docker2019")'
            odotettu = {'viikkoja': 4, 'opiskelijoita': 220, 'tunteja': 5966, 'tunteja_keskimaarin': 27, 'tehtavia': 4988, 'tehtavia_keskimaarin': 22}
            try:
                vastaus = hae_kurssi("docker2019")
            except:
                self.assertEqual(odotettu.keys(), vastaus.keys(), f'Funktiokutsun {koodi} aiheuttaa virheen')        

            self.assertEqual(odotettu.keys(), vastaus.keys(), f'Funktiokutsun {koodi}, pitäisi palauttaa sanakirja jossa on avaimet {odotettu.keys()}.\nFunktio palauttaa\n{vastaus}')        

            for k, v in odotettu.items():
                self.assertEqual(vastaus[k], v, f'Funktiokutsun {koodi} vastaukssa pitäisi avaimen {k} arvona olla {v}, arvo on kuitenkin {vastaus[k]}\nFunktio palauttaa\n{vastaus}')        

    def test2_funktio_hae_kurssi_toimii_2(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("CCFUN")]):
            from src.kurssistatistiikka import hae_kurssi
            
            odotettu = {'viikkoja': 9, 'opiskelijoita': 59, 'tunteja': 1687, 'tunteja_keskimaarin': 28, 'tehtavia': 951, 'tehtavia_keskimaarin': 16}
            koodi = 'hae_kurssi("CCFUN")'

            try:
                vastaus = hae_kurssi("CCFUN")
            except:
                self.assertFalse(True, f'Funktiokutsun {koodi} aiheuttaa virheen')    

            self.assertEqual(odotettu.keys(), vastaus.keys(), f'Funktiokutsun {koodi}, pitäisi palauttaa sanakirja jossa on avaimet {odotettu.keys()}.\nFunktio palauttaa\n{vastaus}')        

            for k, v in odotettu.items():
                self.assertEqual(vastaus[k], v, f'Funktiokutsun {koodi} vastaukssa pitäisi avaimen {k} arvona olla {v}, arvo on kuitenkin {vastaus[k]}\nFunktio palauttaa\n{vastaus}')        

    def test2_funktio_hae_kurssi_toimii_3(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("ohtus17")]):
            from src.kurssistatistiikka import hae_kurssi
            
            odotettu = {'viikkoja': 7, 'opiskelijoita': 96, 'tunteja': 2977, 'tunteja_keskimaarin': 31, 'tehtavia': 5381, 'tehtavia_keskimaarin': 56}
            koodi = 'hae_kurssi("ohtus17")'

            try:
                vastaus = hae_kurssi("ohtus17")
            except:
                self.assertFalse(True, f'Funktiokutsun {koodi} aiheuttaa virheen')    

            self.assertEqual(odotettu.keys(), vastaus.keys(), f'Funktiokutsun {koodi}, pitäisi palauttaa sanakirja jossa on avaimet {odotettu.keys()}.\nFunktio palauttaa\n{vastaus}')        

            for k, v in odotettu.items():
                self.assertEqual(vastaus[k], v, f'Funktiokutsun {koodi} vastaukssa pitäisi avaimen {k} arvona olla {v}, arvo on kuitenkin {vastaus[k]}\nFunktio palauttaa\n{vastaus}')        

    def test2_funktio_hae_kurssi_toimii_4(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("ofs")]):
            from src.kurssistatistiikka import hae_kurssi
           
            odotettu = {'viikkoja': 9, 'opiskelijoita': 542, 'tunteja': 28116, 'tunteja_keskimaarin': 51, 'tehtavia': 31746, 'tehtavia_keskimaarin': 58}
            koodi = 'hae_kurssi("ofs")'
            try:
                 vastaus = hae_kurssi("ofs")
            except:
                self.assertFalse(True, f'Funktiokutsun {koodi} aiheuttaa virheen')    

            self.assertEqual(odotettu.keys(), vastaus.keys(), f'Funktiokutsun {koodi}, pitäisi palauttaa sanakirja jossa on avaimet {odotettu.keys()}.\nFunktio palauttaa\n{vastaus}')        

            for k, v in odotettu.items():
                self.assertEqual(vastaus[k], v, f'Funktiokutsun {koodi} vastaukssa pitäisi avaimen {k} arvona olla {v}, arvo on kuitenkin {vastaus[k]}\nFunktio palauttaa\n{vastaus}')        

    def test2_funktio_hae_kurssi_toimii_5(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("ofs2019")]):
            from src.kurssistatistiikka import hae_kurssi
            
            odotettu = {'viikkoja': 11, 'opiskelijoita': 4441, 'tunteja': 201752, 'tunteja_keskimaarin': 45, 'tehtavia': 238712, 'tehtavia_keskimaarin': 53}
            koodi = 'hae_kurssi("ofs2019")'
            try:
                 vastaus = hae_kurssi("ofs2019")
            except:
                self.assertFalse(True, f'Funktiokutsun {koodi} aiheuttaa virheen')   

            self.assertEqual(odotettu.keys(), vastaus.keys(), f'Funktiokutsun {koodi}, pitäisi palauttaa sanakirja jossa on avaimet {odotettu.keys()}.\nFunktio palauttaa\n{vastaus}')        

            for k, v in odotettu.items():
                self.assertEqual(vastaus[k], v, f'Funktiokutsun {koodi} vastaukssa pitäisi avaimen {k} arvona olla {v}, arvo on kuitenkin {vastaus[k]}\nFunktio palauttaa\n{vastaus}')        

if __name__ == '__main__':
    unittest.main()
