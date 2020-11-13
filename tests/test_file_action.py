import unittest
from zeppos_file_manager.file_action import FileAction
from tests.util_for_testing import UtilForTesting


class TestTheProjectMethods(unittest.TestCase):
    def test_get_json_from_file_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(sub_directory="file_action",
                                                                            content='{"test1":"test2"}')
        self.assertEqual(FileAction.get_json_from_file(full_file_name_list[0]), {'test1': 'test2'})
        UtilForTesting.file_teardown(temp_dir)




if __name__ == '__main__':
    unittest.main()
