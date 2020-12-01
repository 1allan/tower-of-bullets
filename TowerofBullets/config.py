import pygame

from util.functions import *
from entity import Entity


class ConfigView:
    def __init__(self, screen_size: tuple, fps=60):
        self.width, self.height = screen_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = fps

        self.bg = load_image('misc/config/bg.png', screen_size)
        self.config = Entity(self.screen, (131, 50),
                             (500, 50), 0, 'misc/config/config.png')
        self.back = Entity(self.screen, (28, 50), (64, 64),
                           0, 'misc/config/voltar.png')

    def run(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Tower of Bullets - Configurações")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handlePress(event.pos)

            self.render()

    def handlePress(self, pos_mouse):
        x, y = pos_mouse

        if self.back.rect.collidepoint(x, y):
            pass

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        self.screen.blit(self.config.image, (131, 50))
        self.screen.blit(self.back.image, (28, 50))
        pygame.display.update()

    def quit(self):
        pygame.quit()


if __name__ == "__main__":
    config = ConfigView((800, 600))
    config.run()
