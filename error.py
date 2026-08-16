class MyException(Exception):
    """Base class for interpreter-specific errors."""


class NoFileError(MyException):
    def __init__(self, path: str = "") -> None:
        self.path = path

    def __str__(self) -> str:
        return f'"{self.path}"が存在しません．'


class NoBracketsError(MyException):
    def __str__(self) -> str:
        return "カッコの対応に問題があります．"


class PointerError(MyException):
    def __str__(self) -> str:
        return "ポインタエラーです．"
