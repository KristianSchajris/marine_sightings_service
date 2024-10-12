
from abc import ABC, abstractmethod


class ControllerInterface(ABC):

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def get(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self, **kwargs):
        pass