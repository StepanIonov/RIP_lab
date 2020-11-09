from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def space(self):
        pass
