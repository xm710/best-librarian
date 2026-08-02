from amulet.api.errors import LoaderNoneMatched

from lib.amulet.fileIO import World
from ui.dialog.warningDialog import wrong_level_file

class WorldService:
    def __init__(self):
        self.world = None

    def open_world(self, path):
        try:
            self.world = World._open_world(path)
        except Exception as e:
            wrong_level_file(e)

    def close_world(self):
        if self.world:
            World._save_world(self.world)
            World._close_world(self.world)