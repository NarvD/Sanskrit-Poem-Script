def visarga(list_variable, item):
    if item in list_variable:
        list_variable.remove(item)
    else:
        list_variable.append(item)
    return list_variable
