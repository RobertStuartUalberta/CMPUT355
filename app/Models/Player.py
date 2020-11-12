class Player:
    def __init__(self, colour):
        self. colour = colour
        self.stones = list()
        self.captured = list()

    def get_colour(self):
        return self.colour
    
    def get_stones(self):
        return self.stones
    
    def get_captured(self):
        return self.captured

    def add_stone(self, stone):
        self.stones.append(stone)
    
    def capture_stone(self, stone):
        self.stones.remove(stone)
        self.captured.append(stone)
    
    def stone_owned(self, stone):
        if stone in self.get_stones():
            return True
        else:
            return False
