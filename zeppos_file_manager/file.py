from os import path
import logging
from zeppos_file_manager.file_marker import FileMarker


class File:
    def __init__(self, logger, full_file_name):
        self._logger = logger
        self._full_file_name = full_file_name

    @property
    def file_name(self):
        return path.basename(self._full_file_name)

    @property
    def full_file_name(self):
        return self._full_file_name

    @property
    def extension(self):
        return path.splitext(self._full_file_name)[1][1:]

    def mark_as_done(self):
        return FileMarker.mark_file_as_done(self._logger, self._full_file_name)

    def mark_as_fail(self):
        return FileMarker.mark_file_as_fail(self._logger, self._full_file_name)

    def mark_as_nodata(self):
        return FileMarker.mark_file_as_nodata(self._logger, self._full_file_name)
