import CamelCaser
import unittest


class TestCamelCasing(unittest.TestCase):

    def test_wrong_spaces(self):
        # Everything correct except spacing
        self.assertEqual(CamelCaser.camel_case('The Life Of Brian'), 'TheLifeOfBrian')

    def test_wrong_casing(self):
        # casing is mixed
        self.assertEqual(CamelCaser.camel_case('the Life of Brian'), 'TheLifeOfBrian')

    def test_forbidden_characters(self):
        self.assertEqual(CamelCaser.camel_case('the,.* Life&%: of Brian'), 'TheLifeOfBrian')

if __name__ == '__main__':
    unittest.main()
