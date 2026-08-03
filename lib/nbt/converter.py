from amulet_nbt import CompoundTag, IntTag

from typing import Iterable, cast, ItemsView


def int_items(tag: CompoundTag) -> Iterable[tuple[str, IntTag]]:
    """
    將未知的 ConpoundTag 轉成資料為 IntTag 的 CompoundTag
    """
    items = cast(ItemsView[str, IntTag], tag.items())

    for key, value in items:
        yield key, value