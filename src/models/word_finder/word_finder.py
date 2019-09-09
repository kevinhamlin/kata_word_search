from src.models.utilities.moves_to_search_surrounding_characters import moves
from src.models.utilities.apply_move_to_coordinates import apply_move_to_coordinates
from src.models.utilities.range_check import range_check


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
        if range_check(temp_x, temp_y):
            possible_moves.append((temp_x, temp_y))
    return possible_moves


def search_surrounding_spaces_for_second_letter(letter, possible_coords, grid):
    matches = []
    for coords in possible_coords:
        x, y = coords
        if grid[x][y].lower() == letter.lower():
            matches.append(coords)
    return matches


def find_rest_of_word(matched_coord, move_used, word, grid):
    remaining_coords = []
    letter_index = 2
    match = True
    temp_x, temp_y = matched_coord
    while letter_index < len(word) and match:
        temp_x, temp_y = apply_move_to_coordinates(temp_x, temp_y, move_used)
        if range_check(temp_x, temp_y):
            if grid[temp_x][temp_y].lower() == word[letter_index].lower():
                remaining_coords.append((temp_x, temp_y))
                letter_index += 1
            else:
                match = False
        else:
            match = False
    if match:
        return remaining_coords
    else:
        return None


