import abc
from abc import ABC


class AbstractContactService(ABC):

    @abc.abstractmethod
    def send(self, text):
        """send data"""

