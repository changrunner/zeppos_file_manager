from os import path
from shutil import move
from zeppos_logging.app_logger import AppLogger

class FileMarker:
    done_marker = "done"
    nodata_marker = "nodata"
    fail_marker = "fail"

    @staticmethod
    def file_maker_list():
        return [FileMarker.done_marker, FileMarker.nodata_marker, FileMarker.fail_marker]

    @staticmethod
    def mark_file_as_done(src_file):
        return FileMarker.mark_file_with_extension(src_file, FileMarker.done_marker)

    @staticmethod
    def mark_file_as_nodata(src_file):
        return FileMarker.mark_file_with_extension(src_file, FileMarker.nodata_marker)

    @staticmethod
    def mark_file_as_fail(src_file):
        return FileMarker.mark_file_with_extension(src_file, FileMarker.fail_marker)

    @staticmethod
    def mark_file_with_extension(source_file, state):
        try:
            destination_file = f"{source_file}.{state}"
            AppLogger.logger.debug(f'Marking file as {state}: [{source_file}] to [{destination_file}]')
            move(source_file, destination_file)
            AppLogger.logger.debug(f'Marked file as {state}: [{source_file}] to [{destination_file}]')
            return True
        except Exception as error:
            AppLogger.logger.error(f"mark_file_with_extension: {error}")
            pass
        return False

    @staticmethod
    def mark_file_as_ready(source_file):
        try:
            destination_file = path.splitext(source_file)[0]
            AppLogger.logger.debug(f'Marking file as Ready: [{source_file}] to [{destination_file}]')
            move(source_file, destination_file)
            AppLogger.logger.debug(f'Marked file as Ready: [{source_file}] to [{destination_file}]')
            return True
        except Exception as error:
            AppLogger.logger.error(f"mark_file_as_ready: {error}")
            return False

