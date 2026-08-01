from PySide6.QtWidgets import QApplication

from ui.widgets.mainWindowWidget import MainWindow

def run():
    app = QApplication.instance() or QApplication([])

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    run()