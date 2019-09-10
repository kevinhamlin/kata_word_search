
def build_final_output_string(word, final_list_of_word_coords):
    output_string = word + ": "
    for index, coord in enumerate(final_list_of_word_coords):
        if index == len(final_list_of_word_coords) - 1:
            output_string = output_string + str(coord)
        else:
            output_string = output_string + str(coord) + ", "

    return output_string