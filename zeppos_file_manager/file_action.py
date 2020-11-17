from os import path
from json import load, dump
from datetime import datetime
from zeppos_logging.app_logger import AppLogger

class FileAction:
    @staticmethod
    def get_json_from_file(full_file_name):
        try:
            if full_file_name:
                if path.exists(full_file_name):
                    with open(full_file_name, 'r') as fr:
                        json_string = load(fr)
                    return json_string
            return None
        except Exception as error:
            AppLogger.logger.error(f"Error get_json_from_file: {error}")
            return None

    @staticmethod
    def save_json(base_dir, payload, payload_dict_element_name,
                  payload_type, start_date_string, end_date_string,
                  file_extension="json"):
        try:
            payload_hash_string = payload_type
            full_file_name = path.join(
                base_dir,
                f'payload_type={payload_type}_start_date={start_date_string}_end_date={end_date_string}'
                f'_guid={abs(hash(payload_hash_string + str(datetime.now())))}.{file_extension}'
            )
            AppLogger.logger.debug("Saving info to file [{}]".format(path.basename(full_file_name)))
            json_res = payload.get(payload_dict_element_name)
            if json_res:
                dump(json_res, open(path.join(base_dir, full_file_name), 'w'))
                return full_file_name

            AppLogger.logger.info("Empty Payload!")
            return full_file_name
        except Exception as error:
            AppLogger.logger.error(f"Error save_json: {error}")
            return None
