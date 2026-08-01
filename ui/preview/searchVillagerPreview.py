from PySide6.QtWidgets import QApplication, QWidget

from ui.generated.searchVillagerGenerated import Ui_SearchVillager
from ui.generated.modifyLibrarianGenerated import Ui_ModifyLibrarian


def preview():
    app = QApplication.instance() or QApplication([])

    widget = QWidget()
    ui = Ui_SearchVillager()
    ui.setupUi(widget)

    modifywidget = QWidget()
    modifyUI = Ui_ModifyLibrarian()
    modifyUI.setupUi(modifywidget)
    
    ui.modifyVillagerLayout.addWidget(modifywidget)
    widget.show()
    app.exec()

if __name__ == "__main__":
    preview()