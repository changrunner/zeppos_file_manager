from glob import glob
from os import path, listdir
from zeppos_file_manager.file_marker import FileMarker
from zeppos_logging.app_logger import AppLogger
from os import walk, path


class FilesInformation:
    @staticmethod
    def get_files_by_extension(base_dir, extension="*", start_file_filter=None, end_file_filter=None,
                               include_subdir=False, include_processed=False):
        AppLogger.logger.debug(f'get_files_by_extension: [{base_dir}], [{extension}]')
        if not include_subdir:
            file_list = glob(
                path.join(
                    base_dir,
                    f'{str(start_file_filter or "")}*{str(end_file_filter or "")}.{extension}'
                )
            )
        else:
            file_list = []
            for root, dirs, files in walk(base_dir):
                for file in files:
                    # append the file name to the list
                    file_list.append(path.join(root, file))

        if include_processed:
            for file_marker in FileMarker.file_maker_list():
                files += FilesInformation.get_files_by_extension(base_dir, f"{extension}.{file_marker}",
                                                                 start_file_filter, end_file_filter, include_subdir)

        return sorted(file_list)

    @staticmethod
    def get_files_excluding_extension(base_dir, extension):
        AppLogger.logger.debug(f'get_files: [{base_dir}]')
        files = glob(path.join(base_dir, '*'))
        return filter(lambda x: not x.upper().endswith(f".{extension.upper()}"), files)

    @staticmethod
    def get_child_directories(base_dir):
        dirs = [path.join(base_dir, o) for o in listdir(base_dir)
                if path.isdir(path.join(base_dir, o))]
        AppLogger.logger.debug(f"Got [{len(dirs)}] directories")
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
