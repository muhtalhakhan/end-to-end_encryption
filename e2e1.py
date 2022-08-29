from e2e import *

def swap_letters(message):
    letters_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)

    for counter in range(0, int(len(message)/2)):
        letters_list.append(odd_letters[counter])
        letters_list.append(even_letters[counter])
    new_message = ''.join(letters_list)
    return new_message    