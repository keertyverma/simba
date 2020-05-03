"""
Base Abstract class to crawl data from any host.

"""

from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """
    APIs base methods.
    """
    @abstractmethod
    def get_url(self) -> str:
        pass

    @abstractmethod
    def process_import(self) -> int:
        pass

    @abstractmethod
    def make_api_call(self):
        pass
