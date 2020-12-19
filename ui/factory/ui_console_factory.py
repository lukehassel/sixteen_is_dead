__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from ui.factory.ui_factory import UIFactory
from ui.ui_console_impl import UIConsoleImpl


class UIConsoleFactory(UIFactory):
    def initUI(self):
        return UIConsoleImpl()
