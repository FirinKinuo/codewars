from string import ascii_lowercase


def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(x)+1) for x in text.lower() if x in ascii_lowercase)
