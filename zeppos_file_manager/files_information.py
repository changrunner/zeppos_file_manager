from glob import glob
from os import path, listdir
from zeppos_file_manager.file_marker import FileMarker
from zeppos_logging.app_logger import AppLogger

class FilesInformation:
    def __init__(self):
        pass

    def get_files_by_extension(self, base_dir, extension="*", start_file_filter=None, end_file_filter=None,
                               include_processed=False):
        AppLogger.logger.info(f'get_files_by_extension: [{base_dir}], [{extension}]')
        files = glob(
            path.join(
                base_dir,
                f'{str(start_file_filter or "")}*{str(end_file_filter or "")}.{extension}'
            )
        )
        if include_processed:
            for file_marker in FileMarker.file_maker_list():
                files += self.get_files_by_extension(base_dir, f"{extension}.{file_marker}",
                                                     start_file_filter, end_file_filter)
        return sorted(files)

    def get_files_excluding_extension(self, base_dir, extension):
        AppLogger.logger.info(f'get_files: [{base_dir}]')
        files = glob(path.join(base_dir, '*'))
        return filter(lambda x: not x.upper().endswith(f".{extension.upper()}"), files)

    def get_child_directories(self, base_dir):
        dirs = [path.join(base_dir, o) for o in listdir(base_dir)
                if path.isdir(path.join(base_dir, o))]
        AppLogger.logger.info(f"Got [{len(dirs)}] directories")
        return dirs

    @staticmethod
    def file_exists_start_with(full_file_name):
        files = glob(path.join(path.dirname(full_file_name), '*'))
        return len(
            list(
                filter(lambda x:
                       path.basename(x).upper().startswith(
                           path.basename(full_file_name).upper()),
                       files))) > 0
