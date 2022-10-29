import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.tulosta_luvut'

@points('2.tulosta_luvut')
class TulostaLuvutTest(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.module = load_module(exercise, 'fi')

        def test_tulosta_luvut(self):
            reload_module(self.module)
            output = get_stdout()
            output_list = [x for x in output.split("\n") if len(x.strip()) > 0]
            cor = [str(x) for x in range(2,31,2)]
            self.assertEqual(len(output_list), 15, f"Ohjelmasi tulisi tulostaa 15 riviä, nyt se tulostaa {len(output_list)} riviä.")
            r = 1
            for l1,l2 in zip(cor, output_list):
                self.assertEqual(l1, l2, f"Tulostus ei vastaa mallivastausta rivillä {r+1}: ohjelman pitäisi tulostaa {l1}, mutta se tulostaa {l2}.")

if __name__ == '__main__':
    unittest.main()
