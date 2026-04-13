import unittest
from age import categorize_by_age

class TestIsGolden(unittest.TestCase):
    def test_child_age(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a child.")
                self.assertEqual(result, "Child")

    def test_adolescent_age(self):
        for age in range(10, 19):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as an adolescent.")
                self.assertEqual(result, "Adolescent")

    def test_golden_age(self):
        for age in range(66, 151):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a golden age.")
                self.assertEqual(result, "Golden age")

if __name__ == "__main__":
    unittest.main(verbosity=2)