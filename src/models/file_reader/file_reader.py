import os


def file_reader():
    grid_list = []
    models_dir = os.path.dirname(os.path.dirname(__file__))
    input_filepath = os.path.join(models_dir, "input", "input.txt")

    with open(input_filepath, "r") as infile:
        for index, line in enumerate(infile):
            if index == 0:
                temp_string = line.strip('\n')
                words_to_find = temp_string.split(',')
            else:
                temp_grid_string = line.strip('\n')
                row = temp_grid_string.split(',')
                grid_list.append(row)

    result = (words_to_find, grid_list)
    return result

