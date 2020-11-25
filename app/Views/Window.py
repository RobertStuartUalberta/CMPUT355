import pygame
from pygame.locals import*

class Window:

    def __init__(self, name, width, height):
        self.dimensions = (width, height)
        self.window = pygame.display.set_mode((self.get_dimensions()))
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption(name)
        pygame.display.flip()
        self.surface = pygame.display.get_surface()

    def get_dimensions(self):
        return self.dimensions

    def get_window(self):
        return self.window

    def get_surface(self):
        return self.surface
    
    def update(self):
        pygame.display.flip()

