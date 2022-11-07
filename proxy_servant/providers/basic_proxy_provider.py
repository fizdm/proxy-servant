from ..data_sources import IDataSource
from .i_proxy_provider import IProxyProvider
from ..proxy_checker import ProxyCheckResponse
from ..proxy import IProxy
from typing import List

class InsufficientProxyCount(Exception):
    ...

class BasicProxyProvider(IProxyProvider):
    def __init__(self, proxy_check_result: List[ProxyCheckResponse], remove_proxy_after_use: bool = False):
        self._data = BasicProxyProvider.extract_proxy_from_check(proxy_check_result)

        if len(self._data) == 0:
            raise ValueError("Non of provided proxies are working")

        self._idx = 0
        self._remove_proxy_after_use = remove_proxy_after_use

    @staticmethod
    def extract_proxy_from_check(proxy_check_result: List[ProxyCheckResponse], only_working: bool = True):
        return [proxy_res.proxy for proxy_res in proxy_check_result if (proxy_res.is_succeed if only_working else True)]

    def report_dead_proxy(self, dead_proxy: IProxy):
        self._data = [proxy for proxy in self._data if proxy != dead_proxy]

    def get_all(self) -> List[IProxy]:
        return self._data[:]
        
    def __iter__(self):
        return self

    def __next__(self):
        if len(self._data) == 0:
            raise StopIteration

        if self._idx > len(self._data) - 1:
            self._idx = 0
    
        if self._remove_proxy_after_use:
            proxy = self._data.pop(self._idx)
        else:
            proxy = self._data[self._idx]

        self._idx += 1
        return proxy
