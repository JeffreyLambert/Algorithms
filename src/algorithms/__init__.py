from typing import List, Union, Any


def simple_search(value: Any, space: List) -> Union[int, None]:
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
        return None


def binary_search(value: Any, space: List) -> Union[int, None]:
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
        return None


def selection_sort(sequence: List) -> Union[List, None]:
    """
    Takes in a sequence of sortable items and returns a sorted sequence of those items.

    Expects all elements of sequence to be same type and for sequence to not be empty.

    Args:
        sequence (list): list object

    Returns:
        list
    """
    assert len(sequence) > 0, "Sequence is empty.  Cannot sort empty sequence."
    assert all(isinstance(x, type(sequence[0])) for x in sequence), "Sequence contains multiple types."

    sorted_sequence = sequence.copy()
    n = len(sorted_sequence)
    try:
        # Loop through list
        for i in range(0, n, 1):
            jmin = i
            # Loop through remaining elements of list
            for j in range(i + 1, n, 1):
                if sorted_sequence[j] < sorted_sequence[jmin]:
                    jmin = j

            # Swap places between current element and smaller element found
            if jmin != i:
                sorted_sequence[i], sorted_sequence[jmin] = sorted_sequence[jmin], sorted_sequence[i]

        return sorted_sequence

    except Exception as e:
        print(e)
        return None


def quicksort(sequence: List[Union[int, float]]):
    """
    Sort an array using quicksort algorithm
    Args:
        sequence: array like object

    Returns:
        sorted array
    """
    assert all(isinstance(x, type(sequence[0])) for x in sequence), "Sequence contains multiple types."

    try:
        if len(sequence) <= 1:
            return sequence
        else:
            pivot = sequence[0]
            less = [x for x in sequence if x < pivot]
            greater = [x for x in sequence if x > pivot]
            return quicksort(less) + [pivot] + quicksort(greater)

    except Exception as e:
        print(e)