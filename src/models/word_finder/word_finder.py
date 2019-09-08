


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