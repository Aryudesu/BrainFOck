import os
from error import NoFileError


def file_check(path):
    is_file = os.path.isfile(path)
    if not is_file:
        raise NoFileError(path)
