from abc import ABC, abstractmethod

class PaginatedCollectionInterface(ABC):

    @abstractmethod
    def total_pages(self):
        pass