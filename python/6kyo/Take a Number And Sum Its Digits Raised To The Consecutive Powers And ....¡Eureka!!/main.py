def sum_dig_pow(a, b):
    return [i for i in range(a, b+1) if i == sum([int(value)**(pos+1) for pos, value in enumerate(str(i))])]
