from os import path, makedirs
from shutil import copy
from zeppos_file_manager.files_information import FilesInformation
import os
from zeppos_logging.setup_logger import logger

class FilesAction:
    def __init__(self,):
        pass

    def backup_files_in_sub_directory(self, source_directory, destination_directory, extension='*'):
        for child_directory in FilesInformation().get_child_directories(source_directory):
            for source_full_file_name in FilesInformation().get_files_by_extension(child_directory, extension):
                destination_full_file_name = path.join(
                    destination_directory, '\\'.join([x.replace('\\', '') for x in os.path.split(source_full_file_name.replace(source_directory, ''))])
                )
                if not FilesInformation.file_exists_start_with(destination_full_file_name):
                    makedirs(path.dirname(destination_full_file_name), exist_ok=True)
                    copy(source_full_file_name, destination_full_file_name)
                    logger.info(f"Copy [{source_full_file_name}] to [{destination_full_file_name}")
