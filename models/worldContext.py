# type
from typing import cast

from amulet.api.level import World

class WorldContext:
    def __init__(self) -> None:
        self._world: World | None = None

    def get_world(self):
        return cast(World, self._world)