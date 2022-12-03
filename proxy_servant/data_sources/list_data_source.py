from typing import List
from .i_data_source import IDataSource
from ..proxy import IProxy

class ListDataSource(IDataSource):
    def __init__(self, list_source: List[IProxy]):
        self._list_source = list_source
        self._idx = 0

    def get_all_data(self) -> List[IProxy]:
        return self._list_source

    def __iter__(self):
        return self

    def __next__(self):
        try:
            proxy = self._list_source[self._idx]
            self._idx += 1
            return proxy
        except IndexError:
            self._idx = 0
            raise StopIteration
