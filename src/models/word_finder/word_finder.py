


def search_row_for_y_coord(row, character):
    for y, unknown_character in enumerate(row):
        if unknown_character == character:
            return y
    return None