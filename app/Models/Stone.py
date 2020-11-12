import pygame

class Stone:
    def __init__(self, colour, row, col):
        self.position = (row, col)
        self.colour = colour
        self.king = False
        self.captured = False
        self.circle = None

    def get_position(self):
        return self.position
    
    def update_position(self, row, col):
        self.position = (row, col)
    
    def captured(self):
        self.captured = True

    def is_captured(self):
        return self.captured
    
    def make_king(self):
        self.king = True
    
    def is_king(self):
        return self.king

    def get_colour_string(self):
        return self.colour
    
    def get_colour(self):
        if self.colour == "Black":
            return pygame.Color(0, 0, 0)
        else:
            return pygame.Color(255, 0, 0)
    
    def get_direction(self):
        if self.colour == "Black":
            return "Down"
        else:
            return "Up"

    