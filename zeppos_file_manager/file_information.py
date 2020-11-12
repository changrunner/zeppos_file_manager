from glob import glob
from os import path, listdir
from zeppos_file_manager.file_marker import FileMarker
from logging import getLogger
from json import load, dump
from datetime import datetime


class FileInformation:
    def __init__(self, logger=None):
        if not logger:
            logger = getLogger("zeppos_file_manager_file_information")
        self._logger = logger

    @staticmethod
    def get_total_line_count_for_file(full_file_name, line_terminator="\n"):
        with open(full_file_name, "r", encoding="utf-8", errors='ignore') as f:
            total_count = sum(bl.count(line_terminator) for bl in FileInformation._blocks(f))
        return total_count

    @staticmethod
    def _blocks(files, size=65536):
        while True:
            b = files.read(size)
            if not b: break
            yield b


