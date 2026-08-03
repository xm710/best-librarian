from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from ui.generated.worldImportGenerated import Ui_WorldImport
from ui.dialog.confirmDialog import select_world


class WorldImportWidget(QWidget):
    world_loaded = Signal()

    def __init__(self, app_service):
        super().__init__()
        self.ui = Ui_WorldImport()
        self.ui.setupUi(self) # type: ignore[reportUnknownMemberType]

        self.app_service = app_service
        
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
        self.app_service.world_service.open_world(world_path)
        self.world_loaded.emit()