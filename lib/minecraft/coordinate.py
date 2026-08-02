def block_to_chunk(x, z):
    return x // 16, z // 16

def position_to_block(x, y, z):
    return x // 1, y // 1, z // 1