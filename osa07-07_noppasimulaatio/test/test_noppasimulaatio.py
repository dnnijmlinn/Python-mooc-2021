import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.noppasimulaatio'

@points('7.noppasimulaatio')
class NoppasimulaatioTest(unittest.TestCase):
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
    
    def test1_funktio_heita_olemassa_ja_paluuarvo_oikea(self):
        try:
             from src.noppasimulaatio import heita
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä heita(noppa: str)')
        
        try:
            vastaus = heita("A")
        except:
            self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu heita("A")')

        try:
            vastaus = heita("B")
        except:
            self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu heita("B")')

        try:
            vastaus = heita("C")
        except:
            self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu heita("C")')        

        self.assertTrue(type(vastaus) == int, f'Funktio heita ei palauta kokonaislukua, kun suoritetaan koodi heita("A")')

    def test_2_heitoilla_oikeat_tulokset_noppa_A(self):
        from src.noppasimulaatio import heita

        odotettu = [3, 6]
        lkm = {3:0, 6:0}
        kertaa = 60000
        for i in range(kertaa):
            vastaus = heita("A")
            self.assertTrue(vastaus in odotettu, f'Kun kutsutaan heita("A") on vastauksen oltava 3 tai 6, nyt vastaus oli {vastaus}')
            lkm[vastaus] += 1

        n = 3
        m = 5
        self.assertTrue(m*9700 < lkm[n] < m*10300, f'Kun kutsutaan heita("A") {kertaa} kertaa, numero {n} pitäisi saada noin {m*kertaa//6} kertaa, nyt se saatiin {lkm[n]} kertaa, noppasi ei voi toimia oikein!')

        n = 6
        m = 1
        self.assertTrue(m*9700 < lkm[n] < m*10300, f'Kun kutsutaan heita("A") {kertaa} kertaa, numero {n} pitäisi saada noin {m*kertaa//6} kertaa, nyt se saatiin {lkm[n]} kertaa, noppasi ei voi toimia oikein!')

    def test_2_heitoilla_oikeat_tulokset_noppa_B(self):
        from src.noppasimulaatio import heita

        odotettu = [2, 5]
        lkm = {2:0, 5:0}
        kertaa = 60000
        for i in range(kertaa):
            vastaus = heita("B")
            self.assertTrue(vastaus in odotettu, f'Kun kutsutaan heita("B") on vastauksen oltava 2 tai 5, nyt vastaus oli {vastaus}')
            lkm[vastaus] += 1

        n = 2
        m = 3
        self.assertTrue(m*9700 < lkm[n] < m*10300, f'Kun kutsutaan heita("B") {kertaa} kertaa, numero {n} pitäisi saada noin {m*kertaa//6} kertaa, nyt se saatiin {lkm[n]} kertaa, noppasi ei voi toimia oikein!')

        n = 5
        m = 3
        self.assertTrue(m*9700 < lkm[n] < m*10300, f'Kun kutsutaan heita("B") {kertaa} kertaa, numero {n} pitäisi saada noin {m*kertaa//6} kertaa, nyt se saatiin {lkm[n]} kertaa, noppasi ei voi toimia oikein!')

    def test_2_heitoilla_oikeat_tulokset_noppa_C(self):
        from src.noppasimulaatio import heita

        odotettu = [1, 4]
        lkm = {1:0, 4:0}
        kertaa = 60000
        for i in range(kertaa):
            vastaus = heita("C")
            self.assertTrue(vastaus in odotettu, f'Kun kutsutaan heita("C") on vastauksen oltava 1 tai 4, nyt vastaus oli {vastaus}')
            lkm[vastaus] += 1

        n = 1
        m = 1
        self.assertTrue(m*9700 < lkm[n] < m*10300, f'Kun kutsutaan heita("C") {kertaa} kertaa, numero {n} pitäisi saada noin {m*kertaa//6} kertaa, nyt se saatiin {lkm[n]} kertaa, noppasi ei voi toimia oikein!')

        n = 4
        m = 5
        self.assertTrue(m*9700 < lkm[n] < m*10300, f'Kun kutsutaan heita("C") {kertaa} kertaa, numero {n} pitäisi saada noin {m*kertaa//6} kertaa, nyt se saatiin {lkm[n]} kertaa, noppasi ei voi toimia oikein!')

    def test_3_funktio_pelaa_olemassa_ja_paluuarvo_oikea(self):
        try:
             from src.noppasimulaatio import pelaa
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä pelaa(noppa1: str, noppa2: str, kertaa: int)')
        
        try:
            vastaus = pelaa("A", "B", 10)
        except:
            self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu pelaa("A", "B", 10)')

        try:
            vastaus = pelaa("C", "A", 10)
        except:
            self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu pelaa("C", "A", 10)')

        try:
            vastaus = pelaa("B", "C", 10)
        except:
            self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu pelaa("B", "C", 10)')        

        self.assertTrue(type(vastaus) == tuple, f'Funktio pelaa tulee palauttaa tuple, joka sisältä kolme kokonaislukua kun suoritetaan koodi pelaa("B", "C", 10).\nFunktio palautti {vastaus}')
        self.assertTrue(len(vastaus)  == 3, f'Funktio pelaa tulee palauttaa tuple, joka sisältä kolme kokonaislukua kun suoritetaan koodi pelaa("B", "C", 10).\nFunktio palautti {vastaus}')
        self.assertTrue(type(vastaus[0]) == int, f'Funktio pelaa tulee palauttaa tuple, joka sisältä kolme kokonaislukua kun suoritetaan koodi pelaa("B", "C", 10).\nFunktio palautti {vastaus}')
        self.assertTrue(type(vastaus[1]) == int, f'Funktio pelaa tulee palauttaa tuple, joka sisältä kolme kokonaislukua kun suoritetaan koodi pelaa("B", "C", 10).\nFunktio palautti {vastaus}')
        self.assertTrue(type(vastaus[2]) == int, f'Funktio pelaa tulee palauttaa tuple, joka sisältä kolme kokonaislukua kun suoritetaan koodi pelaa("B", "C", 10).\nFunktio palautti {vastaus}')

    def test_4_paluuarvot_jarkevia(self):
        from src.noppasimulaatio import pelaa
        n1 = "A"
        n2 = "B"
        koodi = f'pelaa("{n1}", "{n2}", 100)'
        vastaus = pelaa(n1, n2, 100)
       
        self.assertEqual(vastaus[0] + vastaus[1] , 100, f'Kun kutsutaan {koodi} pitää voittojen summan olla 100, nyt paluuarvo oli {vastaus}')
        self.assertTrue(vastaus[0] > 0 and vastaus[1] > 0, f'Kun kutsutaan {koodi} pitää molemmilla olla voittoja, paluuarvo oli {vastaus}')
        self.assertTrue(vastaus[2] == 0, f'Kun kutsutaan {koodi} on tuloksessa ei voi olla tasapelejä, paluuarvo oli {vastaus}')

        n1 = "C"
        n2 = "A"
        koodi = f'pelaa("{n1}", "{n2}", 100)'
        vastaus = pelaa(n1, n2, 100)
       
        self.assertEqual(vastaus[0] + vastaus[1] , 100, f'Kun kutsutaan {koodi} pitää voittojen summan olla 100, nyt paluuarvo oli {vastaus}')
        self.assertTrue(vastaus[0] > 0 and vastaus[1] > 0, f'Kun kutsutaan {koodi} pitää molemmilla olla voittoja, paluuarvo oli {vastaus}')
        self.assertTrue(vastaus[2] == 0, f'Kun kutsutaan {koodi} on tuloksessa ei voi olla tasapelejä, paluuarvo oli {vastaus}')

        n1 = "B"
        n2 = "C"
        koodi = f'pelaa("{n1}", "{n2}", 100)'
        vastaus = pelaa(n1, n2, 100)
       
        self.assertEqual(vastaus[0] + vastaus[1] , 100, f'Kun kutsutaan {koodi} pitää voittojen summan olla 100, nyt paluuarvo oli {vastaus}')
        self.assertTrue(vastaus[0] > 0 and vastaus[1] > 0, f'Kun kutsutaan {koodi} pitää molemmilla olla voittoja, paluuarvo oli {vastaus}')
        self.assertTrue(vastaus[2] == 0, f'Kun kutsutaan {koodi} on tuloksessa ei voi olla tasapelejä, paluuarvo oli {vastaus}')

        n1 = "C"
        n2 = "C"
        koodi = f'pelaa("{n1}", "{n2}", 1000)'
        vastaus = pelaa(n1, n2, 1000)
       
        self.assertEqual(vastaus[0] + vastaus[1] + vastaus[2], 1000, f'Kun kutsutaan {koodi} pitää voittojen summan olla 100, nyt paluuarvo oli {vastaus}')
        self.assertTrue(vastaus[0] > 0 and vastaus[1] > 0, f'Kun kutsutaan {koodi} pitää molemmilla olla voittoja, paluuarvo oli {vastaus}')
        self.assertTrue(vastaus[2] > 0, f'Kun kutsutaan {koodi} on tuloksessa oltava myös tasapelejä, paluuarvo oli {vastaus}')


    def test_5_A_vastaan_B(self):
        from src.noppasimulaatio import pelaa

        voitot = { "A":0, "B":0, "C": 0}
        kertaa = 100
        for i in range(kertaa):
            n1 = "A"
            n2 = "B"
            vastaus = pelaa(n1, n2, 100)
            koodi = f'pelaa("{n1}", "{n2}", 100)'
            voitot[n1] += vastaus[0]
            voitot[n2] += vastaus[1] 
        self.assertTrue(voitot[n1] > voitot[n2], f'Kun kutsutaan {kertaa} kertaa {koodi} pitäiasi nopan {n1} voittaa useammin')

    def test_5_B_vastaan_C(self):
        from src.noppasimulaatio import pelaa

        voitot = { "A":0, "B":0, "C": 0}
        kertaa = 100
        for i in range(kertaa):
            n1 = "B"
            n2 = "C"
            vastaus = pelaa(n1, n2, 100)
            koodi = f'pelaa("{n1}", "{n2}", 100)'
            voitot[n1] += vastaus[0]
            voitot[n2] += vastaus[1] 
        self.assertTrue(voitot[n1] > voitot[n2], f'Kun kutsutaan {kertaa} kertaa {koodi} pitäiasi nopan {n1} voittaa useammin')

    def test_5_C_vastaan_A(self):
        from src.noppasimulaatio import pelaa

        voitot = { "A":0, "B":0, "C": 0}
        kertaa = 100
        for i in range(kertaa):
            n1 = "C"
            n2 = "A"
            vastaus = pelaa(n1, n2, 100)
            koodi = f'pelaa("{n1}", "{n2}", 100)'
            voitot[n1] += vastaus[0]
            voitot[n2] += vastaus[1] 
        self.assertTrue(voitot[n1] > voitot[n2], f'Kun kutsutaan {kertaa} kertaa {koodi} pitäiasi nopan {n1} voittaa useammin')


if __name__ == '__main__':
    unittest.main()
