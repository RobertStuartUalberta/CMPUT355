

class Neighbour:

    def __init__(self, coords, starting_tile):
        self.parent = starting_tile
        self.coords = coords
        self.coords_for_capture = self.init_capture(coords, starting_tile.get_coords())
    
    def get_coords(self):
        return self.coords
    def get_parent(self):
        return self.parent
    def get_coords_for_capture(self):
        return self.coords_for_capture
    
    def init_capture(self, coords, starting_coords):
        row_direction = coords[0] - starting_coords[0]
        col_direction = coords[1] - starting_coords[1]
        if coords[0] + row_direction > 7 or coords[0] + row_direction < 0:
            return None
        elif coords[1] + col_direction > 7 or coords[1] + col_direction < 0:
            return None
        else:
            return (coords[0] + row_direction, coords[1] + col_direction)
    
    def is_captureable(self, board):
        coords = self.get_coords()
        capture_coords = self.get_coords_for_capture()
        parent_tile = self.get_parent()
        if capture_coords != None:
            tile_to_be_captured = board.get_tile(coords[0], coords[1])
            tile_for_capture = board.get_tile(capture_coords[0], capture_coords[1])
            if tile_to_be_captured.get_stone() == None:
                return False
            elif tile_for_capture.get_stone() != None:
                return False
            elif parent_tile.get_stone().get_colour_string() == tile_to_be_captured.get_stone().get_colour_string():
                return False
            else:
                return True
        else:
            return False
