def uttara_vibhajana(string, index):
    """
    Splits a string into two parts at the specified index.

    Parameters:
        string (str): The string to split.
        index (int): The index at which to split the string.

    Returns:
        A tuple containing the two parts of the split string.
    """
    return (string[:index], string[index:])
