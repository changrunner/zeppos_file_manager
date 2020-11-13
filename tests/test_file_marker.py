import unittest
from zeppos_file_manager.file_marker import FileMarker
import os
from tests.util_for_testing import UtilForTesting


class TestTheProjectMethods(unittest.TestCase):
    def test_done_method(self):
        self.assertEqual(FileMarker.done_marker, "done")

    def test_fail_method(self):
        self.assertEqual(FileMarker.fail_marker, "fail")

    def test_nodata_method(self):
        self.assertEqual(FileMarker.nodata_marker, "nodata")

    def test_mark_files_as_done_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('done')

        result = FileMarker.mark_file_as_done(full_file_name_list[0])

        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(full_file_name_list[0] + ".done"), True)

        UtilForTesting.file_teardown(temp_dir)

    def test_mark_files_as_fail_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('fail')

        result = FileMarker.mark_file_as_fail(full_file_name_list[0])

        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(full_file_name_list[0] + ".fail"), True)

        UtilForTesting.file_teardown(temp_dir)

    def test_mark_files_as_nodata_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('nodata')

        result = FileMarker.mark_file_as_nodata(full_file_name_list[0])

        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(full_file_name_list[0] + ".nodata"), True)

        UtilForTesting.file_teardown(temp_dir)

    def test_mark_files_as_ready_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('ready', '.done')

        result = FileMarker.mark_files_as_ready(full_file_name_list[0])

        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.splitext(full_file_name_list[0])[0]), True)

        UtilForTesting.file_teardown(temp_dir)


if __name__ == '__main__':
    unittest.main()
