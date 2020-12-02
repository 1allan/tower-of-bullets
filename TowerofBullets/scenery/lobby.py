import pygame

from scenario import Scenario


class Lobby(Scenario):
    
    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, 
                 image_path: str, shop_image_file: str):
        
        super().__init__(surface, position, size, image_path)
        
        self.shop = pygame.image.load(shop_image_file)
