import pygame
from pygame.locals import *
from app.Models.Neighbour import Neighbour

class Tile:

    def __init__(self, row, col, size):
        self.coords = (row, col)
        self.stone = None
        self.neighbours = self.init_neighbours()
        self.rect = None
        self.size = size
        self.colour = None
        self.outlined = False

    def set_stone(self, stone):
        self.stone = stone
    
    def get_size(self):
        return self.size

    def get_stone(self):
        return self.stone
    
    def get_coords(self):
        return self.coords

    def get_colour(self):
        return self.colour
    
    def set_colour(self, colour):
        self.colour = colour
    
    def has_stone(self):
        return self.stone != None

    def init_neighbours(self):
        coords = self.get_coords()
        neighbours = list()
        above = False
        below = False
        if coords[0] >= (1):
            above = True
        if coords[0] <= (6):
            below = True
        if coords[1] >= (1):
            if above:
                neighbours.append(Neighbour((coords[0] - 1, coords[1] - 1), self))
            if below:
                neighbours.append(Neighbour((coords[0] + 1, coords[1] - 1), self))
        if coords[1] <= (6):
            if above:
                neighbours.append(Neighbour((coords[0] - 1, coords[1] + 1), self))
            if below:
                neighbours.append(Neighbour((coords[0] + 1, coords[1] + 1), self))
        return neighbours
    
    def check_bounds(self, position):
        if position <= 7 and position >= 0:
            return True
        else:
            return False
    
    def add_neighbour(self, row, col):
        self.neighbours.append((row, col))

    def get_neighbours(self):
        return self.neighbours

    def get_capture_neighbours(self):
        return self.capture_neighbours
    
    def get_rect(self):
        return self.rect
    
    def set_rect(self, rect):
        self.rect = rect

    def is_outlined(self):
        return self.outlined
    
    def set_outlined(self, state):
        self.outlined = state
    
    def check_move(self, new_tile):
        new_coords = new_tile.get_coords()
        if self.check_not_owned(new_tile):
            if self.check_direction(new_coords):
                return True
        elif self.get_stone().get_colour_string() == new_tile.get_stone().get_colour_string():
            self.set_outlined(False)
            new_tile.set_outlined(True)
            return new_tile
        return False
    
    def check_direction(self, new_coords):
        is_king = self.get_stone().is_king()
        coords = self.get_coords()
        direction = self.get_stone().get_direction()
        if is_king:
            return True # All neighbours are valid and so direction is valid
        else:
            if direction == "Up":
                if new_coords[0] < coords[0]:
                    if new_coords[0] == 0:
                        self.get_stone().make_king()
                    return True
            elif direction == "Down":
                if new_coords[0] > coords[0]:
                    if new_coords[0] == 7:
                        self.get_stone().make_king()
                    return True
        return False
    
    def check_not_owned(self, new_tile):
        if new_tile.get_stone() == None:
            return True
        return False
    
    def draw_tile(self, window):
        pygame.draw.rect(window.get_surface(), self.get_colour(), self.get_rect())
    
    def draw_stone(self, window):
        circle_colour = self.get_stone().get_colour()
        radius = int(self.get_size() // 2)
        centre = (int(self.get_rect().left + radius), int(self.get_rect().top + radius))
        radius -= 5
        if self.is_outlined():
            outline_colour = pygame.Color(255, 255, 0)
            pygame.draw.circle(window.get_surface(), outline_colour, centre, (radius + 2))
        pygame.draw.circle(window.get_surface(), circle_colour, centre, radius)
        if self.get_stone().is_king():
            king_font = pygame.font.Font(None, radius)
            king = king_font.render("K", True, (255, 255, 255))
            king_size = king_font.size("K")
            king_coords = ((centre[0] - (king_size[0]//2)), (centre[1] - (king_size[1]//2)))
            window.get_window().blit(king, king_coords)
        




