from api_hub.exception_handlers.abstract_client_exception_handler import AbstractClientExceptionHandler
from api_hub.notif_center import TelegramServie
from api_hub.schemas import RequestModel, ResponseModel


class HandleExceptionBySendingNotifTelegram(AbstractClientExceptionHandler):
    """handle exception by sending the exception """

    @staticmethod
    def manage(request: RequestModel, response: ResponseModel):
        # Send notif
        telegram_service = TelegramServie()
        data = {
            "service_name": request.url.unicode_host(),
            "endpoint": request.url.unicode_string(),
            "request_data": request.data,
            "response_data": response.data,
            "status_code": response.status_code,
            "error": str(response.error) if response.error else '-',
        }
        telegram_service.send_exception_notif(data)

class HandleExceptionByOnlyRaising(AbstractClientExceptionHandler):
    """ handle exception by sending the exception """

    @staticmethod
    def manage(request: RequestModel, response: ResponseModel):
        print(f'{response=}')
        raise response.error


class ReturnNoneExceptionHandler(AbstractClientExceptionHandler):
    @staticmethod
    def manage(request: RequestModel, response: ResponseModel):
        """ do nothing just return None"""
        print(response.error)
        return None



class HandleExceptionByRetryRequest(AbstractClientExceptionHandler):
    """handle exception by retrying the request """

    @staticmethod
    def manage(request: RequestModel, response: ResponseModel):
        ...
