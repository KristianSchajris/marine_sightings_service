
from src.interface.controller_interface import ControllerInterface


class BaseController(ControllerInterface):
    def __init__(self, service):
        self.service = service

    def create(self, **kwargs):
        return self.service.create(**kwargs)
    
    def get(self, **kwargs):
        return self.service.get(**kwargs)
    
    def update(self, **kwargs):
        return self.service.update(**kwargs)
    
    def delete(self, **kwargs):
        return self.service.delete(**kwargs)
