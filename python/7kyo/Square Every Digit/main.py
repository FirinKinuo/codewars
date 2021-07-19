def square_digits(num: int) -> int:
    return int(''.join(str(x**2) for x in map(int, str(num))))