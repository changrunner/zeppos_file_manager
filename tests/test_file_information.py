import unittest
from zeppos_file_manager.file_information import FileInformation


class TestTheProjectMethods(unittest.TestCase):
    def test_get_total_line_count_for_file_method(self):
        with open("c:\\temp\\testfile.txt", "w") as fl:
            fl.write("line1\n")

        self.assertEqual(FileInformation.get_total_line_count_for_file("c:\\temp\\testfile.txt"), 1)


if __name__ == '__main__':
    unittest.main()