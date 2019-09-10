from src.models.utilities.moves_to_search_surrounding_characters import moves
from src.models.utilities.apply_move_to_coordinates import apply_move_to_coordinates
from src.models.utilities.range_check import range_check


def search_grid_for_all_instances_of_first_letter(grid, letter):
    first_letter_coords = []
    for x, row in enumerate(grid):
        for y, grid_character in enumerate(row):
            if grid_character.lower() == letter.lower():
                first_letter_coords.append((x, y))
    if len(first_letter_coords) > 0:
        return first_letter_coords
    return None


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


def search_remaining_letters_in_a_line(matched_coord, move_used, word, grid):
    remaining_coords = []
    letter_index = 2
    match = True
    temp_x, temp_y = matched_coord
    while letter_index < len(word) and match:
        temp_x, temp_y = apply_move_to_coordinates(temp_x, temp_y, move_used)
        letter_index, match, remaining_coords = compare_remaining_letters(grid, letter_index, match, remaining_coords, temp_x, temp_y, word)
    if match:
        return remaining_coords
    else:
        return None


def compare_remaining_letters(grid, letter_index, match, remaining_coords, temp_x, temp_y, word):
    if range_check(temp_x, temp_y):
        if grid[temp_x][temp_y].lower() == word[letter_index].lower():
            remaining_coords.append((temp_x, temp_y))
            letter_index += 1
        else:
            match = False
    else:
        match = False
    return letter_index, match, remaining_coords


