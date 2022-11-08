import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.eka_toka_vika_sana'

@points('4.eka_toka_vika_sana')
class ETjaVSanaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_5_tokasana_toiminta_kunnossa(self):
        for rivi in ["olipa kerran ohjelmointi", "sen pituinen se", "Lorem ipsum dolor sit amet consectetur adipiscing elit", "eka toka", "Tee ohjelma joka kysyy käyttäjältä merkkijonoa ja yksittäistä merkkia"]:
            with patch('builtins.input', side_effect=["2 2"] * 10):
                reload_module(self.module)
                output_alussa = get_stdout()
                from src.eka_toka_vika_sana import toka_sana
                
                try:
                    vast = toka_sana(rivi)
                except:
                    self.assertTrue(False, f'Varmista että seuraava funktiokutsu toimii\ntoka_sana("{rivi}")') 
        
                output_all = get_stdout().replace(output_alussa, '', 1)

                odotettu = rivi.split(' ')[1]
                self.assertFalse(vast == None, f'Funktiokutsun toka_sana("{rivi}") pitäisi palauttaa\n{odotettu}\nnyt se ei palauta mitään. Varmista, että funktiossasi käytetään return-komentoa kaikissa tilanteissa!')           
                self.assertEqual(vast, odotettu, f'Funktiokutsun toka_sana("{rivi}") pitäisi palauttaa\n{odotettu}\nnyt se palauttaa\n{vast}')
                self.assertFalse(len(output_all)>0, f'Funktiokutsun toka_sana("{rivi}") ei pitäisi tulostaa mitään, sen kuitenkin tulostaa\n{output_all}\npoista print-komennot metodin sisältä')

    def test_6_vikasana_olemassa(self):
        try:
            from src.eka_toka_vika_sana import vika_sana
        except:
            self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään vika_sana')
        try:
            from src.eka_toka_vika_sana import vika_sana
            vika_sana("olipa kerran ohjelmointi")
        except:
            self.assertTrue(False, f'tarkista että seuraava funktiokutsu onnistuu\vika_sana("olipa kerran ohjelmointi")')

    def test_7_vikasana_toiminta_kunnossa(self):
        for rivi in ["olipa kerran ohjelmointi", "sen pituinen se", "Lorem ipsum dolor sit amet consectetur adipiscing elit", "eka toka", "Tee ohjelma joka kysyy käyttäjältä merkkijonoa ja yksittäistä merkkia"]:
            with patch('builtins.input', side_effect=["2 2"] * 10):
                reload_module(self.module)
                output_alussa = get_stdout()
                from src.eka_toka_vika_sana import vika_sana
               
                try:
                     vast = vika_sana(rivi)
                except:
                    self.assertTrue(False, f'Varmista että seuraava funktiokutsu toimii\nvika_sana("{rivi}")') 
                        
                output_all = get_stdout().replace(output_alussa, '', 1)

                odotettu = rivi.split(' ')[-1]
                self.assertFalse(vast == None, f'Funktiokutsun vika_sana("{rivi}") pitäisi palauttaa\n{odotettu}\nnyt se ei palauta mitään. Varmista, että funktiossasi käytetään return-komentoa kaikissa tilanteissa!')           
                self.assertEqual(vast, odotettu, f'Funktiokutsun vika_sana("{rivi}") pitäisi palauttaa\n{odotettu}\nnyt se palauttaa\n{vast}')
                self.assertFalse(len(output_all)>0, f'Funktiokutsun vika_sana("{rivi}") ei pitäisi tulostaa mitään, sen kuitenkin tulostaa\n{output_all}\npoista print-komennot metodin sisältä')

if __name__ == '__main__':
    unittest.main()
