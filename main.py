from amulet import load_level
from amulet_nbt import (
    StringTag
)

import copy

level = load_level("C://Users/Owner/Desktop/.minecraft/versions/26.2-Fabric 0.19.3/saves/新的世界")

entities, version = level.get_native_entities(0, 0, "minecraft:overworld")

villager = entities[0]
nbt = villager.nbt



level.set_native_entites(0, 0, "minecraft:overworld", entities)

level.save()
level.close()