from mock import patch

from src.models.controller.controller import begin_search, find_second_letter_matches


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