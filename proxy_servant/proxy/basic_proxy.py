from .i_proxy import IProxy
from dataclasses import dataclass

@dataclass
class BasicProxy(IProxy):
    def __str__(self):
        "Returns connection string in format "
        if self.login and self.password:
            return f"{ self.protocol }://{ self.login }:{ self.password }@{ self.url }:{ self.port }"
        else:
            return f"{ self.protocol }://{ self.url }:{ self.port }"
    
    @staticmethod
    def from_url(url: str):
        protocol, other = url.split("://")

        if other.count("@") > 0:
            creds, conn_string = other.split("@")

            return BasicProxy(protocol, *(conn_string.split(":")), *(creds.split(":")))

        else:
            return BasicProxy(protocol, *(other.split(":")))


