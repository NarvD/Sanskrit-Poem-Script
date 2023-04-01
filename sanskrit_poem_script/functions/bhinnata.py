def bhinnata(list_variable, index):
    try:
        return list_variable[index]
    except IndexError:
        raise IndexError(f"list index '{index}' out of range")
