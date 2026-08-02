import json
from pathlib import Path

_JSON_PATH = Path(__file__).parent.parent.parent / "data" / "enchantments.json"

with open(_JSON_PATH, "r", encoding="utf-8") as f:
    _ENCHANTMENTS = json.load(f)

def get_enchantment_data_by_namespace_name(namespace_name):
    return _ENCHANTMENTS[namespace_name.replace("minecraft:", "")]

def get_max_price(level, is_treasure):
    return min(64, (level * 13 + 6) * 2) if is_treasure else min(64, (level * 13 + 6))

def get_min_price(level, is_treasure):
    return (level * 3 + 2) * 2 if is_treasure else (level * 3 + 2)