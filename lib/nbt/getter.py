# type
from amulet_nbt import CompoundTag

def fast_get_compound(tag: CompoundTag, keys: list[str]) -> CompoundTag:
    """
    快速取得目標 CompoundTag
    """
    if len(keys):
        return fast_get_compound(tag.get_compound(keys[0]), keys[1:])
    else:
        return tag