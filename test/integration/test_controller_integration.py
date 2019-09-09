from src.models.controller.controller import begin_search


def test_word_finder__rename():
    words_to_find = ["Big"]
    puzzle_grid = [
        ["B", "I", "G", "D"],
        ["A", "I", "I", "G"],
        ["G", "T", "X", "P"],
    ]

    actual = begin_search(words_to_find, puzzle_grid)

    assert actual == [(0, 0), (0, 1), (0, 2)]
