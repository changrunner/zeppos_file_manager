import unittest
from zeppos_file_manager.file import File
from tests.util_for_testing import UtilForTesting
import os


class TestTheProjectMethods(unittest.TestCase):
    def test_constructor_method(self):
        self.assertEqual(str(type(File("c:\\temp\\test.csv"))),
                         "<class 'zeppos_file_manager.file.File'>")

    def test_file_name_property(self):
        self.assertEqual(File("c:\\temp\\test.csv").file_name, "test.csv")

    def test_full_file_name_property(self):
        self.assertEqual(File("c:\\temp\\test.csv").full_file_name, "c:\\temp\\test.csv")

    def test_full_extension_property(self):
        self.assertEqual(File("c:\\temp\\test.csv").extension, "csv")

    def test_mark_file_as_done_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('done')

        File(full_file_name=full_file_name_list[0]).mark_as_done()
        self.assertEqual(os.path.exists(full_file_name_list[0] + ".done"), True)

        UtilForTesting.file_teardown(temp_dir)

    def test_mark_file_as_fail_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('fail')

        File(full_file_name=full_file_name_list[0]).mark_as_fail()
        self.assertEqual(os.path.exists(full_file_name_list[0] + ".fail"), True)

        UtilForTesting.file_teardown(temp_dir)

    def test_mark_file_as_nodata_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('nodata')

        File(full_file_name=full_file_name_list[0]).mark_as_nodata()
        self.assertEqual(os.path.exists(full_file_name_list[0] + ".nodata"), True)

        UtilForTesting.file_teardown(temp_dir)

    def test_get_total_line_count_for_file_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(sub_directory="file_info", content="1\n2\n")

        self.assertEqual(
            File(full_file_name_list[0]).get_total_line_count_for_file(),
            2
        )
        UtilForTesting.file_teardown(temp_dir)

    def test_mark_file_as_ready_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('ready', '.done')

        result = File(full_file_name_list[0]).mark_file_as_ready()

        self.assertEqual(result, True)
        self.assertEqual(os.path.exists(os.path.splitext(full_file_name_list[0])[0]), True)

        UtilForTesting.file_teardown(temp_dir)


if __name__ == '__main__':
    unittest.main()