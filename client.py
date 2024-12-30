from typing import Optional, Dict, Any, List
import requests
from pydantic import HttpUrl
from abc import ABC
from .exception_handlers import AbstractClientExceptionHandler
from .logger_classes.abstract_client_logger import AbstractClientLogger
from .post_action_classes import AbstractPostActionClient
from .schemas import RequestModel, ResponseModel


# Abstract client class
class AbstractClient(ABC):
    exception_header_classes : Optional[List[AbstractClientExceptionHandler]] = None
    logger_classes: Optional[List[AbstractClientLogger]] = None
    post_action_classes : Optional[List[AbstractPostActionClient]] = None

    def _request(self, request: RequestModel) -> requests.Response:
        """
        Internal method responsible for making HTTP calls.
        """
        response = requests.request(
                method=request.method,
                url=str(request.url),
                headers=request.headers,
                params=request.params,
                json=request.data,
            )

        return response

    def request(
        self,
        url: str,
        method: str = "GET",
        headers: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> ResponseModel:
        """
        Public method to handle the request and process the response.
        User provides simple arguments, which are used to construct the RequestModel.
        """
        request_model = RequestModel(
            url=HttpUrl(url),
            method=method.upper(),
            headers=headers,
            params=params,
            data=data,
        )

        try:
            # Construct the RequestModel from the provided arguments
            # Pass the constructed RequestModel to the private request method
            raw_response = self._request(request_model)

            # Process the raw response and return a ResponseModel
            response_model =  ResponseModel(
                status_code=raw_response.status_code,
                headers=dict(raw_response.headers),
                data=raw_response.json() if "application/json" in raw_response.headers.get("Content-Type", "") else raw_response.text,
                ok = True
            )
        except requests.RequestException as e:
            # Handle any exception from the requests library
            response_model =  ResponseModel(
                status_code=0,
                headers={},
                data=None,
                error= e,
                ok = False,
            )
        except Exception as e: # raise unknown error
            raise e

        # call logger classes for logging
        if self.logger_classes:  # Ensure the list is not None
            for logging_class in self.logger_classes:
                logging_class.make_log(request=request_model, response=response_model)

        if self.post_action_classes:
            for post_action_class in self.post_action_classes:
                post_action_class.do(request= request_model, response = response_model, )
            # call exception classes if response is not ok

        if not response_model.ok:
            if self.exception_header_classes:
                for exception_class in self.exception_header_classes:
                    exception_class.manage(request = request_model,
                                           response = response_model)

        return response_model


