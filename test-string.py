import unittest

def double_text(text):
    return "".join([char * 2 for char in text])

class TestDoubleText(unittest.TestCase):
    def test_double_text(self):
        # Test case for the function to check if it doubles each character correctly
        self.assertEqual(double_text("aupp"), "aauupppp")
        self.assertEqual(double_text(""), "")  # Test with empty string
        self.assertEqual(double_text("abc"), "aabbcc")  # Test with different characters
        self.assertEqual(double_text("123"), "112233")  # Test with numbers
        self.assertEqual(double_text(" "), "  ")  # Test with whitespace
        self.assertEqual(double_text("Aa"), "AAaa")  # Test with mixed case

if __name__ == "__main__":
    unittest.main()
