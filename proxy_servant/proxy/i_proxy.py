from dataclasses import dataclass
from abc import abstractmethod, ABC

@dataclass
class IProxy(ABC):
    protocol: str
    url: str
    port: int
    login: str = None
    password: str = None

    @abstractmethod
    def __str__(self):
        "Returns connection string in format {{ protocol }}://{{ login }}:{{ password }}@{{ url }}:{{ port }}"
