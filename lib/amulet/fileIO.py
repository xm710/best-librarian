from amulet import load_level

class World:
    @staticmethod
    def _open_world(path):
        return load_level(path)

    @staticmethod
    def _close_world(world):
        world.close()

    @staticmethod
    def _save_world(world):
        world.save()