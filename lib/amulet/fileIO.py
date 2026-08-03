from amulet import load_level
from amulet.api.level import World


def open_world(path: str) -> World:
    """
    開啟以 path 為目標的世界
    """
    world = load_level(path)

    assert isinstance(world, World)

    return world


def close_world(world: World):
    """
    關閉 world
    """
    world.close()


def save_world(world: World):
    """
    儲存 world
    """
    world.save()  # type: ignore[reportUnknownMemberType]
