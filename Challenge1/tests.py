import unittest
from get_sandwich_task import get_sandwich



class TestGetSandwich(unittest.TestCase):
        def test_get_sandwich_with_empty_sandwich(self):
            self.assertEqual(
                get_sandwich(''), '')

        def test_get_sandwich_with_no_bread(self):
            self.assertEqual(
                get_sandwich('xxsalataxx'), '')

        def test_get_sandwich_with_one_bread(self):
            self.assertEqual(
                get_sandwich('chlebjajkoser'), '')

        def test_get_sandwich_with_two_breads_and_inside(self):
            self.assertEqual(
                get_sandwich('chlebjajkochleb'), 'jajko')

        def test_get_sandwich_with_two_breads_no_inside(self):
            self.assertEqual(
                get_sandwich('chlebchleb'), '')

        def test_get_sandwich_with_two_breads_and_stuff_around_it(self):
            self.assertEqual(
                get_sandwich('maslochlebszynkachlebmaslo'), 'szynka')


if __name__ == '__main__':
    unittest.main()