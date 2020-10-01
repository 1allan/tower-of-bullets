from entity import Entity


class Character(Entity):
    
    def __init__(self, surface, position, size, speed, hp):
        super().__init__(surface, position, size, speed)
        self.hp = hp
    
    def shoot(self):
        pass

    def interact(self):
        pass
    
    def get_hit(self):
        pass
