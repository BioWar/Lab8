import unittest
import LW8


class LW8Tests(unittest.TestCase):
    """Doc string"""
    def test_input(self):
        for instance in LW8.gems:
            self.assertIsInstance(instance, LW8.Stones)




if __name__ == '__main__':
    unittest.main()
