from src.models.utilities.build_final_list_of_coords import build_final_list_of_coords
from src.models.utilities.build_final_output_string import build_final_output_string
from src.models.utilities.find_move_used import find_move_used
from src.models.word_finder.word_finder import search_grid_for_all_instances_of_first_letter, \
    find_possible_second_letter_coords, search_surrounding_spaces_for_second_letter, search_remaining_letters_in_a_line


def begin_search(words_to_find, puzzle_grid, final_output_list):
    for word in words_to_find:
        letter = word[0]
        first_letter_coords = search_grid_for_all_instances_of_first_letter(puzzle_grid, letter)
        final_output_string = __find_second_letter_matches(first_letter_coords, word, puzzle_grid)
        if final_output_string is not None:
            final_output_list.append(final_output_string)
    return final_output_list


def __find_second_letter_matches(first_letter_coords, word, puzzle_grid):
    for coord_to_check in first_letter_coords:
        possible_moves = find_possible_second_letter_coords(coord_to_check)
        final_output_string = __get_matched_second_letter_coords(word[1], possible_moves, puzzle_grid, coord_to_check, word)
        if final_output_string is not None:
            return final_output_string
    return None


def __get_matched_second_letter_coords(letter, possible_moves, puzzle_grid, coord_to_check, word):
    matches = search_surrounding_spaces_for_second_letter(letter, possible_moves, puzzle_grid)
    final_output_string = __get_move_used(matches, coord_to_check, word, puzzle_grid)
    if final_output_string is not None:
        return final_output_string
    return None


def __get_move_used(matches, coord_to_check, word, puzzle_grid):
    for match in matches:
        move_used = find_move_used(coord_to_check, match)
        final_output_string = __check_if_path_matches_rest_of_word(match, move_used, word, puzzle_grid, coord_to_check)
        if final_output_string is not None:
            return final_output_string
    return None


def __check_if_path_matches_rest_of_word(match, move_used, word, puzzle_grid, coord_to_check):
    result = search_remaining_letters_in_a_line(match, move_used, word, puzzle_grid)
    if result is not None:
        final_output_string = __create_list_of_found_word_coords(result, coord_to_check, match, word)
        return final_output_string
    return None


def __create_list_of_found_word_coords(result, coord_to_check, match, word):
    final_list_of_word_coords = build_final_list_of_coords(coord_to_check, match, result)
    final_output_string = __get_output_string(word, final_list_of_word_coords)
    return final_output_string


def __get_output_string(word, final_list_of_word_coords):
    final_output_string = build_final_output_string(word, final_list_of_word_coords)
    return final_output_string

