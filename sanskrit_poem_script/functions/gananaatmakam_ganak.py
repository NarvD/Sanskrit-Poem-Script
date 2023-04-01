def gananaatmakam_ganak(collection, function):
    """
    Counts the number of elements in a collection that satisfy a condition.

    Parameters:
        collection (iterable): The collection to count.
        function (function): The function to use as the condition.

    Returns:
        The number of elements in the collection that satisfy the condition.
    """
    return sum(1 for item in collection if function(item))
