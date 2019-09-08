from src.models.utilities.apply_move_to_coordinates import apply_move_to_coordinates
from src.models.utilities.range_check import range_check


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

def test_range_check__should_return_False_for_x_coord_below_zero():
    temp_x = -1
    temp_y = 1

    actual = range_check(temp_x, temp_y)

    assert not actual

def test_range_check__should_return_False_for_x_coord_above_fourteen():
    temp_x = 15
    temp_y = 6

    actual = range_check(temp_x, temp_y)

    assert not actual