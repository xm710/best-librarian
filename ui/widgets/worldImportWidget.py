from ui.widgets.baseWidget import BaseWidget
from ui.generated.worldImportGenerated import Ui_WorldImport
from ui.dialog.confirmDialog import select_world


class WorldImportWidget(BaseWidget):
    ui: Ui_WorldImport

    def __init__(self, world_service):
        super().__init__(Ui_WorldImport())

        self.world_service = world_service

    def reset(self):
        ui = self.ui

        ui.worldFolderPathLineEdit.clear()
        ui.browseButton.setChecked(False)
        ui.loadButton.setChecked(False)

    def bind_event(self):
        ui = self.ui

        ui.browseButton.clicked.connect(
            self.browser_button_on_click
        )
        ui.loadButton.clicked.connect(
            self.load_button_on_click
        )

    def browser_button_on_click(self):
        world_path = select_world()
        self.ui.worldFolderPathLineEdit.setText(world_path)

    def load_button_on_click(self):
        world_path = self.ui.worldFolderPathLineEdit.text()
        self.world_service.load_world(world_path)
        print(self.world_service.world)