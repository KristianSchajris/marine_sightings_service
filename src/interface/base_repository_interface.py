from abc import abstractmethod

from abc import ABC, abstractmethod

class BaseRepositoryInterface(ABC):

    @abstractmethod
    def create(self, model):
        pass

    @abstractmethod
    def get(self, model_class, model_id: int):
        pass
    
    @abstractmethod
    def get_all(self, model_class):
        pass
    
    @abstractmethod
    def update(self, model_instance, **kwargs):
        pass
    
    @abstractmethod
    def delete(self, model_instance):
        pass
