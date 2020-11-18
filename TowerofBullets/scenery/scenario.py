from abc import ABC, abstractmethod
from utils import *

import pygame

class Scenario(ABC):

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, image_path: str):
        self.x, self.y = position
        self.width, self.height = size
        self.surface = surface
        self.background = load_image(image_path, size)

        self.walkablePad = [14, 14, 780, 553] # pode andar
        self.pads = [
            pygame.Rect(0, 0, 14, 600),
            pygame.Rect(0, 0, 800, 14),
            pygame.Rect(786, 0, 14, 600),
            pygame.Rect(0, 560, 800, 42)
        ]

        # self.pixelarray = pygame.PixelArray(open('stages/1.txt', 'rb'))
        # self.structure = pygame.self.pixelarray.make_surface()        # self.pixelarray = pygame.PixelArray(open('stages/1.txt', 'rb'))