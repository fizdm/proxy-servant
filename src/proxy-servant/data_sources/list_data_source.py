from typing import List
from .i_data_source import IDataSource


class ListDataSource(IDataSource):
    def __init__(self, list_source: List[str]):
        self._list_source = list_source
        self._idx = -1

    def get_all_data(self) -> List[str]:
        return self._list_source

    def __iter__(self):
        return self

    def __next__(self):
        self._idx += 1
        try:
            return self._list_source[self._idx]
        except IndexError:
            self._idx = -1
            raise StopIteration
