from amulet.api.chunk import EntityList
from amulet.api.entity import Entity
from amulet.api.level import World

from lib.minecraft.coordinate import block_to_chunk, position_to_block


class VillagerService:
    def __init__(self):
        pass

    def get_villagers_by_block(self, world: World, x: int, y: int, z: int):
        """
        由方塊座標搜尋村民
        """
        cx, cz = block_to_chunk(x, z)
        entities, _ = world.get_native_entities(cx, cz, "minecraft:overworld")
        villagers = self._filter_villagers(entities)
        villagers = self._filter_villagers_by_block(villagers, x, y, z)

        return villagers

    def _filter_villagers(self, entities: EntityList):
        """
        篩選出村民
        """
        return [
            entity
            for entity in entities.__iter__()
            if entity.namespaced_name == "minecraft:villager"
        ]

    def _filter_villagers_by_block(
        self, villagers: list[Entity], x: int, y: int, z: int
    ):
        """
        篩選出位於特定位置的村民
        """
        return [
            villager
            for villager in villagers
            if position_to_block(*villager.location) == (x, y, z)
        ]
