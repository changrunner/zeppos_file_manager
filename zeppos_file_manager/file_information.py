from zeppos_logging.setup_logger import logger

class FileInformation:
    @staticmethod
    def get_total_line_count_for_file(full_file_name, line_terminator="\n"):
        try:
            with open(full_file_name, "r", encoding="utf-8", errors='ignore') as f:
                total_count = sum(bl.count(line_terminator) for bl in FileInformation._blocks(f))
            return total_count
        except Exception as error:
            logger.error(f"Error get_total_line_count_for_file: {error}")
            return None

    @staticmethod
    def _blocks(files, size=65536):
        while True:
            b = files.read(size)
            if not b: break
            yield b


