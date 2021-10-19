import re


def to_underscore(string: str) -> str:
    return "_".join(re.findall('.[^A-Z]*', str(string))).lower()
