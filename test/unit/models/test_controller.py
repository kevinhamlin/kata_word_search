from mock import patch

from src.models.controller.controller import begin_search, __find_second_letter_matches, __get_matched_second_letter_coords, \
    __get_move_used, __check_if_path_matches_rest_of_word, __create_list_of_found_word_coords


@patch('src.models.controller.controller.search_grid_for_all_instances_of_first_letter')
def test_begin_search__should_call_search_grid_for_instance_of_first_letter_once(mock_validate):
    words_to_find = ["Big"]
    puzzle_grid = [
        ["B", "I", "G", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    final_output_list = []
    begin_search(words_to_find, puzzle_grid, final_output_list)

    assert mock_validate.call_count == 1
    mock_validate.assert_called_with(puzzle_grid, "B")


@patch('src.models.controller.controller.find_possible_second_letter_coords')
def test_find_second_letter_matches__should_call_find_possible_second_letter_coords_once(mock_validate):
    first_letter_coords = [(0, 0)]
    word = "Big"
    puzzle_grid = [
        ["B", "I", "G", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]

    __find_second_letter_matches(first_letter_coords, word, puzzle_grid)

    assert mock_validate.call_count == 1
    mock_validate.assert_called_with((0, 0))


@patch('src.models.controller.controller.search_surrounding_spaces_for_second_letter')
def test_get_matched_second_letter_coords__should_call_search_surrounding_spaces_for_second_letter_once(mock_validate):
    letter = "I"
    possible_moves = [(0, 1), (1, 1)]
    puzzle_grid = [
        ["B", "I", "G", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    coord_to_check = (0, 0)
    word = "BIG'"

    __get_matched_second_letter_coords(letter, possible_moves, puzzle_grid, coord_to_check, word)

    assert mock_validate.call_count == 1
    mock_validate.assert_called_with(letter, possible_moves, puzzle_grid)


@patch('src.models.controller.controller.__check_if_path_matches_rest_of_word')
@patch('src.models.controller.controller.find_move_used')
def test_get_move_used__should_call_find_move_used_once(mock_validate, mock_check):
    matches = [(0, 1), (1, 1)]
    coord_to_check = (0, 0)
    word = "BIG"
    puzzle_grid = [
        ["B", "I", "G", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]

    __get_move_used(matches, coord_to_check, word, puzzle_grid)

    assert mock_validate.call_count == 1


@patch('src.models.controller.controller.search_remaining_letters_in_a_line')
def test_check_if_path_matches_rest_of_word__shoul_call_search_remaining_letters_in_a_line_once(mock_validate):
    puzzle_grid = [
        ["B", "I", "G", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    match = (0, 1)
    move_used = (0, 1)
    word = "BIG"
    coord_to_check = (0, 0)

    __check_if_path_matches_rest_of_word(match, move_used, word, puzzle_grid, coord_to_check)

    assert mock_validate.call_count == 1
    mock_validate.assert_called_with(match, move_used, word, puzzle_grid)

@patch('src.models.controller.controller.build_final_list_of_coords')
def test_create_list_of_found_word_coords__should_call_build_list_of_coords_once(mock_validate):
    coord_to_check = (0, 0)
    match = (0, 1)
    result = [(0, 2)]
    word = "BIG"

    __create_list_of_found_word_coords(result, coord_to_check, match, word)

    assert mock_validate.call_count == 1
    mock_validate.assert_called_with(coord_to_check, match, result)


def test___find_second_letter_matches__should_return_None_when_word_not_found():
    puzzle_grid = [
        ["B", "I", "D", "G"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    first_letter_coords = [(0,0)]
    word = "BIG"


    actual = __find_second_letter_matches(first_letter_coords, word, puzzle_grid)

    assert actual is None


def test__get_matched_second_letter_coords__should_return_None_when_word_not_found():
    puzzle_grid = [
        ["B", "I", "D", "G"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    coord_to_check = (0, 0)
    word = "BIG"
    letter = "I"
    possible_moves = [(0, 1), (1, 1)]

    actual = __get_matched_second_letter_coords(letter, possible_moves, puzzle_grid, coord_to_check, word)

    assert actual is None


def test___get_move_used__should_return_None_when_word_not_found():
    puzzle_grid = [
        ["B", "I", "D", "G"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    coord_to_check = (0, 0)
    word = "BIG"
    matches = [(0, 1), (1, 1)]

    actual = __get_move_used(matches, coord_to_check, word, puzzle_grid)

    assert actual is None


def test___check_if_path_matches_rest_of_word__should_return_None_when_word_not_found():
    puzzle_grid = [
        ["B", "I", "D", "G"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]
    coord_to_check = (0, 0)
    word = "BIG"
    match = (0, 1)
    move_used = (0, 1)

    actual = __check_if_path_matches_rest_of_word(match, move_used, word, puzzle_grid, coord_to_check)

    assert actual is None