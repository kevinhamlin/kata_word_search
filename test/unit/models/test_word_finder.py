from src.models.word_finder.word_finder import find_possible_second_letter_coords, \
    search_surrounding_spaces_for_second_letter, \
    search_remaining_letters_in_a_line, search_grid_for_all_instances_of_first_letter, compare_remaining_letters


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


def test_search_remaining_letters_in_a_line__should_return_none_if_word_is_not_found():
    grid = [
        ["B", "I", "R", "R"],
        ["A", "I", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    matched_coord = (0, 1)
    move_used = (0, 1)
    word = "BIG"

    actual = search_remaining_letters_in_a_line(matched_coord, move_used, word, grid)

    assert actual is None


def test_search_remaining_letters_in_a_line__should_return_none_if_third_letter_matches_but_fourth_does_not():
    grid = [
        ["B", "I", "R", "X"],
        ["A", "I", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    matched_coord = (0, 1)
    move_used = (0, 1)
    word = "BIRD"

    actual = search_remaining_letters_in_a_line(matched_coord, move_used, word, grid)

    assert actual is None


def test_search_remaining_letters_in_a_line__should_return_none_if_search_goes_off_grid():
    grid = [
        ["R", "I", "B", "D"],
        ["I", "A", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    matched_coord = (0, 1)
    move_used = (0, -1)
    word = "BIRD"

    actual = search_remaining_letters_in_a_line(matched_coord, move_used, word, grid)

    assert actual is None


def test_search_remaining_letters_in_a_line__should_return_coord_of_last_letter_when_found():
    grid = [
        ["B", "I", "B", "D"],
        ["I", "A", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    matched_coord = (1, 0)
    move_used = (1, 0)
    word = "BIG"

    actual = search_remaining_letters_in_a_line(matched_coord, move_used, word, grid)

    assert actual == [(2, 0)]


def test_search_remaining_letters_in_a_line__should_stop_searching_when_entire_word_is_found():
    grid = [
        ["B", "I", "G", "D"],
        ["I", "A", "I", "G"],
        ["D", "T", "X", "P"],
    ]
    matched_coord = (0, 1)
    move_used = (0, 1)
    word = "BIG"

    actual = search_remaining_letters_in_a_line(matched_coord, move_used, word, grid)

    assert actual == [(0, 2)]


def test_search_remaining_letters_in_a_line__should_stop_return_coords_of_letters_for_words_longer_than_three_characters():
    grid = [
        ["B", "I", "G", "D"],
        ["I", "A", "I", "G"],
        ["D", "T", "V", "P"],
        ["D", "T", "E", "P"],
        ["D", "T", "T", "P"],
        ["D", "T", "X", "P"],
    ]
    matched_coord = (1, 2)
    move_used = (1, 0)
    word = "GIVE"

    actual = search_remaining_letters_in_a_line(matched_coord, move_used, word, grid)

    assert actual == [
        (2, 2),
        (3, 2)
    ]


def test_search_remaining_letters_in_a_line__should_stop_return_coords_of_letters_for_words_longer_than_four_characters():
    grid = [
        ["B", "I", "G", "D"],
        ["I", "A", "I", "G"],
        ["D", "T", "V", "P"],
        ["D", "T", "E", "P"],
        ["D", "T", "S", "P"],
        ["D", "T", "X", "P"],
    ]
    matched_coord = (1, 2)
    move_used = (1, 0)
    word = "GIVES"

    actual = search_remaining_letters_in_a_line(matched_coord, move_used, word, grid)

    assert actual == [
        (2, 2),
        (3, 2),
        (4, 2)
    ]


def test_search_remaining_letters_in_a_line__should_stop_return_coords_of_letters_for_words_with_case_mismatch():
    grid = [
        ["B", "I", "G", "D"],
        ["I", "A", "I", "G"],
        ["D", "T", "V", "P"],
        ["D", "T", "E", "P"],
        ["D", "T", "S", "P"],
        ["D", "T", "X", "P"],
    ]
    matched_coord = (1, 2)
    move_used = (1, 0)
    word = "gives"

    actual = search_remaining_letters_in_a_line(matched_coord, move_used, word, grid)

    assert actual == [
        (2, 2),
        (3, 2),
        (4, 2)
    ]


def test_search_surrounding_spaces_for_second_letter__should_return_list_with_coords_when_despite_case_mismatch():
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
    letter = "i"

    actual = search_surrounding_spaces_for_second_letter(letter, possible_coords, grid)

    assert actual == [
        (0, 1),
        (1, 1)
    ]

def test_search_grid_for_all_instances_of_first_letter__should_return_None_if_no_matches_found():
    grid = [
        ["B", "I", "R", "R"],
        ["A", "I", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    letter = "K"

    actual = search_grid_for_all_instances_of_first_letter(grid, letter)

    assert actual is None


def test_search_grid_for_all_instances_of_first_letter__should_return_a_single_set_of_coords_when_one_match_found():
    grid = [
        ["B", "I", "R", "R"],
        ["A", "I", "I", "G"],
        ["Y", "T", "X", "P"],
    ]
    letter = "G"

    actual = search_grid_for_all_instances_of_first_letter(grid, letter)

    assert actual == [(1, 3)]


def test_search_grid_for_all_instances_of_first_letter__should_handle_case_mismatch_and_return_coords():
    grid = [
        ["B", "I", "R", "R"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    letter = "x"

    actual = search_grid_for_all_instances_of_first_letter(grid, letter)
    assert actual == [(2, 2)]


def test_search_grid_for_all_instances_of_first_letter__should_return_multiple_coords_when_multiple_matches_found():
    grid = [
        ["B", "I", "R", "R"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    letter = "I"

    actual = search_grid_for_all_instances_of_first_letter(grid, letter)
    assert actual == [(0, 1), (1, 1), (1, 2)]


def test_compare_remaining_letters__match_should_return_false_when_letters_do_not_match():
    grid = [
        ["B", "I", "P", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    letter_index = 2
    match = True
    remaining_coords = []
    temp_x = 0
    temp_y = 2
    word = "BIRD"

    letter_index, match, remaining_coords = compare_remaining_letters(grid, letter_index, match, remaining_coords, temp_x, temp_y, word)


    assert match is False
    assert letter_index == 2
    assert remaining_coords == []


def test_compare_remaining_letters__match_should_return_true_when_letters_match():
    grid = [
        ["B", "I", "R", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    letter_index = 2
    match = True
    remaining_coords = []
    temp_x = 0
    temp_y = 2
    word = "BIRD"

    letter_index, match, remaining_coords = compare_remaining_letters(grid, letter_index, match, remaining_coords, temp_x, temp_y, word)


    assert match is True
    assert letter_index == 3
    assert remaining_coords == [(0, 2)]


def test_compare_remaining_letters__should_handle_case_mismatch_and_return_true_with_increased_letter_index():
    grid = [
        ["B", "I", "R", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    letter_index = 2
    match = True
    remaining_coords = []
    temp_x = 0
    temp_y = 2
    word = "BIrD"

    letter_index, match, remaining_coords = compare_remaining_letters(grid, letter_index, match, remaining_coords, temp_x, temp_y, word)

    assert match is True
    assert letter_index == 3
    assert remaining_coords == [(0, 2)]

