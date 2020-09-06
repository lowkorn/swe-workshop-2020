import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("ปอซ่า"))

    def test_validate_name_with_invalid_input_string_of_int(self):
        self.assertEqual(False, validate_name("007"))

    def test_validate_name_with_invalid_input_contained_string_of_int(self):
        self.assertEqual(False, validate_name("ชายปอzaa007"))

    def test_validate_name_with_invalid_input_spacial_char(self):
        self.assertEqual(False, validate_name("มีไรหรอ!"))

    def test_validate_name_with_invalid_input_spacial_char_more_one(self):
        self.assertEqual(False, validate_name("$อะไร@เนี้ย#"))

    def test_validate_name_with_empty_input(self):
        self.assertEqual(False, validate_name(""))

    def test_validate_name_with_without_space(self):
        self.assertEqual(False, validate_name("ปอ ซ่า"))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
