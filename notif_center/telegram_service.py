from types import SimpleNamespace
from typing import Dict, Any

import requests
from django.conf import settings

from api_hub.notif_center.abstract_service import AbstractContactService


class TelegramServie(AbstractContactService): #TODO: shall we use the abstract client here too !!!
    _TELEGRAM_TOKEN = settings.API_HUB_TELEGRAM_NOTIF_TOKEN
    _TELEGRAM_CHAT_ID = settings.API_HUB_TELEGRAM_NOTIF_CHAT_ID
    _TELEGRAM_THREAD_ID = getattr(settings,'API_HUB_TELEGRAM_NOTIF_THREAD_ID', None)

    def send(self, text):
        url = f"https://api.telegram.org/bot{self._TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": self._TELEGRAM_CHAT_ID,
            "text": text,
            "disable_web_page_preview": True  # Set to True to disable preview
        }
        if self._TELEGRAM_THREAD_ID:
            payload["message_thread_id"]= self._TELEGRAM_THREAD_ID

        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
        except Exception as e:
            raise e
        return response.json()

    def send_exception_notif(self, data:Dict[str,Any]) -> None:
        text = self.format_message_for_telegram_for_service_api_log(data)
        self.send(text)

    @staticmethod
    def format_message_for_telegram_for_service_api_log(data:Dict) -> str:
        data = SimpleNamespace(**data)
        env_name = "Production" if settings.ENVIRONMENT == 'PRO' else "Development"

        text = (
            f"🔔 *Service API Log * 🔔\n"
            f"🔔 *Service * 🔔\n"
            f"🛠️ *Service Name:* {data.service_name}\n"
            f"🔗 *Endpoint:* {data.endpoint}\n"
            # f"🔄 *Third Party:* {data.third_party or 'N/A'}\n" 
            f"📩 *Request Data:* ```{data.request_data}```\n"
            f"📨 *Response Data:* ```{data.response_data}```\n"
            f"📊 *Status:* {data.status_code}\n"
            f"📊 *Errors:* {data.error}\n"
            f"🏦 *Environment:* {env_name}\n"
        )
        return text
