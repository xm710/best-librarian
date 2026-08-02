from PySide6.QtWidgets import QWidget

class BaseWidget(QWidget):
    def __init__(self, ui):
        super().__init__()

        self.ui = ui
        self.ui.setupUi(self)

    def bind_event(self):
        pass