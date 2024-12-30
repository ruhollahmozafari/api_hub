from asgiref.sync import sync_to_async
from celery import shared_task

from api_hub.schemas import RequestModel, ResponseModel
from .abstract_client_logger import AbstractClientLogger
from ..models import ServiceAPILog


class DatabaseClientLogger(AbstractClientLogger):
    """Logger implementation that saves logs to the database."""

    @staticmethod
    def make_log(request: RequestModel, response: ResponseModel):
        data = {
            "service_name": request.url.unicode_host(),
            "endpoint": request.url.unicode_string(),
            "request_data": request.data,
            "response_data": response.data,
            "status_code": response.status_code,
            'ok': response.ok,
            # "error": str(response.error) if response.error else '-',
        }
        save_service_api_log.delay(data)

@shared_task
def save_service_api_log(data):
    ServiceAPILog.objects.create(** data)
