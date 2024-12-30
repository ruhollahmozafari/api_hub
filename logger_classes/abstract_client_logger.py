from abc import ABC, abstractmethod

from api_hub.schemas import RequestModel, ResponseModel


class AbstractClientLogger(ABC):
    """class to handle general exception at the end of the process """

    @staticmethod
    @abstractmethod
    def make_log(request: RequestModel, response: ResponseModel):
        """passing a request and a response to this method will manage log for those objects"""

