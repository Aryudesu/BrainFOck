import os

from error import NoFileError


def file_check(path: str) -> None:
    if not os.path.isfile(path):
        raise NoFileError(path)
