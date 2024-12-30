from asgiref.sync import sync_to_async

from api_hub.schemas import RequestModel, ResponseModel
from .abstract_post_action_client import AbstractPostActionClient
from ..models import ServiceAPILog


class DoAPostActionExcample(AbstractPostActionClient):
    """Logger implementation that saves logs to the database."""


    @staticmethod
    def do(request: RequestModel, response: ResponseModel):
        """just an example post action"""
        print(f'*'*10)
        print(f'\nhere is the example post action here \n',)
        print(f'*'*10)
