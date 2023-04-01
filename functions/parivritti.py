def parivritti(list_variable, index, new_value):
    try:
        list_variable[index] = new_value
    except IndexError:
        raise IndexError(f"list index '{index}' out of range")
