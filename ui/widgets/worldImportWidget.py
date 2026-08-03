from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from ui.dialog.confirmDialog import select_world
from ui.generated.worldImportGenerated import Ui_WorldImport

from services.appServices import AppServices


class WorldImportWidget(QWidget):
    world_loaded = Signal()

    def __init__(self, services: AppServices) -> None:
        super().__init__()
        self.ui = Ui_WorldImport()
        self.ui.setupUi(self)  # type: ignore[reportUnknownMemberType]

        self.services = services

        self.bind_event() # 開始監聽事件

    def reset(self) -> None:
        """
        重置元件
        """
        self.ui.worldFolderPathLineEdit.clear()
        self.ui.browseButton.setChecked(False)
        self.ui.loadButton.setChecked(False)

    def bind_event(self) -> None:
        """
        綁定事件
        """
        self.ui.browseButton.clicked.connect(self.browser_button_on_click)
        self.ui.loadButton.clicked.connect(self.load_button_on_click)

    def browser_button_on_click(self) -> None:
        """
        當按下瀏覽按鈕觸發 將路徑設定為選擇的資料夾
        """
        world_path = select_world()
        self.ui.worldFolderPathLineEdit.setText(world_path)

    def load_button_on_click(self) -> None:
        """
        當按下載入按鈕時觸發 載入以路徑為目標的世界
        """
        world_path = self.ui.worldFolderPathLineEdit.text()
        self.services.world_service.open_world(world_path)
        self.world_loaded.emit()
