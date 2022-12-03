from typing import List
from .i_data_source import IDataSource
from ..proxy import IProxy, BasicProxy


class FileDataSource(IDataSource):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def get_all_data(self) -> List[IProxy]:
        with open(self._file_path) as file:
            return [BasicProxy.from_url(line.rstrip()) for line in file.readlines()]

    def __iter__(self):
        self._file = open(self._file_path, "r")
        return self

    def __next__(self) -> IProxy:
        line = self._file.readline().rstrip()

        if line == "":  # EOF
            self._file.close()
            raise StopIteration
        else:
            return BasicProxy.from_url(line)
