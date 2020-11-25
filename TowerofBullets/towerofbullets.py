import pygame

from util.functions import load_image

from character.player import Player
from scenery.room import Room


class TowerOfBullets:
    
    def __init__(self, screen_size, fps=60):
        self.width, self.height = screen_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = fps
        self.room = None
        self.player = None
        self.paused = False
        self.sprites = pygame.sprite.Group()
    
    def run(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Tower of Bullets")
        
        # setar elementos principais
        self.player = Player(self.screen, (self.width/2, self.height/2),
                             (70, 70), 3, 200, 200, self.sprites, gold=200)
        self.room = Room(self.screen, (0, 0), (self.width, self.height), 0, False,  self.player, self.sprites)
        self.sprites.add(self.room)
        self.sprites.add(self.player)
       
        # while do jogo principal
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            
            # personagem colisão parede
            self.collide_walls()

            # colisão bullet player / enemy
            self.detect_collision()

            # ver se não está pausado, para renderizar o principal do jogo
            if not self.paused:
                self.render()

            # handle key events
            self.handle_input()
    
    def detect_collision(self):
        # dettect collision with each enemy
        for enemy in self.room.enemies:
            # bullet enemy with player
            if pygame.sprite.spritecollideany(self.player, enemy.weapon.bullets):
                print('bala enemy bateu no player')

            # bullet player with enemies
            if pygame.sprite.spritecollideany(enemy, self.player.weapon.bullets):
                print(f'hittou o enemy {enemy}')

    # colisão com paredes
    def collide_walls(self):
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

    def render(self):
        self.sprites.draw(self.screen)
        self.sprites.update()
        pygame.display.update()

    def handle_input(self):
        keyboard = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        direction = [0, 0]
        if keyboard[pygame.K_a]:
            direction[0] = -1
        elif keyboard [pygame.K_d]:
            direction[0] = 1

        if keyboard[pygame.K_w]:
            direction[1] = -1
        elif keyboard[pygame.K_s]:
            direction[1] = 1
        
        self.player.move(direction)

        if mouse[0]:
            self.player.shoot()

    def quit(self):
        pygame.quit()


if __name__ == '__main__':
    game = TowerOfBullets((800, 600))
    game.run()