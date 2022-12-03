from dataclasses import dataclass
from abc import abstractmethod, ABC
from ..proxy import IProxy
from typing import List

@dataclass
class ProxyCheckResponse:
    proxy: IProxy
    is_succeed: bool
    http_code: int
    msg: str

class IProxyChecker(ABC):
    @abstractmethod
    async def check(self) -> List[ProxyCheckResponse]:
        ...
        