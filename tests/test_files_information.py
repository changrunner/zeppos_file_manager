import unittest
from zeppos_file_manager.files_information import FilesInformation
from tests.util_for_testing import UtilForTesting
import shutil
import os


class TestTheProjectMethods(unittest.TestCase):
    def setUp(self):
        UtilForTesting.file_clean_up()

    def tearDown(self):
        UtilForTesting.file_clean_up()

    def test_get_files_by_extension_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_1', extension="",
            content="col1,col2\ntest1,test2")
        files = FilesInformation.get_files_by_extension(base_dir=file_dir, extension="csv")
        self.assertEqual(1, len(files))

    def test_get_files_by_extension_start_file_filter_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_2', extension="",
            content="col1,col2\ntest1,test2")
        shutil.move(full_file_name_list[0], os.path.join(file_dir, 'testme_test_0.csv'))
        files = FilesInformation.get_files_by_extension(base_dir=file_dir, extension="csv", start_file_filter="testme")
        self.assertEqual(1, len(files))

    def test_get_files_by_extension_end_file_filter_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_3', extension="",
            content="col1,col2\ntest1,test2")
        shutil.move(full_file_name_list[0], os.path.join(file_dir, 'test_0_testme.csv'))
        files = FilesInformation.get_files_by_extension(base_dir=file_dir, extension="csv", end_file_filter="testme")
        self.assertEqual(1, len(files))

    def test_get_files_by_extension_include_subdir_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_4\field1=somedata1\field2=somedata2', extension="",
            content="col1,col2\ntest1,test2")
        files = FilesInformation.get_files_by_extension(base_dir=temp_dir, extension="csv", include_subdir=True)
        self.assertEqual(1, len(files))

    def test_get_files_by_extension_include_processed_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_5', extension="done",
            content="col1,col2\ntest1,test2")
        files = FilesInformation.get_files_by_extension(base_dir=file_dir, extension="csv", include_processed=True)
        self.assertEqual(1, len(files))

    def test_get_files_by_extension_include_subdir_include_processed_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_6\field1=somedata1\field2=somedata2', extension="",
            content="col1,col2\ntest1,test2")
        files = FilesInformation.get_files_by_extension(base_dir=temp_dir, extension="csv",
                                                        include_subdir=True, include_processed=True)
        self.assertEqual(1, len(files))

    def test_get_files_excluding_extension_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_7\field1=somedata1\field2=somedata2', extension="",
            content="col1,col2\ntest1,test2")
        files = FilesInformation.get_files_excluding_extension(base_dir=file_dir, extension="csv")
        self.assertEqual(0, len(files))

    def test_get_child_directories_method(self):
        FilesInformation.get_child_directories("c:\\")

    def test_file_exists_start_with_method(self):
        FilesInformation.file_exists_start_with("c:\\temp\\test.csv")


if __name__ == '__main__':
    unittest.main()