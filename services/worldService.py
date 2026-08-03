from amulet.api.errors import LoaderNoneMatched

from lib.amulet.fileIO import close_world, open_world, save_world
from models.worldContext import WorldContext
from ui.dialog.warningDialog import wrong_level_file


class WorldService:
    def __init__(self) -> None:
        self.context = WorldContext()

    def open_world(self, path: str) -> None:
        """
        打開根據path選擇的世界檔案
        """
        try:
            self.context.set_world(open_world(path))
        except LoaderNoneMatched as e:
            wrong_level_file(e)

    def close_world(self) -> None:
        """
        儲存並關閉世界檔案
        """
        if self.context.get_world():
            save_world(self.context.get_world())
            close_world(self.context.get_world())
