import contextlib, pathlib, typing


# File Exceptions
class FileException(Exception):
    ...


class NotFoundFileException(FileException):
    message = "Specified file does not exists!"

    def __init__(self, message):
        self.message = message or self.message
        super().__init__(self, self.message)


# File Functions
@contextlib.contextmanager
def __handle_file(file_path: pathlib.Path, mode: str = "r+b") -> typing.IO:
    file_path = pathlib.Path(file_path)
    if mode.startswith("r"):
        if not file_path.exists(): raise NotFoundFileException()
    with file_path.open(mode) as file:
        yield file


def read_file(file_path: str | pathlib.Path) -> bytes:
    f = __handle_file(file_path)
    return f.read()


def write_file(file_path: str | pathlib.Path, content: bytes) -> None:
    if not isinstance(content, bytes):
        raise TypeError("Buffer is not of type bytes!")
    f = __handle_file(file_path, 'w+b')
    f.write(content)
