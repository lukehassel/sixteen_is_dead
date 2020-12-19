__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from abc import ABC, abstractmethod


class UIFactory(ABC):
    @abstractmethod
    def initUI(self):
        pass
