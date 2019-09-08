from src.models.file_reader.file_reader import file_reader


def test_file_reader__words_to_find_list_should_contain_BIGHOUSE_GOBLUE_HAIL_MICHIGAN_WOLVERINES():
    words_to_find, puzzle_grid = file_reader()

    assert len(words_to_find) == 5
    assert words_to_find == ['BIGHOUSE', 'GOBLUE', 'HAIL', 'MICHIGAN', 'WOLVERINES']


def test_file_reader__first_row_of_puzzle_grid_should_contain_the_correct_characters():
    words_to_find, puzzle_grid = file_reader()

    assert len(puzzle_grid[0]) == 15
    assert puzzle_grid[0] == ['S', 'G', 'C', 'W', 'J', 'J', 'C', 'D', 'B', 'C', 'R', 'J', 'P', 'T', 'W']


