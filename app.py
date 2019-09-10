from src.models.controller.controller import begin_search
from src.models.file_reader.file_reader import file_reader

words_to_find, puzzle_grid = file_reader()
final_output_list = []

final_output_list = begin_search(words_to_find, puzzle_grid, final_output_list)

for output_string in final_output_list:
    print(output_string)