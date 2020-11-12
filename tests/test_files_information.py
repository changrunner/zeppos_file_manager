import unittest
from zeppos_file_manager.files_information import FilesInformation


class TestTheProjectMethods(unittest.TestCase):
    def test_get_files_by_extension_method(self):
        FilesInformation().get_files_by_extension("c:\\", "*.txt")
        FilesInformation().get_files_by_extension("c:\\", "*.txt", "test1", "test2")
        FilesInformation().get_files_by_extension("c:\\", "*.txt", "test1", "test2", True)

    def test_get_files_excluding_extension_method(self):
        FilesInformation().get_files_excluding_extension("c:\\", "*.txt")

    def test_get_child_directories_method(self):
        FilesInformation().get_child_directories("c:\\")

    def test_file_exists_start_with_method(self):
        FilesInformation.file_exists_start_with("c:\\temp\\test.csv")


if __name__ == '__main__':
    unittest.main()