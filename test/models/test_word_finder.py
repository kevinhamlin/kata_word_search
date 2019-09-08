from src.models.word_finder.word_finder import search_row_for_y_coord, find_first_letter_coords, \
    find_possible_second_letter_coords, search_surrounding_spaces_for_second_letter, find_rest_of_word


def test_search_row_for_y_coord__should_return_none_if_character_not_found():
    row = ['S', 'A', 'B', 'C']
    character = 'N'

    actual = search_row_for_y_coord(row, character)

    assert actual is None


def test_search_row_for_y_coord__should_return_1_when_character_found():
    row = ['S', 'A', 'B', 'C']
    character = 'A'

    actual = search_row_for_y_coord(row, character)

    assert actual == 1


def test_search_row_for_y_coord__should_return_2_when_character_found_with_case_mismatch():
    row = ['S', 'A', 'B', 'C']
    character = 'b'

    actual = search_row_for_y_coord(row, character)

    assert actual == 2


def test_find_first_letter_coords__should_return_none_when_not_found():
    grid = [
        ["S", "A", "I", "G"],
    ]

    character_to_find = "B"

    actual = find_first_letter_coords(character_to_find, grid)

    assert actual is None


def test_find_first_letter_coords__should_return_coords_when_found():
    rows = [
        ["S", "B", "I", "G"],
    ]

    character_to_find = "B"

    actual = find_first_letter_coords(character_to_find, rows)

    assert actual == (0,1)


def test_find_first_letter_coords__should_search_multiple_rows_and_return_coords_when_found():
    rows = [
        ["S", "B", "I", "G"],
        ["A", "B", "C", "D"]
    ]

    character_to_find = "C"

    actual = find_first_letter_coords(character_to_find, rows)

    assert actual == (1,2)


def test_find_possible_second_letter_coords__should_return_coord_when_match_found():

    coord = (1,2)

    actual = find_possible_second_letter_coords(coord)

    assert actual == [
        (0,1),
        (0,2),
        (0,3),
        (1,3),
        (2,3),
        (2,2),
        (2,1),
        (1,1)
    ]

def test_find_possible_second_letter_coords__should_not_return_coords_outside_of_puzzle_grid():

    coord = (0, 0)

    actual = find_possible_second_letter_coords(coord)

    assert actual == [
        (0,1),
        (1,1),
        (1,0)
    ]

def test_search_surrounding_spaces_for_second_letter__should_return_empty_list_if_no_matches_found():
    grid = [
        ["S", "U", "R", "R"],
        ["A", "B", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    possible_coords = [
        (0, 1),
        (1, 1),
        (1, 0)
    ]
    letter = "I"

    actual = search_surrounding_spaces_for_second_letter(letter, possible_coords, grid)

    assert actual == []


def test_search_surrounding_spaces_for_second_letter__should_return_list_with_one_set_of_coords_if_a_single_match_found():
    grid = [
        ["B", "U", "R", "R"],
        ["A", "I", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    possible_coords = [
        (0, 1),
        (1, 1),
        (1, 0)
    ]
    letter = "I"

    actual = search_surrounding_spaces_for_second_letter(letter, possible_coords, grid)

    assert actual == [(1, 1)]


def test_search_surrounding_spaces_for_second_letter__should_return_list_with_multiple_coords_when_multiple_matches_found():
    grid = [
        ["B", "I", "R", "R"],
        ["A", "I", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    possible_coords = [
        (0, 1),
        (1, 1),
        (1, 0)
    ]
    letter = "I"

    actual = search_surrounding_spaces_for_second_letter(letter, possible_coords, grid)

    assert actual == [
        (0, 1),
        (1, 1)
    ]


def test_find_rest_of_word__should_return_none_if_word_is_not_found():
    grid = [
        ["B", "I", "R", "R"],
        ["A", "I", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    matched_coord = (0, 1)
    move_used = (0, 1)
    word = "BIG"

    actual = find_rest_of_word(matched_coord, move_used, word, grid)

    assert actual is None


def test_find_rest_of_word__should_return_none_if_third_letter_matches_but_fourth_does_not():
    grid = [
        ["B", "I", "R", "D"],
        ["A", "I", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    matched_coord = (0, 1)
    move_used = (0, 1)
    word = "BIRD"

    actual = find_rest_of_word(matched_coord, move_used, word, grid)

    assert actual is None