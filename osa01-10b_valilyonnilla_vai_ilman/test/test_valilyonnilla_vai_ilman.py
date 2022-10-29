import unittest
from unittest.mock import patch
from inspect import getsource

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.valilyonnilla_vai_ilman'

expected = [
    "nimeni on Teppo Testaaja, olen 20-vuotias",
    "",
    "taitoihini kuuluvat",
    " - python (aloittelija)",
    " - java (veteraani)",
    " - ohjelmointi (puoliammattilainen)",
    "",
    "haen työtä, josta maksetaan palkkaa 2000-3000 euroa kuussa"
]

@points('1.valilyonnilla_vai_ilman')
class ValilyontiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        reload_module(self.module)
        output = get_stdout().split('\n')
        self.assertEqual(8, len(output), f"sovelluksesi tulostaa väärän määrän rivejä {len(output)}, sen tulisi tulostaa 8 riviä. Tulostathan myös tyhjät rivit?")
        for i in range(0, 8):
            if i in [3, 4, 5]:
                self.assertEqual(' ', output[i][0], f"sovelluksesi tulostaa rivin {i+1} väärin, tulostit:\n{output[i]}\nhuomaathan että rivin alussa on välilyönti!")    
            self.assertEqual(expected[i], output[i].rstrip(), f"sovelluksesi tulostaa rivin {i+1} väärin, sen pitäisi olla:\n{expected[i]}\nsovelluksesi tulosti:\n{output[i]}")

    def test_tulostus_2(self):
        kielletyt = [
            "nimeni on Teppo Testaaja, olen 20-vuotias",
            " - python (aloittelija)",
            " - java (veteraani)",
            " - ohjelmointi (puoliammattilainen)",
            "haen työtä, josta maksetaan palkkaa 2000-3000 euroa kuussa"
        ]

        source = getsource(self.module)
        for line in source.split("\n"):
            for kielletty in kielletyt:
                if kielletty in line:
                    self.assertTrue(False, f"käytä tulostuksessa muuttujien arvoja, koodistasi ei saa olla riviä\n{line}")

if __name__ == '__main__':
    unittest.main()
