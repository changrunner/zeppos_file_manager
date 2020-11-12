from zeppos_file_manager.files_information import FilesInformation
from zeppos_file_manager.file import File

class Files:
    def __init__(self, logger, base_dir, extension, start_file_filter=None, end_file_filter=None,
                 include_processed=False, file_object=File):
        self._logger = logger
        self._file_object = file_object
        self._files = FilesInformation(logger).get_files_by_extension(
            base_dir=base_dir,
            extension=extension,
            start_file_filter=start_file_filter,
            end_file_filter=end_file_filter,
            include_processed=include_processed
        )
        self._extension = extension
        self.idx = 0

    def count(self):
        return len(self._files)

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        try:
           return self._file_object(self._logger, self._files[self.idx-1], self._extension)
        except IndexError:
           self.idx = 0
           raise StopIteration  # Done iterating.

