import pygame

from towerofbullets import TowerOfBullets

from screens.hud import Hud
from screens.pause import Pause


class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((800, 600))
        self.__screen = None
        self.game = TowerOfBullets(self.display)
        self.game.run()
        self.hud = Hud(self.display, self.game.player)
        self.last_pause = 0
        
    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        if pygame.time.get_ticks() - self.last_pause > 200:
            self.__screen = value
            self.last_pause = pygame.time.get_ticks()

    def start(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Tower of Bullets")
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            keyboard = pygame.key.get_pressed()
            if keyboard[pygame.K_p]:
                if self.screen is None:
                    self.screen = Pause(self.display)

            if self.screen is None:
                self.game.render()
                self.game.detect_collision()
                self.game.handle_input()
                self.hud.render(self.game.player)
            else:
                next_ = self.screen.render()
                if next_ is not None:
                    self.screen = None
            pygame.display.update()

        
    def quit(self):
        pygame.quit()

if __name__ == '__main__':
    g = Game()
    g.start()