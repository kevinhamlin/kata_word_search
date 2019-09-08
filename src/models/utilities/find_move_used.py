
def find_move_used(first_letter_coords, second_letter_coords):
    first_x, first_y = first_letter_coords
    second_x, second_y = second_letter_coords
    return second_x - first_x, second_y - first_y