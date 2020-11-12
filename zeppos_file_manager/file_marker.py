from os import path, makedirs
from shutil import move, copyfile
from glob import glob
from datetime import datetime
from logging import getLogger


class FileMarker:
    done_marker = "done"
    nodata_marker = "nodata"
    fail_marker = "fail"

    def __init__(self, logger=None):
        if not logger:
            logger = getLogger("zeppos_file_manager_file_marker")
        self._logger = logger

    @staticmethod
    def file_marker():
        return [FileMarker.done_marker, FileMarker.nodata_marker, FileMarker.fail_marker]

    def mark_files_as_done(self, src_file):
        return self.mark_file_with_extension(src_file, FileMarker.done_marker)

    def mark_files_as_nodata(self, src_file):
        return self.mark_file_with_extension(src_file, FileMarker.no_data_marker)

    def mark_files_as_fail(self, src_file):
        return self.mark_file_with_extension(src_file, FileMarker.fail_marker)

    def mark_file_with_extension(self, src_file, state):
        # This function is self contained and errors will be read from the error log.
        try:
            dest_file = f"{src_file}.{state}"
            self._logger.info(f'Marking file as {state}: [{src_file}] to [{dest_file}]')
            move(src_file, dest_file)
            self._logger.info(f'Marked file as {state}: [{src_file}] to [{dest_file}]')
            return True
        except Exception as error:
            self._logger.error(f"mark_file_with_extension: {error}")
        return False

    def mark_files_as_ready(self, src_file):
        # This function is self contained and errors will be read from the error log.
        try:
            dest_file = path.splitext(src_file)[0]
            self._logger.info(f'Marking file as Ready: [{src_file}] to [{dest_file}]')
            move(src_file, dest_file)
            self._logger.info(f'Marked file as Ready: [{src_file}] to [{dest_file}]')
            return True
        except Exception as error:
            self._logger.error(f"mark_files_as_ready: {error}")
            return False

    def copy_files_adding_today_timestamp(self, source_directory, source_file_list,
                                          destination_directory, now_datetime=datetime.today(),
                                          date_format="%Y_%m_%d_%H_%M_%S"):
        # This function is self contained and errors will be read from the error log.
        try:
            makedirs(destination_directory, exist_ok=True)
            files = glob(path.join(source_directory, "*"))
            for file in files:
                for source_file in source_file_list:
                    if path.basename(file).lower().strip() == source_file.lower().strip():
                        copyfile(src=file,
                                 dst=path.join(destination_directory,
                                               f"{now_datetime.strftime(date_format)}_{path.basename(file)}"
                                               )
                                 )
            return True
        except Exception as error:
            self._logger.error(f"Could not copy file over: {error}")
            return False
