from mock import patch

from src.models.controller.controller import begin_search, find_second_letter_matches, get_matched_second_letter_coords, \
    get_move_used


@patch('src.models.controller.controller.search_grid_for_all_instances_of_first_letter')
def test_begin_search__should_call_search_grid_for_instance_of_first_letter_once(mock_validate):
    words_to_find = ["Big"]
    puzzle_grid = [
        ["B", "I", "G", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]

    begin_search(words_to_find, puzzle_grid)

    assert mock_validate.call_count == 1
    mock_validate.assert_called_with(puzzle_grid, "B")


@patch('src.models.controller.controller.find_second_letter_matches')
def test_begin_search__should_call_search_grid_for_instance_of_first_letter_once(mock_matches):
    words_to_find = ["Big"]
    puzzle_grid = [
        ["B", "I", "G", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]

    begin_search(words_to_find, puzzle_grid)

    assert mock_matches.call_count == 1


@patch('src.models.controller.controller.find_possible_second_letter_coords')
def test_find_second_letter_matches__should_call_find_possible_second_letter_coords_once(mock_validate):
    first_letter_coords = [(0, 0)]
    word = "Big"
    puzzle_grid = [
        ["B", "I", "G", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]

    find_second_letter_matches(first_letter_coords, word, puzzle_grid)

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

    get_matched_second_letter_coords(letter, possible_moves, puzzle_grid)

    assert mock_validate.call_count == 1
    mock_validate.assert_called_with(letter, possible_moves, puzzle_grid)


@patch('src.models.controller.controller.find_move_used')
def test_get_move_used__should_call_find_move_used_twice(mock_validate):
    matches = [(0, 1), (1, 1)]
    coord_to_check = (0, 0)

    get_move_used(matches, coord_to_check)

    assert mock_validate.call_count == 2


