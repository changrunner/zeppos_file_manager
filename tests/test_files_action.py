import unittest
from zeppos_file_manager.files_action import FilesAction


class TestTheProjectMethods(unittest.TestCase):
    def test_backup_dir_method(self):
        FilesAction().backup_files_in_directory("c:\\temp", "c:\\temp\\backuptest")


if __name__ == '__main__':
    unittest.main()