from src.models.utilities.apply_move_to_coordinates import apply_move_to_coordinates


def test_apply_move_to_coordinates__should_advance_coordinates_by_1():
    temp_x = 2
    temp_y = 2
    move = (1, 1)

    new_x, new_y = apply_move_to_coordinates(temp_x, temp_y, move)

    assert new_x == 3
    assert new_y == 3


def test_apply_move_to_coordinates__should_advance_x_coord_by_minus_1_y_should_remain_the_same():
    temp_x = 2
    temp_y = 2
    move = (-1, 0)

    new_x, new_y = apply_move_to_coordinates(temp_x, temp_y, move)

    assert new_x == 1
    assert new_y == 2