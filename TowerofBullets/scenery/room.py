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
        self.hearts = pygame.sprite.Group()
        self.cont = 0
        self.player = Player(self.surface, self.sprite_group, (size[0]/2, size[1]/2),
                             (70, 70), 3, 20, 200, self.wall_sprites, gold=0)

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
        
        # detect collision hearts
        collisionHeart = pygame.sprite.spritecollideany(
            self.player, self.hearts)
        if collisionHeart:
            self.player.hp += 10
            if self.player.hp > 20:
                self.player.hp = 20
            collisionHeart.kill()

        # detect collision bullet player walls
        collisionWallsPlayer = pygame.sprite.groupcollide(self.player.weapon.bullets, self.wall_sprites, True, False)

    def spawn_enemies(self, quantity: int):
        for _ in range(quantity):
            chosen = choice(list(self.floor_sprites))
            position = (chosen.rect.left, chosen.rect.top)

            self.enemies.add(Enemy(self.surface, self.sprite_group, position, 
                                  (70, 70), 1, 100, self.wall_sprites))
            self.sprite_group.add(self.enemies)
    
    def spawn_coins(self, quantity: int):
        image_file = "items/coin.png"

        for _ in range(quantity):
            chosen = choice(list(self.floor_sprites))
            position = (chosen.rect.left, chosen.rect.top)

            self.coins.add(Item(self.surface, position, (20, 20), image_file, 
                                0)) 
            self.sprite_group.add(self.coins)
    
    def spawn_hearts(self, quantity: int):
        image_file = "items/ui_heart_full.png"

        for _ in range(quantity):
            chosen = choice(list(self.floor_sprites))
            position = (chosen.rect.left, chosen.rect.top)

            self.hearts.add(Item(self.surface, position, (20, 20), image_file, 
                                0)) 
            self.sprite_group.add(self.hearts)

    def update(self):
        self.player.draw()

        if len(self.enemies) == 0:
            print(self.cont)
            self.cont+=1
            self.spawn_enemies(1)
            if self.cont%2==0:
                self.spawn_coins(2)
            elif self.cont%3==0:
                self.spawn_hearts(1)
        for enemy in self.enemies:
            enemy.shoot((self.player.x, self.player.y))
            enemy.chase((self.player.x, self.player.y))
            enemy.draw()
