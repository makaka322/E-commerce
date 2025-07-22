from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def __str__(self):
        pass

