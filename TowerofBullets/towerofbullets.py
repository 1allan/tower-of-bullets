import pygame

from character.player import Player
from scenery.room import Room

class TowerOfBullets:
    
    def __init__(self, screen_size, fps=60):
        self.width, self.height = screen_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = fps

        # self.rooms = []

        self.room = None
        self.player = None
        self.paused = False
    
    def start(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Tower of Bullets")
        
        self.room = Room(self.screen, (0, 0), (self.width, self.height), 'scenery/01.png', 0, 0, False)
        self.player = Player(self.screen, (self.width/2, self.height/2), (70, 70), 5, 'placeholder.png', 200, 200, 200)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                  self.player.shoot()

            if not self.paused:
                self.render()

            for index, pad in enumerate(self.room.pads):
                # parede esquerda
                if self.player.rect.colliderect(pad) and index == 0:
                    self.player.move((1, 0))

                # parede inferior
                elif self.player.rect.colliderect(pad) and index == 1:
                    self.player.move((0, 1))

                # parede direita
                elif self.player.rect.colliderect(pad) and index == 2:
                    self.player.move((-1, 0))

                # parede superior
                elif self.player.rect.colliderect(pad) and index == 3:
                    self.player.move((0, -1))
            
            self.handle_key_events()
            pygame.display.update()

    def render(self):
        self.room.draw()
        self.player.draw()

    def handle_key_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(( 0, -1))
        if keys[pygame.K_a]:
            self.player.move((-1,  0))
        if keys[pygame.K_s]:
            self.player.move(( 0,  1))
        if keys[pygame.K_d]:
            self.player.move(( 1,  0))

    def quit(self):
        pygame.quit()


if __name__ == '__main__':
    game = TowerOfBullets((800, 600))
    game.start()