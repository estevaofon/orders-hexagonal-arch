# ports/repository.py
from abc import ABC, abstractmethod

class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, order):
        pass
