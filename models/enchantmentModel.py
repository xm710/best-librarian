class Enchantment:
    def __init__(self, namespace_name: str, level: int):
        self.namespace_name = namespace_name
        self.level = level

    def __repr__(self):
        return f"{self.namespace_name} {self.level}"
