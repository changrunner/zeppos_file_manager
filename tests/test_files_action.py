import unittest
from zeppos_file_manager.files_action import FilesAction
from tests.util_for_testing import UtilForTesting
import os

class TestTheProjectMethods(unittest.TestCase):
    def test_backup_files_in_sub_directory_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('source', None)
        dest_dir = os.path.join(temp_dir, "backup")
        FilesAction().backup_files_in_sub_directory(
            source_directory=temp_dir,
            destination_directory=dest_dir,
            extension='csv'
            )

        self.assertEqual(os.path.exists(os.path.join(dest_dir, 'source', 'test_0.csv')), True)
        UtilForTesting.file_teardown(temp_dir)


if __name__ == '__main__':
    unittest.main()