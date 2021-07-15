def open_or_senior(data):
    return list(map(lambda x: "Senior" if x[0]>=55 and x[1]>7 else "Open", data))