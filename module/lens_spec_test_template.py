import unittest


class TestLensSpec(unittest.TestCase):
    def setUp(self):
        self.ttl = 1.5

    def test_ttl(self):
        expeted = 1.6
        self.assertLessEqual(
            self.ttl, 
            expeted, 
            msg = "Hey! Your ttl should be awared."
            )

    def test_mtf_c(self):
        expeted = 0.85
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
