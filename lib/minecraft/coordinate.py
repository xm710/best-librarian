def block_to_chunk(x: int, z: int) -> tuple[int, int]:
    """
    把方塊座標轉為 chunk 座標
    """
    return x // 16, z // 16


def position_to_block(x: float, y: float, z: float) -> tuple[int, int, int]:
    """
    將生物座標轉為方塊座標
    """
    return int(x // 1), int(y // 1), int(z // 1)
