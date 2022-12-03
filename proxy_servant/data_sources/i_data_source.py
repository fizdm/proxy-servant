from abc import abstractmethod, ABC
from typing import List
from ..proxy import IProxy

class IDataSource(ABC):
    @abstractmethod
    def get_all_data(self) -> List[IProxy]:
        ...

    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self) -> IProxy:
        ...
