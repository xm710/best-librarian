from PySide6.QtCore import QStringListModel

from ui.widgets.baseWidget import BaseWidget
from ui.generated.modifyLibrarianGenerated import Ui_ModifyLibrarian

class ModifyLibrarianWidget(BaseWidget):
    ui: Ui_ModifyLibrarian

    def __init__(self):
        super().__init__(Ui_ModifyLibrarian())
        self.enchantsListViewModel = QStringListModel([])
        self.ui.enchantsListView.setModel(self.enchantsListViewModel)

    def reset(self):
        ui = self.ui

        for i in range(ui.gridLayout.count()):
            ui.gridLayout.itemAt(i).widget().setChecked(False)

        self.enchantsListViewModel.setStringList([])

        ui.enchantNameLV1.clear()
        ui.enchantNameLV2.clear()
        ui.enchantNameLV3.clear()
        ui.enchantNameLV4.clear()

        ui.enchantLevelLV1.setValue(0)
        ui.enchantLevelLV2.setValue(0)
        ui.enchantLevelLV3.setValue(0)
        ui.enchantLevelLV4.setValue(0)

        ui.enchantPriceLV1.setValue(0)
        ui.enchantPriceLV2.setValue(0)
        ui.enchantPriceLV3.setValue(0)
        ui.enchantPriceLV4.setValue(0)

        ui.saveButton.setChecked(False)