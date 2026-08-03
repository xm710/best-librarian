from services.worldService import WorldService
from services.villagerService import VillagerService
from services.librarianService import LibrarianService

from models.worldContext import WorldContext

class AppServices:
    def __init__(self):
        self.world_service = WorldService(WorldContext())
        self.villager_service = VillagerService()
        self.librarian_service = LibrarianService()