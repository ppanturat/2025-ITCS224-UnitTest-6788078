import unittest
from age import categorize_by_age

class TestIsGolden(unittest.TestCase):
    def test_golden_age(self):
        for age in range(66, 151):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a golden age.")
                self.assertEqual(result, "Golden age")

if __name__ == "__main__":
    unittest.main(verbosity=2)