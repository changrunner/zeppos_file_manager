from zeppos_file_manager.file import File
from os import environ, path
from sys import platform
from random import choices
from tempfile import gettempdir
from string import ascii_letters, digits

class TempFile(File):
    tmp_dir = None

    def __init__(self):
        self._tmp_full_file_name = self._get_full_file_name()

    @property
    def temp_full_file_name(self):
        return self._tmp_full_file_name

    @classmethod
    def _get_tmp_dir(cls):
        if cls.tmp_dir:
            tmp_dir = cls.tmp_dir
        elif platform == 'linux':
            try:
                tmp_dir = environ['XDG_RUNTIME_DIR']
            except KeyError:
                tmp_dir = None
            if not tmp_dir:
                tmp_dir = '/dev/shm'
        else:
            tmp_dir = gettempdir()
        return tmp_dir

    @classmethod
    def _get_full_file_name(cls):
        tmp_dir = cls._get_tmp_dir()
        file_path = path.join(tmp_dir, ''.join(
            choices(ascii_letters + digits, k=21)))
        return file_path
