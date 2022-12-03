import aiohttp
import asyncio
from aiosocksy.errors import SocksError
from aiosocksy.connector import ProxyConnector, ProxyClientRequest
from .i_proxy_checker import IProxyChecker, ProxyCheckResponse
from ..proxy import IProxy
from ..data_sources import IDataSource
from typing import List


class BasicProxyChecker(IProxyChecker):
    def __init__(self, proxies_to_check: IDataSource, endpoint_url: str, timeout: aiohttp.ClientTimeout = aiohttp.ClientTimeout(connect=5)):
        self._proxies_to_check = proxies_to_check
        self._endpoint_url = endpoint_url
        self._timeout = timeout

    async def check(self) -> List[ProxyCheckResponse]:
        self._connector = ProxyConnector()

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Cookie": "clientPrefs=||||lightg; userSymbolList=EOD+&DIT; userCookiePref=true; selectedsymbolindustry=EOD,; "
            "selectedsymboltype=EOD,EVERGREEN GLOBAL DIVIDEND OPPORTUNITY FUND COMMON SHARES OF BENEFICIAL INTEREST,NYSE; c_enabled$=true",
            "Connection": "keep-alive", }

        async with aiohttp.ClientSession(
                timeout=self._timeout, connector=self._connector, request_class=ProxyClientRequest, headers=headers) as aio_session:

            tasks = []

            for proxy in self._proxies_to_check:
                if proxy.protocol not in ["socks4", "socks5", "http"]:
                    raise ValueError(
                        "Only http, socks4 and socks5 proxies are supported")

                tasks.append(self._run_and_obtain(aio_session, self._endpoint_url, proxy))

            return await asyncio.gather(*tasks)

    async def _run_and_obtain(self, aio_session: aiohttp.ClientSession, endpoint_url: str, proxy: IProxy) -> ProxyCheckResponse:
        try:
            async with aio_session.get(endpoint_url, proxy=str(proxy)) as response:
                pcr = ProxyCheckResponse(proxy, response.ok, response.status, await response.text())

        except (aiohttp.ClientError, SocksError) as e:
            pcr = ProxyCheckResponse(proxy, False, -1, str(e))

        return pcr
