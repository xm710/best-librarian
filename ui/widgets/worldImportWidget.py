from PySide6.QtCore import Signal

from ui.widgets.baseWidget import BaseWidget
from ui.generated.worldImportGenerated import Ui_WorldImport
from ui.dialog.confirmDialog import select_world


class WorldImportWidget(BaseWidget):
    ui: Ui_WorldImport

    world_loaded = Signal()

    def __init__(self, world_service):
        super().__init__(Ui_WorldImport())

        self.world_service = world_service
        
        self.bind_event()

    def reset(self):
        self.ui.worldFolderPathLineEdit.clear()
        self.ui.browseButton.setChecked(False)
        self.ui.loadButton.setChecked(False)

    def bind_event(self):
        self.ui.browseButton.clicked.connect(
            self.browser_button_on_click
        )
        self.ui.loadButton.clicked.connect(
            self.load_button_on_click
        )

    def browser_button_on_click(self):
        world_path = select_world()
        self.ui.worldFolderPathLineEdit.setText(world_path)

    def load_button_on_click(self):
        world_path = self.ui.worldFolderPathLineEdit.text()
        self.world_service.open_world(world_path)
        self.world_loaded.emit()