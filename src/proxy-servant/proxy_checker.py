from . import IProxyProvider
import aiohttp
from aiosocksy.errors import SocksError
from aiosocksy.connector import ProxyConnector, ProxyClientRequest


class ProxyChecker:
    def __init__(self, proxy_iterator: IProxyProvider, endpoint_url: str, timeout: int = 3):
        self._proxy_iterator = proxy_iterator
        self._endpoint_url = endpoint_url
        self._timeout = aiohttp.ClientTimeout(connect=timeout)
        self._request_succeed = []

    def __aiter__(self):
        iter(self._proxy_iterator)

        connector = ProxyConnector()
        self._aio_session = aiohttp.ClientSession(
            timeout=self._timeout, connector=connector, request_class=ProxyClientRequest)
        return self

    async def __anext__(self):
        try:
            proxy = next(self._proxy_iterator)
            async with self._aio_session.get(self._endpoint_url, proxy=proxy) as response:
                return proxy
        except aiohttp.ClientError as e:
            print(e)
        except SocksError as e:
            print(e)
        except StopIteration:
            await self._aio_session.close()
            raise StopAsyncIteration
        except Exception as e:
            print(e)
