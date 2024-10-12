
# src/utilities/paginated_iterator.py

from src.interface.paginated_collection_interface import PaginatedCollectionInterface
from src.utilities.pagination.paginated_iterator import PaginatedIterator

class PaginatedCollection(PaginatedCollectionInterface):
    def __init__(self, items, page, page_size):
        self.items = items
        self.page = page
        self.page_size = page_size

    def __iter__(self):
        # Calcular el rango de elementos para la página actual
        start_index = (self.page - 1) * self.page_size
        end_index = start_index + self.page_size
        # Retornar un iterador sobre los elementos de la página actual
        return PaginatedIterator(self.items[start_index:end_index], self.page_size)

    def total_pages(self):
        return (len(self.items) + self.page_size - 1) // self.page_size  # Cálculo de total de páginas

