from src.models.file_reader.file_reader import file_reader


def test_file_reader__words_to_find_list_should_contain_BIGHOUSE_GOBLUE_HAIL_MICHIGAN_WOLVERINES():
    words_to_find, puzzle_grid = file_reader()

    assert len(words_to_find) == 5
    assert words_to_find == ['BIGHOUSE', 'GOBLUE', 'HAIL', 'MICHIGAN', 'WOLVERINES']


