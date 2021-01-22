import unittest
from zeppos_file_manager.file import File
from tests.util_for_testing import UtilForTesting
import os


class TestTheProjectMethods(unittest.TestCase):
    def setUp(self):
        UtilForTesting.file_clean_up()

    def tearDown(self):
        UtilForTesting.file_clean_up()

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

    def test_create_instance_with_todays_date_method(self):
        file = File.create_instance_with_todays_date(r"c:\temp", "test.csv", File)
        self.assertEqual(r"c:\temp", os.path.dirname(file.full_file_name))
        self.assertEqual("test.csv", os.path.basename(file.full_file_name).split("__")[1])
        self.assertGreater(len(os.path.basename(file.full_file_name).split("__")[0]), 0)

    def test_directory_name_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup('test_dir_name', '')
        self.assertEqual(os.path.dirname(full_file_name_list[0]), File(full_file_name_list[0]).directory_name)

    def file_name_without_extension_method(self):
        self.assertEqual("test", File("c:\\test\\test.csv").file_name_without_extension)


if __name__ == '__main__':
    unittest.main()