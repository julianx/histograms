import unittest


class MyTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(True, True)

    def test_failure(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
