
def apply_move_to_coordinates(temp_x, temp_y, move):
    x, y = move
    temp_x = temp_x + x
    temp_y = temp_y + y
    return(temp_x, temp_y)