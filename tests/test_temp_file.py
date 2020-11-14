import unittest
from zeppos_file_manager.temp_file import TempFile


class TestTheProjectMethods(unittest.TestCase):
    def test_constructor_method(self):
        self.assertEqual(str(type(TempFile())), "<class 'zeppos_file_manager.temp_file.TempFile'>")

    def test_temp_full_file_name_property(self):
        self.assertGreater(len(TempFile().temp_full_file_name) , 0)


if __name__ == '__main__':
    unittest.main()