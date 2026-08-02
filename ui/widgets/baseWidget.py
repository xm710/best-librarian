from PySide6.QtWidgets import QWidget

class BaseWidget(QWidget):
    def __init__(self, ui):
        super().__init__()

        self.ui = ui
        self.ui.setupUi(self)

        self.bind_event()

    def bind_event(self):
        pass