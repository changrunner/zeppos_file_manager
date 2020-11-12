from os import path
from shutil import move


class FileMarker:
    done_marker = "done"
    nodata_marker = "nodata"
    fail_marker = "fail"

    @staticmethod
    def file_maker_list():
        return [FileMarker.done_marker, FileMarker.nodata_marker, FileMarker.fail_marker]

    @staticmethod
    def mark_file_as_done(logger, src_file):
        return FileMarker.mark_file_with_extension(logger, src_file, FileMarker.done_marker)

    @staticmethod
    def mark_file_as_nodata(logger, src_file):
        return FileMarker.mark_file_with_extension(logger, src_file, FileMarker.nodata_marker)

    @staticmethod
    def mark_file_as_fail(logger, src_file):
        return FileMarker.mark_file_with_extension(logger, src_file, FileMarker.fail_marker)

    @staticmethod
    def mark_file_with_extension(logger, source_file, state):
        # This function is self contained and errors will be read from the error log.
        try:
            destination_file = f"{source_file}.{state}"
            logger.debug(f'Marking file as {state}: [{source_file}] to [{destination_file}]')
            move(source_file, destination_file)
            logger.debug(f'Marked file as {state}: [{source_file}] to [{destination_file}]')
            return True
        except Exception as error:
            logger.error(f"mark_file_with_extension: {error}")
        return False

    @staticmethod
    def mark_files_as_ready(logger, source_file):
        # This function is self contained and errors will be read from the error log.
        try:
            destination_file = path.splitext(source_file)[0]
            logger.debug(f'Marking file as Ready: [{source_file}] to [{destination_file}]')
            move(source_file, destination_file)
            logger.debug(f'Marked file as Ready: [{source_file}] to [{destination_file}]')
            return True
        except Exception as error:
            logger.error(f"mark_files_as_ready: {error}")
            return False

