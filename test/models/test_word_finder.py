from src.models.word_finder.word_finder import search_row_for_y_coord, find_first_letter_coords


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