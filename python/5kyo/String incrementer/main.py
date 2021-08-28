import re


def increment_string(string: str) -> str:
    re_find_index = re.findall(r'(\d+)', string)
    old_index = re_find_index[-1] if re_find_index else ''
    new_index = f"{(int(old_index or 0) + 1):0{len(old_index)}}"
    return string.replace(old_index, new_index) if old_index else string + new_index
