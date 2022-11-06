from abc import abstractmethod
from ..data_sources import IDataSource


class IProxyProvider:
    '''
        parsing_strategy -- callable object which returns ip address or proxy
    '''
    @abstractmethod
    def __init__(self, data_source: IDataSource, parsing_strategy):
        ...

    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self) -> str:
        ...

    @abstractmethod
    async def __next__(self) -> str:
        ...
