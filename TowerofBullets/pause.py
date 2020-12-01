import pygame
from entity import Entity


class PauseView:

    def __init__(self, screen_size, fps=60):
        self.width, self.height = screen_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = fps

        self.rodando = True

        self.inicio = Entity(self.screen, (170, 300),
                             (200, 75), 0, 'misc/inicio.png')
        self.loja = Entity(self.screen, (420, 300),
                           (200, 75), 0, 'misc/loja.png')
        self.play = Entity(self.screen, (344, 170),
                           (102, 117), 0, 'misc/pause/play.png')

        def run(self):
            pygame.init()
            pygame.display.init()
            pygame.display.set_caption("Tower of Bullets - Pause")

        while self.rodando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handlePress(event.pos)

            self.render()

    def handlePress(self, pos_mouse):
        pass

    def render(self):

        self.screen.blit(self.inicio.image, (170, 300))
        self.screen.blit(self.loja.image, (420, 300))
        self.screen.blit(self.play.image, (344, 170))
        pygame.display.update()

    def quit(self):
        pygame.quit()


if __name__ == '__main__':
    pause = PauseView((800, 600))
    pause.run()
