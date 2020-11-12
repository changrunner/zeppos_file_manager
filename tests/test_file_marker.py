import unittest
from zeppos_file_manager.file_marker import FileMarker
import os
import shutil
import logging
from datetime import datetime


class TestTheProjectMethods(unittest.TestCase):
    def test_done_method(self):
        self.assertEqual(FileMarker.done_marker, "done")

    def test_fail_method(self):
        self.assertEqual(FileMarker.fail_marker, "fail")

    def test_nodata_method(self):
        self.assertEqual(FileMarker.nodata_marker, "nodata")

    def test_mark_files_as_done_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list, logger = self._file_setup('done')

        # Execute Method
        result = FileMarker(logger).mark_file_with_extension(full_file_name_list[0], FileMarker.done_marker)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(full_file_name_list[0] + ".done"), True)

        # Clean up
        self._file_cleanup(temp_dir)

    def test_mark_files_as_fail_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list, logger = self._file_setup('fail')

        # Execute Method
        result = FileMarker(logger).mark_file_with_extension(full_file_name_list[0], FileMarker.fail_marker)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(full_file_name_list[0] + ".fail"), True)

        # Clean up
        self._file_cleanup(temp_dir)

    def test_mark_files_as_nodata_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list, logger = self._file_setup('nodata')

        # Execute Method
        result = FileMarker(logger).mark_file_with_extension(full_file_name_list[0], FileMarker.nodata_marker)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(full_file_name_list[0] + ".nodata"), True)

        # Clean up
        self._file_cleanup(temp_dir)

    def test_mark_files_as_ready_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list, logger = self._file_setup('ready', '.ready')

        # Execute Method
        result = FileMarker(logger).mark_files_as_ready(full_file_name_list[0])

        # # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.splitext(full_file_name_list[0])[0]), True)

        # Clean up
        self._file_cleanup(temp_dir)

    def test_1_copy_files_adding_today_timestamp_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list, logger = self._file_setup(file_marker='cpy', count=1)
        file_name_list = ['test_0.csv']
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        now_datetime = datetime.strptime('2001-02-03 04:05:06', '%Y-%m-%d %H:%M:%S')

        # Execute Method
        result = FileMarker(logger).copy_files_adding_today_timestamp(file_dir, file_name_list, dest_dir, now_datetime)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_0.csv")), True)

        self._file_cleanup(temp_dir)

    def test_2_copy_files_adding_today_timestamp_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list, logger = self._file_setup(file_marker='cpy', count=2)
        file_name_list = ['test_0.csv', 'test_1.csv']
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        now_datetime = datetime.strptime('2001-02-03 04:05:06', '%Y-%m-%d %H:%M:%S')

        # Execute Method
        result = FileMarker(logger).copy_files_adding_today_timestamp(file_dir, file_name_list, dest_dir, now_datetime)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_0.csv")), True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_1.csv")), True)

        self._file_cleanup(temp_dir)

    def test_3_copy_files_adding_today_timestamp_method(self):
        # Setup
        temp_dir, file_dir, full_file_name_list, logger = self._file_setup(file_marker='cpy', count=2)
        file_name_list = ['test_0.csv']
        dest_dir = os.path.join(os.path.dirname(file_dir), 'cpy2')
        now_datetime = datetime.strptime('2001-02-03 04:05:06', '%Y-%m-%d %H:%M:%S')

        # Execute Method
        result = FileMarker(logger).copy_files_adding_today_timestamp(file_dir, file_name_list, dest_dir, now_datetime)

        # Check Result
        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.join(dest_dir, "2001_02_03_04_05_06_test_0.csv")), True)

        self._file_cleanup(temp_dir)

    def _file_setup(self, file_marker, extension="", count=1):
        temp_dir = os.path.join(os.path.dirname(__file__), "temp")
        file_dir = os.path.join(temp_dir, file_marker)
        logger = logging.getLogger("test")
        if os.path.exists(file_dir):
            shutil.rmtree(file_dir, ignore_errors=True)
        os.makedirs(file_dir)

        full_file_name_list = []
        for index in range(0, count):
            full_file_name = os.path.join(file_dir, f"test_{index}.csv" + extension)
            with open(full_file_name, 'w') as fl:
                fl.write("some test file")
            full_file_name_list.append(full_file_name)

        return temp_dir, file_dir, full_file_name_list, logger

    def _file_cleanup(self, temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
