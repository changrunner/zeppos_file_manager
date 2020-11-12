import os
import shutil
import logging


class UtilForTesting:
    @staticmethod
    def file_setup(sub_directory, extension="ext", count=1, content="some test file"):
        if extension:
            extension = "." + extension
        else:
            extension = ""

        temp_dir = os.path.join(os.path.dirname(__file__), "temp")
        file_dir = os.path.join(temp_dir, sub_directory)
        if os.path.exists(file_dir):
            shutil.rmtree(file_dir, ignore_errors=True)
        os.makedirs(file_dir)
        full_file_name_list = []
        for index in range(0, count):
            full_file_name = os.path.join(file_dir, f"test_{index}.csv" + extension)
            with open(full_file_name, 'w') as fl:
                fl.write(content)
            full_file_name_list.append(full_file_name)

        return temp_dir, file_dir, full_file_name_list, UtilForTesting.get_logger()

    @staticmethod
    def file_teardown(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)

    @staticmethod
    def get_logger():
        return logging.getLogger("test")