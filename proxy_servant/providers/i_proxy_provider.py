from abc import abstractmethod, ABC
from ..proxy import IProxy

class IProxyProvider(ABC):
    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self) -> IProxy:
        ...
