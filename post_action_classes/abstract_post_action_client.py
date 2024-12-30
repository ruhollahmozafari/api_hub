from abc import ABC, abstractmethod

from api_hub.schemas import RequestModel, ResponseModel


class AbstractPostActionClient(ABC):
    """classes that will be called after http calls,
    note: the passed response might be ok or nokey, """

    @staticmethod
    @abstractmethod
    def do(request: RequestModel, response: ResponseModel):
        """passing a request and a response to this method will manage log for those objects"""

