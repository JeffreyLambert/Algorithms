import pytest
from src.algorithms import binary_search

"""
Testing Strategy for binary_search
Inputs can be partitioned into a 3 by 3 search space of int, str, and float inputs as
well as empty lists and nulls

We will attempt the following test cases
Test 1: Value is same type as list elements, find index where value is stored, return integer
Test 2: Value is different type than list elements, throw error
Test 3: Value is not in the list, return None
Test 4: Value is any type and list is empty, throw error
Test 5: List is length 1
Test 6: List is length 1000 (if it works for this, it should work for all cases of length > 1000)
"""


@pytest.mark.parametrize(
    "test_value, test_space, expected",
    [
        (3, [*range(10)], 3),
        ('orange', ['banana', 'apple', 'orange'], 2),
        (3, [*range(0, 100, 2)], None),
        (2, [*range(2, 4, 2)], 0),
        (375, [*range(1000)], 375)
    ]
)
def test_binary_search(test_value, test_space, expected):
    test_result = binary_search(test_value, test_space)
    assert test_result == expected


@pytest.mark.parametrize(
    "test_value, test_space",
    [('orange', [0, 1, 2, 3, 4]),
     ('orange', [])]
)
def test_binary_search_throws_assertion_error(test_value, test_space):
    with pytest.raises(AssertionError):
        binary_search(test_value, test_space)


