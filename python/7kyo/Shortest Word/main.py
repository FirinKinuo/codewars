def find_short(words: str) -> int:
    words =  words.split(" ")
    return len([x for x in words if len(x) == sorted(map(len, words))[0]][0])
