from typing import List, Union, Any


def simple_search(value: Any, space: List) -> int:
    """
    Return index value for item, if item is in the search space.

    If item is not in the list prints a message to the log and returns None.

    Args:
        value (any): Value to search for
        space (list): Search space

    Returns:
        int, index of list where value is stored
    """
    assert len(space) > 0, "Space must be not be empty"
    assert all(type(value) == type(x) for x in space), "All elements of space must be of same type as value"

    try:
        index = None
        for i, element in enumerate(space):
            if value == element:
                index = i
            else:
                pass
        print("Value was not found in the list.")
        return index
    except Exception as e:
        print(e)