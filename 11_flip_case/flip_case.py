def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = []
    for char in phrase:
        lower_char = char.lower()
        if lower_char == to_swap.lower():
            new_phrase.append(char.swapcase())
        else:
            new_phrase.append(char)
    return ''.join(new_phrase)
