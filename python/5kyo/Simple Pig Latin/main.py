from string import punctuation


def pig_it(text: str) -> str:
    return ' '.join(map(lambda word: word if word in punctuation else word[1:] + word[0] + 'ay', text.split(" ")))
