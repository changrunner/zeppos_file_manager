from zeppos_logging.app_logger import AppLogger

class FilesLoggerInformation:
    @staticmethod
    def get_global_logger_name():
        return AppLogger.get_global_logger_name()
