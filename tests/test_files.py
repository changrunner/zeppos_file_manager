import unittest
from zeppos_file_manager.files import Files
from tests.util_for_testing import UtilForTesting
import os
from datetime import datetime


class TestTheProjectMethods(unittest.TestCase):
    def setUp(self):
        UtilForTesting.file_clean_up()

    def tearDown(self):
        # UtilForTesting.file_clean_up()
        pass
    def test_constructor_method(self):
        self.assertEqual(str(type(Files("c:\\temp\\"))),
                         "<class 'zeppos_file_manager.files.Files'>")

    def test_count_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('testme', extension="csv")
        self.assertEqual(Files(file_dir, "csv").count(), 1)

    def test_count_with_subdir_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(
            r'test_1\field1=somedata1\field2=somedata2', extension="",
            content="col1,col2\ntest1,test2")
        self.assertEqual(Files(file_dir, extension="csv", include_subdir=True).count(), 1)

    def test__iter___method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('testme')

        for file in Files(file_dir, "ext"):
            self.assertEqual(file.file_name, "test_0.csv.ext")
            break


    def test_1_copy_files_adding_today_timestamp_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('cpy')
        file_name_list = ['test_0.csv.ext']
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        now_datetime = datetime.strptime('2001-02-03 04:05:06', '%Y-%m-%d %H:%M:%S')

        # Execute Method
        result = Files(file_dir, "ext")\
            .copy_files_adding_today_timestamp(
            destination_directory=dest_dir,
            now_datetime=now_datetime,
            source_file_filter_list=file_name_list)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_0.csv.ext")), True)


    def test_2_copy_files_adding_today_timestamp_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('cpy', count=2)
        file_name_list = ['test_0.csv.ext', 'test_1.csv.ext']
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        now_datetime = datetime.strptime('2001-02-03 04:05:06', '%Y-%m-%d %H:%M:%S')

        # Execute Method
        result = Files(file_dir, "ext")\
            .copy_files_adding_today_timestamp(
            destination_directory=dest_dir,
            now_datetime=now_datetime,
            source_file_filter_list=file_name_list)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_0.csv.ext")), True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_1.csv.ext")), True)


    def test_3_copy_files_adding_today_timestamp_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('cpy', count=2)
        file_name_list = ['test_0.csv.ext']
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        now_datetime = datetime.strptime('2001-02-03 04:05:06', '%Y-%m-%d %H:%M:%S')

        # Execute Method
        result = Files(file_dir, 'ext').copy_files_adding_today_timestamp(
            destination_directory=dest_dir,
            now_datetime=now_datetime,
            source_file_filter_list=file_name_list
        )

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_0.csv.ext")), True)


    def test_copy_files_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('cpy', count=1)
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        self.assertEqual(Files(file_dir, 'ext').copy_files(dest_dir), True)
        self.assertEqual(os.path.exists(os.path.join(file_dir, "test_0.csv.ext.done")), True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "test_0.csv.ext")), True)
        UtilForTesting.file_teardown(temp_dir)

        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('cpy', count=1)
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        self.assertEqual(Files(file_dir, 'ext').copy_files(dest_dir, prefix="abc"), True)
        self.assertEqual(os.path.exists(os.path.join(file_dir, "test_0.csv.ext.done")), True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "abc_test_0.csv.ext")), True)
        UtilForTesting.file_teardown(temp_dir)

        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('cpy', count=1)
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        self.assertEqual(Files(file_dir, 'ext').copy_files(dest_dir, target_file_name="abc.ext"), True)
        self.assertEqual(os.path.exists(os.path.join(file_dir, "test_0.csv.ext.done")), True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "abc.ext")), True)
        UtilForTesting.file_teardown(temp_dir)

        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('cpy', count=1)
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        self.assertEqual(Files(file_dir, 'ext').copy_files(dest_dir, mark_as_done=False), True)
        self.assertEqual(os.path.exists(os.path.join(file_dir, "test_0.csv.ext")), True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "test_0.csv.ext")), True)

    def test_mark_files_as_ready_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('cpy', count=1, extension="done")
        self.assertEqual(Files(file_dir, 'csv', include_processed=True).mark_files_as_ready(), True)
        self.assertEqual(os.path.exists(os.path.join(file_dir, "test_0.csv")), True)


if __name__ == '__main__':
    unittest.main()