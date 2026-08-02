from lib.minecraft.coordinate import block_to_chunk, position_to_block

class VillagerService:
    def __init__(self, world_service):
        self.world_service = world_service
    
    def get_villagers_by_block(self, x, y, z):
        cx, cz = block_to_chunk(x, z)
        entities, _ = self.world_service.world.get_native_entities(cx, cz, "minecraft:overworld")
        villagers = self._filter_villagers(entities)
        villagers = self._filter_villagers_by_block(villagers, x, y, z)

        return villagers

    def _filter_villagers(self, entities):
        return [
            entity
            for entity in entities
            if entity.namespaced_name == "minecraft:villager"
        ]

    def _filter_villagers_by_block(self, villagers, x, y, z):
        return [
            villager
            for villager in villagers
            if position_to_block(*villager.location) == (x, y, z)
        ]