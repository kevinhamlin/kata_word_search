import os


def file_reader():
    models_dir = os.path.dirname(os.path.dirname(__file__))
    input_filepath = os.path.join(models_dir, "input", "input.txt")

    with open(input_filepath, "r") as infile:
        return parse_file(infile)


def parse_file(infile):
    grid_list = []
    words_to_find = []

    for index, line in enumerate(infile):
        if index == 0:
            words_to_find = scrub_row(line)
        else:
            grid_list.append(scrub_row(line))
    return words_to_find, grid_list


def scrub_row(line):
    row = line.strip('\n').split(',')
    return row

