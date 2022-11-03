from abc import abstractmethod
from typing import List


class IDataSource:
    @abstractmethod
    def get_all_data(self) -> List[str]:
        ...

    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self):
        ...
