from PySide6.QtWidgets import QApplication, QWidget

from ui.generated.worldImportGenerated import Ui_WorldImport


def preview():
    app = QApplication.instance() or QApplication([])

    widget = QWidget()

    ui = Ui_WorldImport()
    ui.setupUi(widget)

    widget.show()

    app.exec()


if __name__ == "__main__":
    preview()