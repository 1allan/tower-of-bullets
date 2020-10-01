import pygame

from character import Character
from weapon import Weapon


class Player(Character):

    def __init__(self, surface, position, size, speed, hp, energy, gold=0, weapon:Weapon=None):
        super().__init__(surface, position, size, speed, hp)
        self.hp = hp
        self.energy = energy
        self.gold = gold
        self.weapon = Weapon() if weapon is None else weapon
    
