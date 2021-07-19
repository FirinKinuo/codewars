from string import ascii_uppercase, ascii_lowercase, ascii_letters


def rot13(message):
    return ''.join([ascii_lowercase[ascii_lowercase.index(x) + 13 - 26] if x in ascii_lowercase else ascii_uppercase[
        ascii_uppercase.index(x) + 13 - 26] if x in ascii_letters else x for x in message])
