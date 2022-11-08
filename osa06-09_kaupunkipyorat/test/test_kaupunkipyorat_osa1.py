import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.kaupunkipyorat'

def f(d):
    return '\n'.join(d)

function1 = "hae_asematiedot"
function2 = "etaisyys"

import os
from shutil import copyfile

testdata = [f"stations{i}.csv" for i in range(1,10)]

def close(a, b):
   return abs(a-b)<0.001

@points('6.kaupunkipyorat_osa1')
class KaupunkipyoratOsa1Test(unittest.TestCase):
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

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_hae_asematiedot_funktio_olemassa(self):
            try:
                from src.kaupunkipyorat import hae_asematiedot
            except:
                self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä hae_asematiedot(asema_tiedosto: str)')

            try:   
                hae_asematiedot("stations1.csv")
            except:
                self.assertTrue(False, 'Funktiokutsu hae_asematiedot("stations1.csv") aiheutti virheen')

    def test_2_hae_asematiedot_paluuarvon_tyyppi(self):
        hae_asematiedot = load(exercise, function1, 'fi')
        val = hae_asematiedot("stations1.csv")
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == dict, f"Funktion {function1} pitäisi palauttaa sanakirja (eli dict-olio), nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")

    def test_3_hae_asematiedot_1(self):
        exp = {'Kaivopuisto': (24.950292890004903, 60.15544479374228), 'Laivasillankatu': (24.956347471358754, 60.16095909388713), 'Kapteeninpuistikko': (24.944927399779715, 60.15818919997167), 'Viiskulma': (24.941775800312996, 60.16098589997938), 'Sepankatu': (24.93628529982675, 60.157948300373846), 'Hietalahdentori': (24.92970990039163, 60.162225100108344), 'Designmuseo': (24.94595999955436, 60.163103199952786), 'Vanha kirkkopuisto': (24.939149900447603, 60.165288299815245), 'Erottajan aukio': (24.944134928883898, 60.16691166693994)}
        hae_asematiedot = load(exercise, function1, 'fi')
        val = hae_asematiedot("stations1.csv")
        koodi = 'hae_asematiedot("stations1.csv")'

        for a, k in exp.items():
            self.assertTrue(a in val, f'Funktiokutsun {koodi} palauttaman sanakirjan pitäisi sisältää avain {a}. Funktio palautti\n{val}')
            taip = str(type(val[a])).replace("<class '", '').replace("'>","")
            self.assertEqual(type(val[a]), tuple, f'Funktiokutsun {koodi} palauttaman sanakirjan avaimen {a} arvon pitäisi olla tuple\nnyt se oli {val[a]}\njonka tyyppi on {taip}')
            taip = str(type(val[a][0])).replace("<class '", '').replace("'>","")
            self.assertEqual(type(val[a][0]), float, f'Funktiokutsun {koodi} palauttaman sanakirjan avaimen {a} kordinaattien pitäisi olla tyypiltään float\nnyt se oli {val[a][0]} jonka tyyppi on {taip}')
            taip = str(type(val[a][1])).replace("<class '", '').replace("'>","")
            self.assertEqual(type(val[a][1]), float, f'Funktiokutsun {koodi} palauttaman sanakirjan avaimen {a} kordinaattien pitäisi olla tyypiltään float\nnyt se oli {val[a][1]} jonka tyyppi on {taip}')
            self.assertEqual(k, val[a], f'Funktiokutsun {koodi} palauttaman sanakirjan avaimen {a} arvon pitäisi olla\n{k}\nnyt se oli\n{val[a]}')
            #self.assertTrue(False, f'\n{sorted(list(exp.keys()))}\n{sorted(list(exp.keys()))}')
            self.assertEqual(sorted(list(val.keys())), sorted(list(exp.keys())), f'Funktiokutsun {koodi} palauttamamassa sanakirjassa pitäisi olla seuraavat avaimet:\n{sorted(list(exp.keys()))}\n nyt avainten joukko oli:\n{sorted(list(val.keys()))}')

    def test_4_etaisyys_funktio_olemassa(self):
        try:
            from src.kaupunkipyorat import etaisyys
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä etaisyys(asemat: dict, asema1: str, asema2: str)')
       
        try:
            hae_asematiedot = load(exercise, function1, 'fi')
            asemat = hae_asematiedot("stations1.csv")
            val = etaisyys(asemat, "Kaivopuisto", "Laivasillankatu")
            koodi = """asemat = hae_asematiedot("stations1.csv")
etaisyys(asemat, "Kaivopuisto", "Laivasillankatu")"""
        except Exception as ioe:
            self.assertTrue(False, 'Funktiokutsu {koodi} aiheutti virheen')

    def test_5_etaisyys_paluuarvon_tyyppi(self):
        hae_asematiedot = load(exercise, function1, 'fi')
        etaisyys = load(exercise, function2, 'fi')
        asemat = hae_asematiedot("stations1.csv")
        val = etaisyys(asemat, "Kaivopuisto", "Laivasillankatu")
        koodi = """asemat = hae_asematiedot("stations1.csv")
etaisyys(asemat, "Kaivopuisto", "Laivasillankatu")"""

        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == float, f"Funktion {function2} pitäisi palauttaa float-tyypinen arvo, nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")

    def test_6_etaisyys_oiken_1(self):
        for mista, mihin, et in [
            ("Kaivopuisto","Laivasillankatu",0.6985294572684413),
            ("Kaivopuisto","Kapteeninpuistikko",0.42549272615780437),
            ("Kaivopuisto","Viiskulma",0.7753594392019532),
            ("Kaivopuisto","Sepankatu",0.8225989080090765),
            ("Kaivopuisto","Hietalahdentori",1.3646193733314156),
            ("Kaivopuisto","Designmuseo",0.884633872724747),
            ("Kaivopuisto","Vanha kirkkopuisto",1.2559087786511032),
            ("Kaivopuisto","Erottajan aukio",1.3197416922973566),
            ("Laivasillankatu","Kaivopuisto",0.6985294572684413),
            ("Laivasillankatu","Kapteeninpuistikko",0.7022284848835603),
            ("Laivasillankatu","Viiskulma",0.805236059266575),
            ("Laivasillankatu","Sepankatu",1.158086391801006),
            ("Laivasillankatu","Hietalahdentori",1.478708873076181),
            ("Laivasillankatu","Designmuseo",0.6215590959138332),
            ("Laivasillankatu","Vanha kirkkopuisto",1.06531462356818),
            ("Laivasillankatu","Erottajan aukio",0.9452984144177514),
            ("Kapteeninpuistikko","Kaivopuisto",0.42549272615780437),
            ("Kapteeninpuistikko","Laivasillankatu",0.7022284848835603),
            ("Kapteeninpuistikko","Viiskulma",0.3564371848513532),
            ("Kapteeninpuistikko","Sepankatu",0.47831316747614694),
            ("Kapteeninpuistikko","Hietalahdentori",0.9531836845512406),
            ("Kapteeninpuistikko","Designmuseo",0.5494080311763683),
            ("Kapteeninpuistikko","Vanha kirkkopuisto",0.851536068409486),
            ("Kapteeninpuistikko","Erottajan aukio",0.970926409204973),
            ("Viiskulma","Kaivopuisto",0.7753594392019532),
            ("Viiskulma","Laivasillankatu",0.805236059266575),
            ("Viiskulma","Kapteeninpuistikko",0.3564371848513532),
            ("Viiskulma","Sepankatu",0.454038196553383),
            ("Viiskulma","Hietalahdentori",0.6808521499981444),
            ("Viiskulma","Designmuseo",0.3299938171568305),
            ("Viiskulma","Vanha kirkkopuisto",0.49994836657660163),
            ("Viiskulma","Erottajan aukio",0.6717172315531527),
            ("Sepankatu","Kaivopuisto",0.8225989080090765),
            ("Sepankatu","Laivasillankatu",1.158086391801006),
            ("Sepankatu","Kapteeninpuistikko",0.47831316747614694),
            ("Sepankatu","Viiskulma",0.454038196553383),
            ("Sepankatu","Hietalahdentori",0.5985018458531813),
            ("Sepankatu","Designmuseo",0.7838427337497422),
            ("Sepankatu","Vanha kirkkopuisto",0.8314166229661707),
            ("Sepankatu","Erottajan aukio",1.0870235918079745),
            ("Hietalahdentori","Kaivopuisto",1.3646193733314156),
            ("Hietalahdentori","Laivasillankatu",1.478708873076181),
            ("Hietalahdentori","Kapteeninpuistikko",0.9531836845512406),
            ("Hietalahdentori","Viiskulma",0.6808521499981444),
            ("Hietalahdentori","Sepankatu",0.5985018458531813),
            ("Hietalahdentori","Designmuseo",0.9032737292463177),
            ("Hietalahdentori","Vanha kirkkopuisto",0.6230173508383396),
            ("Hietalahdentori","Erottajan aukio",0.9523680841254529),
            ("Designmuseo","Kaivopuisto",0.884633872724747),
            ("Designmuseo","Laivasillankatu",0.6215590959138332),
            ("Designmuseo","Kapteeninpuistikko",0.5494080311763683),
            ("Designmuseo","Viiskulma",0.3299938171568305),
            ("Designmuseo","Sepankatu",0.7838427337497422),
            ("Designmuseo","Hietalahdentori",0.9032737292463177),
            ("Designmuseo","Vanha kirkkopuisto",0.4479532398935395),
            ("Designmuseo","Erottajan aukio",0.43534463863879497),
            ("Vanha kirkkopuisto","Kaivopuisto",1.2559087786511032),
            ("Vanha kirkkopuisto","Laivasillankatu",1.06531462356818),
            ("Vanha kirkkopuisto","Kapteeninpuistikko",0.851536068409486),
            ("Vanha kirkkopuisto","Viiskulma",0.49994836657660163),
            ("Vanha kirkkopuisto","Sepankatu",0.8314166229661707),
            ("Vanha kirkkopuisto","Hietalahdentori",0.6230173508383396),
            ("Vanha kirkkopuisto","Designmuseo",0.4479532398935395),
            ("Vanha kirkkopuisto","Erottajan aukio",0.32935101970694375),
            ("Erottajan aukio","Kaivopuisto",1.3197416922973566),
            ("Erottajan aukio","Laivasillankatu",0.9452984144177514),
            ("Erottajan aukio","Kapteeninpuistikko",0.970926409204973),
            ("Erottajan aukio","Viiskulma",0.6717172315531527),
            ("Erottajan aukio","Sepankatu",1.0870235918079745),
            ("Erottajan aukio","Hietalahdentori",0.9523680841254529),
            ("Erottajan aukio","Designmuseo",0.43534463863879497),
            ("Erottajan aukio","Vanha kirkkopuisto",0.32935101970694375),    
            ]:
            hae_asematiedot = load(exercise, function1, 'fi')
            etaisyys = load(exercise, function2, 'fi')
            asemat = hae_asematiedot("stations1.csv")
            val = etaisyys(asemat, mista, mihin)
            koodi = 'asemat = hae_asematiedot("stations1.csv")\n'+f'etaisyys(asemat, "{mista}", "{mihin}")'

            self.assertTrue(close(val, et), f"Funktion vastaus {val} on väärä, pitäisi olla {et} kun suoritetaan koodi\n{koodi}")

if __name__ == '__main__':
    unittest.main()
