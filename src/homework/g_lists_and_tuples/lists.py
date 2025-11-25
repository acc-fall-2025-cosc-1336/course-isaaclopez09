def get_lowest_list_value(values):
    lowest = values[0]
    for v in values:
        if v < lowest:
            lowest = v
    return lowest

def get_highest_list_value(values):
    highest = values[0]
    for v in values:
        if v > highest:
            highest = v
    return highest