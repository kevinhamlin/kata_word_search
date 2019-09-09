from src.models.word_finder.word_finder import search_grid_for_all_instances_of_first_letter


def begin_search(words_to_find, puzzle_grid):
    for word in words_to_find:
        letter = word[0]
        first_letter_coords = search_grid_for_all_instances_of_first_letter(puzzle_grid, letter)



