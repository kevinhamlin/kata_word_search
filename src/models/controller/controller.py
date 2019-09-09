from src.models.word_finder.word_finder import search_grid_for_all_instances_of_first_letter, \
    find_possible_second_letter_coords


def begin_search(words_to_find, puzzle_grid):
    for word in words_to_find:
        letter = word[0]
        first_letter_coords = search_grid_for_all_instances_of_first_letter(puzzle_grid, letter)
        find_second_letter_matches(first_letter_coords, word, puzzle_grid)


def find_second_letter_matches(first_letter_coords, word, puzzle_grid):
    for coord_to_check in first_letter_coords:
        possible_moves = find_possible_second_letter_coords(coord_to_check)