import pygame

from entity import Entity
from util.functions import *

from towerofbullets import TowerOfBullets
from config import ConfigView


class StartView:

    def __init__(self, screen_size: tuple, fps=60):
        self.width, self.height = screen_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = fps

        self.bg = load_image('misc/start/bg.png', screen_size)
        self.play = Entity(self.screen, (170, 300),
                           (200, 75), 0, 'misc/start/play.png')
        self.config = Entity(self.screen, (420, 300),
                             (200, 75), 0, 'misc/start/config.png')
        self.exit = Entity(self.screen, (680, 100),
                           (60, 60), 0, 'misc/start/exit.png')

    def run(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Tower of Bullets - Start")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handlePress(event.pos)

            self.render()

    def handlePress(self, pos_mouse):
        x, y = pos_mouse

        if self.play.rect.collidepoint(x, y):
            # iniciar towerofbullets
            game = TowerOfBullets((800, 600))
            game.run()

        elif self.config.rect.collidepoint(x, y):
            # iniciar config
            config = ConfigView((800, 600))
            config.run()

        elif self.exit.rect.collidepoint(x, y):
            # sair do programa
            self.quit()

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        self.screen.blit(self.play.image, (170, 300))
        self.screen.blit(self.config.image, (420, 300))
        self.screen.blit(self.exit.image, (680, 100))
        pygame.display.update()

    def quit(self):
        pygame.quit()


if __name__ == '__main__':
    start = StartView((800, 600))
    start.run()
