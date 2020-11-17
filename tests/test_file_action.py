import unittest
from zeppos_file_manager.file_action import FileAction
from tests.util_for_testing import UtilForTesting
from testfixtures import LogCapture
from zeppos_logging.app_logger import AppLogger

class TestTheProjectMethods(unittest.TestCase):
    def test_1_get_json_from_file_method(self):
        temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(sub_directory="file_action",
                                                                            content='{"test1":"test2"}')
        self.assertEqual({'test1': 'test2'}, FileAction.get_json_from_file(full_file_name_list[0]))
        UtilForTesting.file_teardown(temp_dir)

    def test_2_get_json_from_file_method(self):
        AppLogger.configure_and_get_logger('2_get_json_from_file')
        with LogCapture() as lc:
            temp_dir, file_dir, full_file_name_list = UtilForTesting.file_setup(sub_directory="file_action",
                                                                                content='{"test1":"test2"')
            self.assertEqual(None, FileAction.get_json_from_file(full_file_name_list[0]))
            UtilForTesting.file_teardown(temp_dir)

            UtilForTesting.check_log_capture(
                self, lc, [('2_get_json_from_file', 'ERROR', "Error get_json_from_file: Expecting ',' delimiter")],
                ("exact", "exact", "startswith")
            )


if __name__ == '__main__':
    unittest.main()
