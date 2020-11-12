from os import path, listdir
from logging import getLogger
from json import load, dump
from datetime import datetime


class FileAction:
    def __init__(self, logger=None):
        if not logger:
            logger = getLogger("zeppos_file_manager_file_action")
        self._logger = logger

    def get_json_from_file(self, full_file_name):
        if full_file_name:
            if path.exists(full_file_name):
                with open(full_file_name, 'r') as fr:
                    json_string = load(fr)

                return json_string
        return ""

    def save_json(self, base_dir, payload, payload_dict_element_name,
                  payload_type, start_date_string, end_date_string,
                  file_extension="json"):
        payload_hash_string = payload_type
        full_file_name = path.join(
            base_dir,
            f'payload_type={payload_type}_start_date={start_date_string}_end_date={end_date_string}'
            f'_guid={abs(hash(payload_hash_string + str(datetime.now())))}.{file_extension}'
        )
        self._logger.info("Saving info to file [{}]".format(path.basename(full_file_name)))
        json_res = payload.get(payload_dict_element_name)
        if json_res:
            dump(json_res, open(path.join(base_dir, full_file_name), 'w'))
            return full_file_name

        self._logger.info("Empty Payload!")
        return full_file_name

    @staticmethod
    def get_total_line_count_for_file(full_file_name, line_terminator="\n"):
        with open(full_file_name, "r", encoding="utf-8", errors='ignore') as f:
            total_count = sum(bl.count(line_terminator) for bl in File._blocks(f))
        return total_count

    @staticmethod
    def _blocks(files, size=65536):
        while True:
            b = files.read(size)
            if not b: break
            yield b


