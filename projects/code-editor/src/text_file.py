from . import file


class TextFile(file.File):
    encoding = "ascii"

    def _from_bytes(self,
                    buffer: bytes,
                    encoding: str = None,
                    **kwargs) -> str:
        return buffer.decode(encoding or self.encoding)

    def _to_bytes(self, buffer: str, encoding: str = None, **kwargs) -> bytes:
        return buffer.encode(encoding or self.encoding)