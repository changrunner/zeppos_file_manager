from os import path, listdir, makedirs
from logging import getLogger
from shutil import copy
from zeppos_file_manager.files_information import FilesInformation


class FilesAction:
    def __init__(self, logger=None):
        if not logger:
            logger = getLogger("zeppos_file_manager_files_action")
        self._logger = logger

    def backup_files_in_directory(self, source_directory, destination_directory, extension='CSV'):
        for child_directory in FilesInformation().get_child_directories(source_directory):
            for source_full_file_name in FilesInformation().get_files_by_extension(child_directory, extension):
                destination_full_file_name = path.join(
                    destination_directory, source_full_file_name.replace(source_directory, '')
                )

                if not FilesInformation.file_exists_start_with(destination_full_file_name):
                    makedirs(path.dirname(destination_full_file_name), exist_ok=True)
                    copy(source_full_file_name, destination_full_file_name)
                    self._logger.info(f"Copy [{source_full_file_name}] to [{destination_full_file_name}")
