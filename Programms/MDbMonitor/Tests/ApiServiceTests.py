import unittest

from Programms.MDbMonitor.Tests import Helpers

class ApiServiceTests(unittest.TestCase):

    def get_from_api_should_return_correct_values(self):
        sut = Helpers.get_system_under_test()

        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()