from PySide6.QtWidgets import QApplication, QWidget

from ui.generated.modifyLibrarianGenerated import Ui_ModifyLibrarian

def preview():
    app = QApplication.instance() or QApplication([])

    widget = QWidget()

    ui = Ui_ModifyLibrarian()
    ui.setupUi(widget)

    widget.show()

    app.exec()


if __name__ == "__main__":
    preview()