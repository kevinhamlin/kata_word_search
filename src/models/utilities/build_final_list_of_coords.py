
def build_final_list_of_coords(coord_to_check, match, result):
    found_word_coords = [coord_to_check, match]

    for coord in result:
        found_word_coords.append(coord)

    return found_word_coords
