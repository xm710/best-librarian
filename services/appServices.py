from services.librarianService import LibrarianService
from services.villagerService import VillagerService
from services.worldService import WorldService


class AppServices:
    def __init__(self):
        self.world_service = WorldService()
        self.villager_service = VillagerService()
        self.librarian_service = LibrarianService()
