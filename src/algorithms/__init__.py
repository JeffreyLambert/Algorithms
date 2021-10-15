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


def binary_search(value: Any, space: List) -> int:
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

    # Copy keeps original argument passed safe from changes
    search_space = [*range(len(space))]

    # List must be sorted for binary search to work
    search_space.sort()

    try:
        index = None
        lower = search_space[0]
        upper = search_space[-1]
        counter = 0
        while counter < 100:
            counter += 1
            mid = int(round(((upper + lower) / 2), 0))
            if space[mid] < value:
                lower = mid + 1
            elif space[mid] > value:
                upper = mid - 1
            elif space[mid] == value:
                index = mid
                break

        if index is None:
            print("Value was not found in the list.")

        return index
    except Exception as e:
        print(e)