import pygame

class Screen:

    # duration = -1 -> until it be destroyed
    def __init__(self, surface: pygame.Surface, position=None, size=None, duration=-1):
        self.surface = surface
        self.x, self.y = [0, 0] if position is None else position
        self.width, self.height = surface.get_size() if size is None else size
        self.duration = -1
        self.data = None

    def update(self, data):
        pass

    def draw(self):
        pass