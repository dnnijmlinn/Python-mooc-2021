import unittest
unittest.TestLoader.sortTestMethodsUsing = None

from tmc import points

from tmc.utils import get_stdout, load_module, reload_module, assert_ignore_ws, sanitize

exercise = 'src.ukko_nooa'
@points('1.ukko_nooa')
class UkkoNooaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')
        
    def test_content(self):
        reload_module(self.module)
        out = get_stdout()
        self.assertTrue(len(out)>0, 'Koodisi ei tulosta mitään')
        split_output = sanitize(out).split('\n')

        self.assertFalse(len(split_output) != 3, 'Tulostuksessa odotettiin olevan {0} riviä, ohjelmasi tulostaa tällä hetkellä {1} riviä.'.format(3, len(split_output)))
        assert_ignore_ws(self, split_output[0], 'Ukko Nooa, Ukko Nooa oli kunnon mies.', 'Ensimmäisen rivin tulostus väärin. ')
        assert_ignore_ws(self, split_output[1], 'Kun hän meni saunaan, laittoi laukun naulaan.', 'Toisen rivin tulostus väärin. ')
        assert_ignore_ws(self, split_output[2], 'Ukko Nooa, Ukko Nooa oli kunnon mies.', 'Kolmannen rivin tulostus väärin. ')

if __name__ == '__main__':
    unittest.main()