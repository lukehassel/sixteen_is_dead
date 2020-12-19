from abc import ABC, abstractmethod


class UIFactory(ABC):
    @abstractmethod
    def initUI(self):
        pass