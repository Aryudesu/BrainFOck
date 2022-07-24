class MyException(Exception):
    def __init__(self, arg=""):
        self.arg = arg


class NoFileError(MyException):
    def __str__(self):
        return f'"{self.arg}"が存在しません．'


class NoBracketsError(MyException):
    def __str__(self):
        return f"カッコの対応に問題があります．"


class PointerError(MyException):
    def __str__(self):
        return f"ポインタエラーです．"
