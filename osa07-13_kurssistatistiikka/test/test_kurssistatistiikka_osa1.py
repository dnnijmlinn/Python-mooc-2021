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

@points('7.kurssistatistiikka_osa1')
class KurssiStatistiikkaOsa1Test(unittest.TestCase):

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

    def test0c_pyynto_ei_withissa(self):
        src_file = os.path.join('src', 'kurssistatistiikka.py')
        with open(src_file) as f:
            for line in f:
                if "request.urlopen(" in line and "with" in line :
                    self.assertTrue(False, f"Testit eivät toimi jos kutsut request.urlopen with-komennon sisällä, seuraava rivi siis on syytä muuttaa \n{line}")

    def test1_funktio_hae_kaikki_olemassa(self):
        with patch('urllib.request.urlopen', side_effect=[Mok(1)]):
            try:
                from src.kurssistatistiikka import hae_kaikki
            except:
                self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä hae_kaikki()')
            
            try:
                vastaus = hae_kaikki()
            except:
                self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu hae_kaikki()')

            self.assertTrue(type(vastaus) == list, f'Funktiokutsun hae_kaikki() pitää palauttaa list, se palautti nyt arvon {vastaus}')
            self.assertTrue(len(vastaus)>0, f'Funktiokutsun hae_kaikki() pitää palauttaa epätyhjä lista, se palautti nyt arvon {vastaus}')
            self.assertTrue(type(vastaus[0]) == tuple, f'Funktiokutsun hae_kaikki() palauttamalla listalla pitäisi olla tupleja. Funktio palautti nyt arvon {vastaus}')
            self.assertTrue(len(vastaus[0]) == 4, f'Funktiokutsun hae_kaikki() palauttamalla listalla pitäisi olla tupleja, joissa on neljä arvoa. Funktio palautti nyt arvon {vastaus}')
            self.assertTrue(type(vastaus[0][0]) == str, f'Funktiokutsun hae_kaikki() palauttamalla listalla pitäisi olla tupleja joiden ensimmäinen arvo on merkkijono. Funktio palautti nyt arvon {vastaus}')
            self.assertTrue(type(vastaus[0][1]) == str, f'Funktiokutsun hae_kaikki() palauttamalla listalla pitäisi olla tupleja joiden toinen arvo on merkkijono. Funktio palautti nyt arvon {vastaus}')
            self.assertTrue(type(vastaus[0][2]) == int, f'Funktiokutsun hae_kaikki() palauttamalla listalla pitäisi olla tupleja joiden kolmas arvo on kokonaisluku. Funktio palautti nyt arvon {vastaus}')
            self.assertTrue(type(vastaus[0][3]) == int, f'Funktiokutsun hae_kaikki() palauttamalla listalla pitäisi olla tupleja joiden neljäs arvo on kokonaisluku. Funktio palautti nyt arvon {vastaus}')

    def test2_funktio_hae_kaikki_toimii(self):
        with patch('urllib.request.urlopen', side_effect=[Mok(1)]):
            from src.kurssistatistiikka import hae_kaikki
            vastaus = hae_kaikki()
            odotettu = [('Full Stack Open 2020', 'ofs2019', 2020, 201), ('DevOps with Docker 2019', 'docker2019', 2019, 36), ('DevOps with Docker 2020', 'docker2020', 2020, 36), ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)]

            self.assertEqual(len(odotettu), len(vastaus), f'Funktiokutsun hae_kaikki(), pitäisi palauttaa lista jonka pituus on {len(odotettu)} se palautti listan jonka pituus on {len(vastaus)}. Palautettu lista on\n{vastaus}')        

            for r in odotettu:
                self.assertTrue(r in vastaus, f'Funktiokutsun hae_kaikki() vastauksessa pitäisi olla mukana tuple {r}. Palautettu lista on\n{vastaus}')        

            for r in vastaus:
                self.assertTrue(r in odotettu, f'Funktiokutsun hae_kaikki() vastauksessa pitäisi olla mukana tuple {r}. Palautettu lista on\n{vastaus}')        

    def test3_funktio_hae_kaikki_toimii_muullakin_datalla(self):
        with patch('urllib.request.urlopen', side_effect=[Mok(2)]):
            from src.kurssistatistiikka import hae_kaikki
            vastaus = hae_kaikki()
            odotettu = [('Cloud Computing Fundamentals', 'CCFUN', 2019, 27), ('Full Stack Open 2020', 'ofs2019', 2020, 201), ('DevOps with Docker 2018', 'docker2018', 2018, 36), ('DevOps with Docker 2020', 'docker2020', 2020, 54)]

            self.assertEqual(len(odotettu), len(vastaus), f'Et kai ole kovakoodannut vastauksia? Käytettäessä vaihtoehtoista datalähdettä funktiokutsun hae_kaikki(), pitäisi palauttaa lista jonka pituus on {len(odotettu)} se palautti listan jonka pituus on {len(vastaus)}. Palautettu lista on\n{vastaus}')        

            for r in odotettu:
                self.assertTrue(r in vastaus, f'Et kai ole kovakoodannut vastauksia? Käytettäessä vaihtoehtoista datalähdettä fuuktiokutsun hae_kaikki() vastauksessa pitäisi olla mukana tuple {r}. Palautettu lista on\n{vastaus}')        

            for r in vastaus:
                self.assertTrue(r in odotettu, f'Et kai ole kovakoodannut vastauksia? Käytettäessä vaihtoehtoista datalähdettä funktiokutsun hae_kaikki() vastauksessa pitäisi olla mukana tuple {r}. Palautettu lista on\n{vastaus}')        


if __name__ == '__main__':
    unittest.main()
