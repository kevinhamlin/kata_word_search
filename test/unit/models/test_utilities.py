from src.models.utilities.apply_move_to_coordinates import apply_move_to_coordinates
from src.models.utilities.build_final_list_of_coords import build_final_list_of_coords
from src.models.utilities.find_move_used import find_move_used
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

def test_range_check__should_return_False_for_y_coord_below_zero():
    temp_x = 5
    temp_y = -1

    actual = range_check(temp_x, temp_y)

    assert not actual


def test_range_check__should_return_False_for_y_coord_above_fourteen():
    temp_x = 15
    temp_y = -1

    actual = range_check(temp_x, temp_y)

    assert not actual


def test_range_check__should_return_True_for_valid_set_of_coordinates():
    temp_x = 8
    temp_y = 13

    actual = range_check(temp_x, temp_y)

    assert actual

def test_find_move_used__should_return_1_0_when_given_coords():
    first_letter_coords = (8, 13)
    second_letter_coords = (9, 13)

    actual = find_move_used(first_letter_coords, second_letter_coords)

    assert actual == (1, 0)


def test_find_move_used__should_return_minus_one_minus_one_when_given_coords():
    first_letter_coords = (8, 13)
    second_letter_coords = (7, 12)

    actual = find_move_used(first_letter_coords, second_letter_coords)

    assert actual == (-1, -1)


def test_build_final_list_of_coords__should_return_list_containing_all_coords_for_found_word():
    coord_to_check = (0, 2)
    match = (1, 2)
    result = [(2, 2), (3, 2), (4, 2)]

    actual = build_final_list_of_coords(coord_to_check, match, result)

    assert actual == [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]