def reverse(obj):
    if type(obj) == str:
        return obj[::-1]
    elif type(obj) == list or type(obj) == tuple:
        return obj[::-1]
    else:
        raise TypeError("Object must be a string, list, or tuple")
