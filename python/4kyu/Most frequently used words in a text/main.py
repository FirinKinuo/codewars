import re
from collections import Counter


def remove_invalid_apostrophe(text: str) -> str:
    return text.replace("'", '') if re.match(r'\'+$|(\'+.+\'+)', text) is not None else text


def top_3_words(text: str) -> list:
    text = re.sub(r"[!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~]", ' ', text).lower().split()
    text = [remove_invalid_apostrophe(word) for word in text]

    return [word[0] for word in Counter(text).most_common(3) if word[0]]
