import unittest
from zeppos_file_manager.files import Files
from tests.util_for_testing import UtilForTesting
import logging
import os
from datetime import datetime
import shutil


class TestTheProjectMethods(unittest.TestCase):
    def test_constructor_method(self):
        self.assertEqual(str(type(Files(UtilForTesting.get_logger(), "c:\\temp\\"))),
                         "<class 'zeppos_file_manager.files.Files'>")

    def test_count_method(self):
        temp_dir, file_dir, full_file_name_list, logger = UtilForTesting.file_setup('testme')
        self.assertEqual(Files(logger, file_dir, "testme").count(), 0)
        UtilForTesting.file_teardown(temp_dir)

    def test__iter___method(self):
        temp_dir, file_dir, full_file_name_list, logger = UtilForTesting.file_setup('testme')

        for file in Files(logger, file_dir, "ext"):
            self.assertEqual(file.file_name, "test_0.csv.ext")
            break

        UtilForTesting.file_teardown(temp_dir)

    def test_1_copy_files_adding_today_timestamp_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list, logger = UtilForTesting.file_setup('cpy')
        file_name_list = ['test_0.csv.ext']
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        now_datetime = datetime.strptime('2001-02-03 04:05:06', '%Y-%m-%d %H:%M:%S')

        # Execute Method
        result = Files(logger, file_dir, "ext")\
            .copy_files_adding_today_timestamp(
            destination_directory=dest_dir,
            now_datetime=now_datetime,
            source_file_filter_list=file_name_list)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_0.csv.ext")), True)

        UtilForTesting.file_teardown(temp_dir)

    def test_2_copy_files_adding_today_timestamp_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list, logger = UtilForTesting.file_setup('cpy', count=2)
        file_name_list = ['test_0.csv.ext', 'test_1.csv.ext']
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        now_datetime = datetime.strptime('2001-02-03 04:05:06', '%Y-%m-%d %H:%M:%S')

        # Execute Method
        result = Files(logger, file_dir, "ext")\
            .copy_files_adding_today_timestamp(
            destination_directory=dest_dir,
            now_datetime=now_datetime,
            source_file_filter_list=file_name_list)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_0.csv.ext")), True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_1.csv.ext")), True)

        UtilForTesting.file_teardown(temp_dir)

    def test_3_copy_files_adding_today_timestamp_method(self):
        temp_dir, file_dir, full_file_name_list, logger = UtilForTesting.file_setup('cpy', count=2)
        file_name_list = ['test_0.csv.ext']
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        now_datetime = datetime.strptime('2001-02-03 04:05:06', '%Y-%m-%d %H:%M:%S')

        # Execute Method
        result = Files(logger, file_dir, 'ext').copy_files_adding_today_timestamp(
            destination_directory=dest_dir,
            now_datetime=now_datetime,
            source_file_filter_list=file_name_list
        )

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_0.csv.ext")), True)

        UtilForTesting.file_teardown(temp_dir)


if __name__ == '__main__':
    unittest.main()