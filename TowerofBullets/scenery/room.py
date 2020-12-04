import pygame

from random import randint, choice

from character.enemy import Enemy
from character.player import Player
from scenery.scenario import Scenario
from items.item import Item

IMAGE = 'scenery/01.png'


class Room(Scenario):

    def __init__(self, surface: pygame.Surface, 
                 sprite_group: pygame.sprite.Group, position: tuple,
                 size: tuple, traps: int, chest: bool,
                 image_path: str=IMAGE):
        
        super().__init__(surface, position, size, traps, chest, image_path)
        self.enemies = pygame.sprite.Group()
        self.traps = traps
        self.chest = chest
        self.sprite_group = sprite_group
        self.coins = pygame.sprite.Group()
        self.player = Player(self.surface, self.sprite_group, (size[0]/2, size[1]/2),
                             (70, 70), 3, 20, 200, self.wall_sprites, gold=200)

    def detect_collision(self):
        # detect collision with each enemy
        for enemy in self.enemies:
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
            
            # bullet with walls
            collisionWallsEnemy = pygame.sprite.groupcollide(enemy.weapon.bullets, self.wall_sprites, True, False)

        # detect collision coins
        collisionGold = pygame.sprite.spritecollideany(
            self.player, self.coins)
        if collisionGold:
            self.player.gold += 1
            collisionGold.kill()

        # detect collision bullet player walls
        collisionWallsPlayer = pygame.sprite.groupcollide(self.player.weapon.bullets, self.wall_sprites, True, False)

    def lock_doors(self):
        pass

    def spawn_enemies(self, quantity: int):
        for _ in range(quantity):
            chosen = choice(list(self.floor_sprites))
            position = (chosen.rect.left, chosen.rect.top)

            self.enemies.add(Enemy(self.surface, self.sprite_group, position, 
                                  (70, 70), 2, 100, self.wall_sprites))
            self.sprite_group.add(self.enemies)
    
    def spawn_coins(self, quantity: int):
        image_file = "items/coin.png"

        for _ in range(quantity):
            chosen = choice(list(self.floor_sprites))
            position = (chosen.rect.left, chosen.rect.top)

            self.coins.add(Item(self.surface, position, (20, 20), image_file, 
                                0)) 
            self.sprite_group.add(self.coins)

    def check_enemies(self):
        pass

    def open_doors(self):
        pass

    def update(self):
        self.player.draw()

        cont = 0
        if len(self.enemies) == 0:
            self.spawn_enemies(1)
            self.spawn_coins(1)     # spawn moeda a cada morte

        for enemy in self.enemies:
            enemy.shoot((self.player.x, self.player.y))
            enemy.chase((self.player.x, self.player.y))
            enemy.draw()
        #if len(self.coins) == 0:
        #    self.spawn_coins(1)