from abc import ABC, abstractmethod
from api_hub.schemas import RequestModel, ResponseModel


class AbstractClientExceptionHandler(ABC):
    """class to handle general exception at the end of the process """

    @staticmethod
    @abstractmethod
    def manage(request: RequestModel, response: ResponseModel):
        """passing response and the exception to service call"""

