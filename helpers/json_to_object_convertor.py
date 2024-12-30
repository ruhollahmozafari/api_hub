import json
import logging
from functools import wraps
from types import SimpleNamespace

from api_hub.schemas import ResponseModel

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def json_response_to_object(func):
    """Decorator to convert JSON response to a Python object or return None for specific cases."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        response :ResponseModel= func(*args, **kwargs)
        logger.info('Converting response ...')
        # Check if the response has a status code
        if hasattr(response, "status_code"):
            # Return None for 404 status
            if response.status_code == 404:
                return None

            # Process successful response
            if response.ok:
                try:
                    # Convert the JSON content to an object, return None if empty
                    if not response.data:  # Check for empty JSON
                        return None
                    obj = SimpleNamespace(**response.data)
                    logger.info(f'converted response to obj {obj=}')
                    return obj
                except json.JSONDecodeError:
                    return None  # Return None if JSON parsing fails

        # Return raw response for other status codes
        logger.info('response has not status, return response it self')
        return response
    return wrapper
