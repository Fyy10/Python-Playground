import unittest


class TestPossibleResults(unittest.TestCase):
    def test_success(self):
        return 0

    def test_failure(self):
        self.assertEqual(True, False)

    def test_error(self):
        raise TypeError
