from abc import ABC, abstractmethod
from typing import Optional

class ClientRepository(ABC):
    @abstractmethod
    def save(self):
        pass

