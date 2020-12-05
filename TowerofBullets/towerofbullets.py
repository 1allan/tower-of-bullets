import pygame
from time import time

from util.functions import load_image
from scenery.room import Room


class TowerOfBullets:

    def __init__(self, display, fps=60):
        self.surface = display
        self.width, self.height = self.surface.get_size()
        self.fps = fps
        self.room = None
        self.pause_group = None
        self.paused = False
        self.sprites = pygame.sprite.Group()
        self.current_screen = None
        self.last_pause = 0

    def run(self):
        self.room = Room(self.surface, self.sprites, (0, 0), (self.width,
                                               self.height), 0, False)

    def handle_input(self):
        keyboard = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        direction = [0, 0]
        if keyboard[pygame.K_a]:
            direction[0] = -1
        elif keyboard[pygame.K_d]:
            direction[0] = 1

        if keyboard[pygame.K_w]:
            direction[1] = -1
        elif keyboard[pygame.K_s]:
            direction[1] = 1

        self.room.player.move(direction)

        if mouse[0]:
            self.room.player.shoot()

    def render(self):
        self.handle_input()
        self.room.detect_collision()
        self.room.draw()
        self.sprites.draw(self.surface)
        self.sprites.update()
