import pathlib

from . import file_handler


# File Exceptions
class FileException(Exception):
    ...


class NotSpecifiedFileException(FileException):
    message = "No file specified! Please set path or pass path as an argument"

    def __init__(self, message):
        self.message = message or self.message
        super().__init__(self, self.message)


# File Class
class File():

    def __init__(self, path: str | pathlib.Path = None):
        self.__path: pathlib.Path = path
        self.__buffer: bytes = bytes()

    @property
    def path(self) -> str | pathlib.Path:
        return self.__path

    @path.setter
    def path(self, path: str | pathlib.Path) -> None:
        if not isinstance(path, (str, pathlib.Path)):
            raise TypeError("Path is not of type str nor Path!")
        self.__path = path

    @property
    def buffer(self) -> bytes:
        return self.__buffer

    @buffer.setter
    def buffer(self, buffer: bytes) -> None:
        self.__buffer = buffer

    def read(self, path: str | pathlib.Path = None) -> None:
        if not (path or self.__path): raise NotSpecifiedFileException()
        buff = file_handler.read_file(path or self.__path)
        self.__buffer = self._from_bytes(buff)

    def write(self,
              path: str | pathlib.Path = None,
              buffer: bytes = None) -> None:
        if not (path or self.__path): raise NotSpecifiedFileException()
        buff = self._to_bytes(buffer or self.__buffer)
        file_handler.write_file(path or self.__path, buff)

    def _from_bytes(self, buffer: bytes, **kwargs) -> bytes:
        return buffer

    def _to_bytes(self, buffer: bytes, **kwargs) -> bytes:
        return buffer
