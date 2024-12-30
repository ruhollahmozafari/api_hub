# Define the Pydantic models for request and response
import json
from typing import Any, Dict, Optional
import requests
from pydantic import BaseModel, HttpUrl, root_validator, model_validator


class RequestModel(BaseModel):
    url: HttpUrl
    method: str
    headers: Dict[str, Any] | None = None
    params: Dict[str, Any] | None = None
    data: Dict[str, Any] | None = None



class ResponseModel(BaseModel):
    status_code: int
    headers: Dict[str, Any] = {}
    data: Any = None
    error: Optional[Exception] = None  # Include error details if any
    ok: bool = True


    @model_validator(mode="after")
    def validate_error(self):
        if self.error is not None and not isinstance(self.error, Exception):
            raise ValueError("The 'error' field must be an instance of Exception")
        return self

    class Config:
        arbitrary_types_allowed = True

    def json(self, *args, **kwargs) -> Any:
        if isinstance(self.data, (dict, list)):
            return self.data
        if not self.data:
            return None
        try:
            return json.loads(self.data)
        except json.decoder.JSONDecodeError as e:
            raise e

    @property
    def text(self) -> str:
        return str(self.data)
