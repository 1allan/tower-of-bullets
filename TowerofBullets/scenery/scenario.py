from abc import ABC, abstractmethod


class Scenario(ABC):

    def __init__(self, position: tuple, size: tuple, structure: str):
        self.x, self.y = position
        self.width, self.height = size
        self.structure = structure

    