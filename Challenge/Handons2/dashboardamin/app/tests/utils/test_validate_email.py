import unittest
from app.utils.validate import Utils

class TestUtils(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(Utils.is_valid_email("test@example.com"))

    def test_invalid_email_no_at_symbol(self):
        self.assertFalse(Utils.is_valid_email("testexample.com"))

    def test_invalid_email_no_domain(self):
        self.assertFalse(Utils.is_valid_email("test@.com"))

    def test_invalid_email_no_username(self):
        self.assertFalse(Utils.is_valid_email("@example.com"))

    def test_invalid_email_special_characters(self):
        self.assertFalse(Utils.is_valid_email("test@exa!mple.com"))

    def test_invalid_email_double_dot(self):
        self.assertFalse(Utils.is_valid_email("test@example..com"))

    def test_invalid_email_trailing_dot(self):
        self.assertFalse(Utils.is_valid_email("test@example.com."))

    def test_invalid_email_multiple_at_symbols(self):
        self.assertFalse(Utils.is_valid_email("test@@example.com"))

if __name__ == "__main__":
    unittest.main()