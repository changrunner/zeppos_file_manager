import unittest
from zeppos_file_manager.files_information import FilesInformation
from tests.util_for_testing import UtilForTesting

class TestTheProjectMethods(unittest.TestCase):
    def setUp(self):
        UtilForTesting.file_clean_up()

    def tearDown(self):
        UtilForTesting.file_clean_up()

    def test_get_files_by_extension_method(self):
        FilesInformation.get_files_by_extension("c:\\")
        FilesInformation.get_files_by_extension("c:\\", "*.txt")
        FilesInformation.get_files_by_extension("c:\\", "*.txt", "test1", "test2")
        FilesInformation.get_files_by_extension("c:\\", "*.txt", "test1", "test2", True)
        FilesInformation.get_files_by_extension(base_dir="c:\\")

    def test_get_files_by_extension_include_subdir_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_1\field1=somedata1\field2=somedata2', extension="",
            content="col1,col2\ntest1,test2")
        files = FilesInformation.get_files_by_extension(base_dir=file_dir, extension="*.csv", include_subdir=True)
        self.assertEqual(1, len(files))

    def test_get_files_by_extension_include_subdir_include_processed_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_1\field1=somedata1\field2=somedata2', extension=".done",
            content="col1,col2\ntest1,test2")
        files = FilesInformation.get_files_by_extension(base_dir=file_dir, extension="*.csv", include_subdir=True, include_processed=True)
        self.assertEqual(1, len(files))

    def test_get_files_excluding_extension_method(self):
        FilesInformation.get_files_excluding_extension("c:\\", "*.txt")

    def test_get_child_directories_method(self):
        FilesInformation.get_child_directories("c:\\")

    def test_file_exists_start_with_method(self):
        FilesInformation.file_exists_start_with("c:\\temp\\test.csv")


if __name__ == '__main__':
    unittest.main()