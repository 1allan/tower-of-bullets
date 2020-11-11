from scenario import Scenario
import pygame


class Lobby(Scenario):
    def __init__(self, position: tuple, size: tuple, structure: str,
                 shop_image_file: str):
        super().__init__(position, size, structure)
        self.shop = pygame.image.load(shop_image_file)
