from zeppos_file_manager.files_information import FilesInformation
from zeppos_file_manager.file import File
from os import path, makedirs
from shutil import copyfile
from datetime import datetime
from zeppos_logging.setup_logger import logger


class Files:
    def __init__(self, base_dir, extension="*", start_file_filter=None, end_file_filter=None,
                 include_processed=False, file_object=File):
        self._files = FilesInformation().get_files_by_extension(
            base_dir=base_dir,
            extension=extension,
            start_file_filter=start_file_filter,
            end_file_filter=end_file_filter,
            include_processed=include_processed
        )
        self._base_dir = base_dir
        self._file_object = file_object
        self._extension = extension
        self.idx = 0

    def count(self):
        return len(self._files)

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        try:
           return self._file_object(
               full_file_name=self._files[self.idx-1]
           )
        except IndexError:
           self.idx = 0
           raise StopIteration  # Done iterating.

    def copy_files_adding_today_timestamp(self,
                                          destination_directory,
                                          now_datetime=datetime.today(),
                                          date_format="%Y_%m_%d_%H_%M_%S",
                                          source_file_filter_list=None):
        # This function is self contained and errors will be read from the error log.
        try:
            makedirs(destination_directory, exist_ok=True)
            file_list_to_copy = []
            for file in self._files:
                if source_file_filter_list:
                    for source_file in source_file_filter_list:
                        if path.basename(file).lower().strip() == source_file.lower().strip():
                            file_list_to_copy.append(file)
                else:
                    file_list_to_copy.append(file)

            for file in file_list_to_copy:
                copyfile(src=file,
                         dst=path.join(destination_directory,
                                       f"{now_datetime.strftime(date_format)}_{path.basename(file)}"
                                       )
                         )
            return True
        except Exception as error:
            logger.error(f"Could not copy file over: {error}")
            return False

    def copy_files(self, target_directory_string, prefix='', target_file_name=None,
                   mark_as_done=True):
        if not path.exists(target_directory_string):
            logger.debug(f"Create Directory: {target_directory_string}")
            makedirs(target_directory_string, exist_ok=True)

        for file in self.__iter__():
            if target_file_name:
                target_full_file_name = path.join(target_directory_string,
                                                  f"{prefix}{target_file_name}")
            else:
                target_full_file_name = path.join(target_directory_string,
                                                  f"{''.join([prefix + '_' if len(prefix) > 0 else ''])}"
                                                  f"{file.file_name}")

            logger.debug(f'Copy File [{file.full_file_name}] to [{target_full_file_name}]')
            copyfile(file.full_file_name, target_full_file_name)

            if mark_as_done:
                file.mark_as_done()

        return True

    def mark_files_as_ready(self):
        for file in self.__iter__():
            file.mark_file_as_ready()
        return True
