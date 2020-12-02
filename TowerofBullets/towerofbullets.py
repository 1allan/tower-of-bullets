import pygame
import pickle
from time import time

from util.functions import load_image

from character.player import Player
from scenery.room import Room
from screens.pause import Pause


class TowerOfBullets:

    def __init__(self, display, fps=60):
        self.surface = display
        self.width, self.height = self.surface.get_size()
        self.fps = fps
        self.room = None
        self.player = None
        self.pause_group = None
        self.paused = False
        self.sprites = pygame.sprite.Group()
        self.current_screen = None
        self.last_pause = 0

    def run(self):
        # setar elementos principais
        self.player = Player(self.surface, self.sprites, (self.width/2, self.height/2),
                             (70, 70), 3, 20, 200, gold=200)
        self.room = Room(self.surface, self.sprites, (0, 0), (self.width,
                                               self.height), 0, False,  self.player)

        self.sprites.add(self.room)
        self.sprites.add(self.player)

    def detect_collision(self):
        self.collide_walls()
        # detect collision with each enemy
        for enemy in self.room.enemies:
            # bullet enemy with player
            collisionPlayer = pygame.sprite.spritecollideany(
                self.player, enemy.weapon.bullets)
            if collisionPlayer:
                self.player.be_hit(enemy.weapon.damage)
                collisionPlayer.kill()

            # bullet player with enemies
            collisionEnemy = pygame.sprite.spritecollideany(
                enemy, self.player.weapon.bullets)
            if collisionEnemy:
                enemy.be_hit(self.player.weapon.damage)
                if enemy.hp <= 0:
                    self.player.score += 10
                collisionEnemy.kill()

        # detect collision coins
        collisionGold = pygame.sprite.spritecollideany(
            self.player, self.room.coins)
        if collisionGold:
            self.player.gold += 1
            collisionGold.kill()

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

        self.player.move(direction)

        if mouse[0]:
            self.player.shoot()

    def render(self):
        self.sprites.draw(self.surface)
        self.sprites.update()

