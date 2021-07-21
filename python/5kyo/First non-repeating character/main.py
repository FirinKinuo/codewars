def first_non_repeating_letter(string: str) -> str:
    return str().join(x for x in string if string.lower().count(x.lower()) == 1)[:1]
