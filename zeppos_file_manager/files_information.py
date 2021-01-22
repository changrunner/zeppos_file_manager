from glob import glob
from os import path, listdir
from zeppos_file_manager.file_marker import FileMarker
from zeppos_logging.app_logger import AppLogger
from os import walk, path


class FilesInformation:
    @staticmethod
    def get_files_by_extension(base_dir, extension="*", start_file_filter=None, end_file_filter=None,
                               include_subdir=False, include_processed=False, exclude_extension=None):
        AppLogger.logger.debug(f'get_files_by_extension: [{base_dir}], [{extension}]')
        file_list = glob(
            path.join(
                base_dir,
                "**" if include_subdir else "",
                f'{str(start_file_filter or "")}*{str(end_file_filter or "")}.{extension}'
            ),
            recursive=include_subdir
        )

        if include_processed:
            for file_marker in FileMarker.file_maker_list():
                file_list += FilesInformation.get_files_by_extension(
                    base_dir=base_dir,
                    extension=f"{extension}.{file_marker}",
                    start_file_filter=start_file_filter,
                    end_file_filter=end_file_filter,
                    include_subdir=include_subdir,
                    include_processed=False  # very important. Otherwise we get infinite loop.
                )
        if exclude_extension:
            file_list = filter(lambda x: not x.upper().endswith(f".{exclude_extension.upper()}"), file_list)

        return sorted(file_list)

    @staticmethod
    def get_files_excluding_extension(base_dir, extension):
        AppLogger.logger.debug(f'get_files: [{base_dir}]')
        return FilesInformation.get_files_by_extension(
            base_dir=base_dir,
            exclude_extension=extension
        )

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
