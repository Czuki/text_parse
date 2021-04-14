import unittest
from test_utils import create_test_files, remove_test_files, TABS_TO_SPACES, SPACES_TO_TABS
from logic.converter import IndentConverter
import os


class TestClassMethods(unittest.TestCase):
    def setUp(self):
        create_test_files()
        self.test_converter = IndentConverter(
            file_name='tabs_to_spaces.txt',
            convert_from='tabs',
            space_count=4,
            replace=False
        )

    def tearDown(self):
        remove_test_files()

    def test_tabs_to_spaces(self):
        modified_text = self.test_converter.replace_leading_whitespace()
        self.assertEqual(modified_text, SPACES_TO_TABS)

    def test_tabs_to_spaces_creates_new_file(self):
        modified_text = self.test_converter.replace_leading_whitespace()
        self.test_converter.write_to_file(modified_text=modified_text)
        self.assertEqual(os.path.exists('tabs_to_spaces.txt'), True)
        self.assertEqual(os.path.exists('tabs_to_spaces1.txt'), True)

    def test_tabs_to_spaces_file_replace(self):
        self.test_converter.replace = True
        modified_text = self.test_converter.replace_leading_whitespace()
        self.test_converter.write_to_file(modified_text=modified_text)
        self.assertEqual(os.path.exists('tabs_to_spaces.txt'), True)
        self.assertEqual(os.path.exists('tabs_to_spaces1.txt'), False)

    def test_spaces_to_tabs(self):
        self.test_converter.replace = False
        self.test_converter.file_name = 'spaces_to_tabs.txt'
        self.test_converter.convert_from = 'spaces'
        modified_text = self.test_converter.replace_leading_whitespace()
        self.assertEqual(modified_text, TABS_TO_SPACES)

    def test_spaces_to_tabs_creates_new_file(self):
        self.test_converter.file_name = 'spaces_to_tabs.txt'
        self.test_converter.convert_from = 'spaces'
        modified_text = self.test_converter.replace_leading_whitespace()
        self.test_converter.write_to_file(modified_text=modified_text)
        self.assertEqual(os.path.exists('spaces_to_tabs.txt'), True)
        self.assertEqual(os.path.exists('spaces_to_tabs1.txt'), True)

    def test_spaces_to_tabs_file_replace(self):
        self.test_converter.replace = True
        modified_text = self.test_converter.replace_leading_whitespace()
        self.test_converter.write_to_file(modified_text=modified_text)
        self.assertEqual(os.path.exists('spaces_to_tabs.txt'), True)
        self.assertEqual(os.path.exists('spaces_to_tabs1.txt'), False)

    def test_file_not_exists_raises_error(self):
        self.test_converter.file_name = 'some_file.txt'

    def test_to_fail(self):
        self.assertEqual(False, 0)


if __name__ == '__main__':
    unittest.main()
