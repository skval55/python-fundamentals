def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse_lst = []
    reverse = reversed(phrase)
    for letter in reverse:
        reverse_lst.append(letter)
    return ''.join(reverse_lst)
