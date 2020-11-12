import unittest
from zeppos_file_manager.file import File
import logging


class TestTheProjectMethods(unittest.TestCase):
    def test_constructor_method(self):
        file = File(logging.getLogger("test"), "c:\\temp\\test.csv")

    def test_file_name_method(self):
        self.assertEqual(File(logging.getLogger("test"), "c:\\temp\\test.csv").file_name, "test.csv")

    def test_full_file_name_method(self):
        self.assertEqual(File(logging.getLogger("test"), "c:\\temp\\test.csv").full_file_name, "c:\\temp\\test.csv")


if __name__ == '__main__':
    unittest.main()