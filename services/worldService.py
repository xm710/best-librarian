from amulet.api.errors import LoaderNoneMatched

from lib.amulet.fileIO import open_world
from ui.dialog.warningDialog import wrong_level_file

class WorldService:
    def __init__(self):
        self.world = None

    def load_world(self, path):
        try:
            self.world = open_world(path)
        except Exception as e:
            wrong_level_file(e)