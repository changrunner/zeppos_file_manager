# Make sure we have the correct relative path
from sys import path, exc_info, stdout
path.insert(0, '.')  # chang to the root directory of the project
#########################################################################
import unittest
from zeppos_file_manager.file_information import FileInformation
from tests.util_for_testing import UtilForTesting


class TestTheProjectMethods(unittest.TestCase):
    def test_get_total_line_count_for_file_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(sub_directory="file_info", content="1\n2\n")
        print(full_file_name_list[0])
        self.assertEqual(
            FileInformation.get_total_line_count_for_file(full_file_name_list[0]),
            2
        )
        UtilForTesting.file_teardown(temp_dir)


if __name__ == '__main__':
    unittest.main()
