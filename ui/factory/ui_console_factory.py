from ui.factory.ui_factory import UIFactory
from ui.ui_console_impl import UIConsoleImpl


class UIConsoleFactory(UIFactory):
    def initUI(self):
        return UIConsoleImpl()
