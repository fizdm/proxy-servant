from typing import List
from .i_data_source import IDataSource


class FileDataSource(IDataSource):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def get_all_data(self) -> List[str]:
        return self._file.readlines()

    def __iter__(self):
        self._file = open(self._file_path, "r")
        return self

    def __next__(self):
        line = self._file.readline().rstrip()

        if line == "":  # EOF
            self._file.close()
            raise StopIteration
        else:
            return line
