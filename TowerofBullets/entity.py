import pygame

class Entity:

    def __init__(self, surface: pygame.Surface, position: tuple, size: tuple, speed=0, image_file='./assets/placeholder.png'):
        self.surface = surface
        self.size = size
        self.width, self.height = self.size
        self.image = self.__load_image(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.x = round(self.rect.left + self.width/2)
        self.y = round(self.rect.top + self.height/2)
        self.rect.center = (self.x, self.y)
        self.speed = speed
    
    # I think this method should be an utility function in utils/functions.py, 
    # because it will probably be used in many other classes.
    def __load_image(self, path, convert=False):
        image = pygame.image.load(path)
        if convert:
            image = image.convert()
        
        return pygame.transform.scale(image, self.size)

    # @param direction: a tuple of two integers with values -1, 0 or 1, 
    # that sets the movement way.
    def move(self, direction=None):
        self.x += self.speed * direction[0]
        self.y += self.speed * direction[1]

    def update(self):
        self.surface.blit(self.image, (self.x, self.y))