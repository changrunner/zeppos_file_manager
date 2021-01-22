from os import path
from zeppos_file_manager.file_marker import FileMarker
from zeppos_file_manager.file_information import FileInformation
from zeppos_file_manager.file_action import FileAction
from os import path

class File:
    def __init__(self, full_file_name):
        self._full_file_name = full_file_name

    @property
    def file_name(self):
        return path.basename(self._full_file_name)

    @property
    def file_name_without_extension(self):
        return path.splitext(path.basename(self._full_file_name))[0]

    @property
    def full_file_name(self):
        return self._full_file_name

    @property
    def directory_name(self):
        return path.dirname(self._full_file_name)

    @property
    def extension(self):
        return path.splitext(self._full_file_name)[1][1:]

    def mark_as_done(self):
        return FileMarker.mark_file_as_done(self._full_file_name)

    def mark_as_fail(self):
        return FileMarker.mark_file_as_fail(self._full_file_name)

    def mark_as_nodata(self):
        return FileMarker.mark_file_as_nodata(self._full_file_name)

    def get_total_line_count_for_file(self):
        return FileInformation.get_total_line_count_for_file(self._full_file_name)

    def mark_file_as_ready(self):
        return FileMarker.mark_file_as_ready(self._full_file_name)

    @staticmethod
    def create_instance_with_todays_date(root_directory, file_name, file_object,
                                         format="%d_%m_%Y_%H_%M_%S"):
        return file_object(full_file_name=
                           FileAction.get_full_file_name_with_todays_date(root_directory, file_name, format)
                           )
