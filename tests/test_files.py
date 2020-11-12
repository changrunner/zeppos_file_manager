import unittest
from zeppos_file_manager.files import Files
import logging
import os


class TestTheProjectMethods(unittest.TestCase):
    def test_constructor_method(self):
        files = Files(logging.getLogger("test"), "c:\\temp\\", ".csv")

    def test_count_method(self):
        self.assertEqual(Files(logging.getLogger("test"), "c:\\temp\\", "testme").count(), 0)

    def test_count_method(self):
        with open("c:\\temp\\test.testme", 'w') as fl:
            fl.write("test")

        files = Files(logging.getLogger("test"), "c:\\temp\\", "testme")
        self.assertEqual(files.count(), 1)
        first_file = None
        for file in files:
            first_file = file
            break
        self.assertEqual(first_file.file_name, "test.testme")

        os.remove("c:\\temp\\test.testme")



if __name__ == '__main__':
    unittest.main()