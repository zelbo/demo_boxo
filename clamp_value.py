def clamp(value, minimum_value, maximum_value):
    if value < minimum_value:
        return minimum_value
    if value > maximum_value:
        return maximum_value
    return value
