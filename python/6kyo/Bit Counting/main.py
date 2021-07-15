from re import sub


def count_bits(n):
    return len(sub(r'[^1]', '', bin(n)))
