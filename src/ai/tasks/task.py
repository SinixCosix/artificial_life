from abc import ABC, abstractmethod


class Task(ABC):
    @abstractmethod
    def do(self, *args, **kwargs) -> bool:
        pass
