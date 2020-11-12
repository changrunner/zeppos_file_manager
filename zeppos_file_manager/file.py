from os import path


class File:
    def __init__(self, logger, full_file_name, extension):
        self._logger = logger
        self._full_file_name = full_file_name
        self._extension = extension

    @property
    def file_name(self):
        return path.basename(self._full_file_name)

    @property
    def full_file_name(self):
        return self._full_file_name


