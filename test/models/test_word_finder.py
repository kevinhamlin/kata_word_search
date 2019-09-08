from src.models.word_finder.word_finder import search_row_for_y_coord


def test_search_row_for_y_coord__should_return_none_if_character_not_found():
    row = ['S', 'A', 'B', 'C']
    character = 'N'

    actual = search_row_for_y_coord(row, character)

    assert actual is None

