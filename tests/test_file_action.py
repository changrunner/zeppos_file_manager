import unittest
from zeppos_file_manager.file_action import FileAction
import logging


class TestTheProjectMethods(unittest.TestCase):
    def test_get_json_from_file_method(self):
        FileAction(logging.getLogger("test")).get_json_from_file("c:\\json_test_file.json")

    # def test_save_data_method(self):
    #     full_file_name = FileAction().save_data("this is a test", "c:\\temp", '{"Test":"test"}', "2020_01_01", "2020_01_02")


if __name__ == '__main__':
    unittest.main()