def is_isogram(string: str) -> bool:
    string = string.lower()
    return all(string.count(letter) == 1 for letter in string)
