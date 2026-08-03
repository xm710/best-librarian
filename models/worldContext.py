from typing import cast

from amulet.api.level import World


class WorldContext:
    def __init__(self) -> None:
        self._world: World | None = None

    def get_world(self) -> World:
        """
        取得唯一 World 型別 world
        """
        return cast(World, self._world)

    def set_world(self, world: World) -> None:
        """
        設定 World
        """
        self._world = world
