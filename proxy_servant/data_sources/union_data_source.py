from typing import List
from .i_data_source import IDataSource
from .list_data_source import ListDataSource
from itertools import chain
from ..proxy import IProxy


class UnionDataSource(ListDataSource):
    def __init__(self, data_sources: List[IDataSource]):
        super().__init__(UnionDataSource.transform_to_one_list(data_sources))

    def transform_to_one_list(data_sources: List[IDataSource]) -> List[IProxy]:
        return list(set(chain.from_iterable(data_sources)))
