import pygame

from start import StartView
from config import ConfigView
from towerofbullets import TowerOfBullets

if __name__ == "__main__":
    start = StartView((800, 600))
    start.run()
