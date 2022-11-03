from ..data_sources import IDataSource
from .i_proxy_provider import IProxyProvider


class ProxyProvider(IProxyProvider):
    '''
        parsing_strategy -- callable object which returns ip address or proxy
    '''

    def __init__(self, data_source: IDataSource, parsing_strategy=lambda proxy: proxy):
        self._idx = -1
        self._data_source = data_source
        self._parsing_strategy = parsing_strategy

    def __iter__(self):
        iter(self._data_source)
        return self

    def __next__(self):
        return self._parsing_strategy(next(self._data_source))
