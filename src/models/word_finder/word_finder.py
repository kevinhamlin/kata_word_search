from src.models.utilities.moves_to_search_surrounding_characters import moves
from src.models.utilities.apply_move_to_coordinates import apply_move_to_coordinates

def search_row_for_y_coord(row, character):
    for y, unknown_character in enumerate(row):
        if unknown_character.lower() == character.lower():
            return y
    return None


def find_first_letter_coords(character, grid):
    for x, row in enumerate(grid):
        result = search_row_for_y_coord(row, character)

        if result is not None:
            return x, result



def find_possible_second_letter_coords(coords):
    x, y = coords
    possible_moves = []
    for move in moves:
        temp_x, temp_y = apply_move_to_coordinates(x, y, move)
        possible_moves.append((temp_x, temp_y))
    return possible_moves