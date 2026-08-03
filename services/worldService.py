from lib.amulet.fileIO import open_world, save_world, close_world
from ui.dialog.warningDialog import wrong_level_file

# type
from models.worldContext import WorldContext

class WorldService:
    def __init__(self, context: WorldContext):
        self.context = context

    def open_world(self, path: str) -> None:
        """
        打開根據path選擇的世界檔案
        """
        try:
            self.context.world = open_world(path)
        except Exception as e:
            wrong_level_file(e)

    def close_world(self) -> None:
        """
        儲存並關閉世界檔案
        """
        if self.context.world:
            save_world(self.context.world)
            close_world(self.context.world)