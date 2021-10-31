import pytest
from src.algorithms import quicksort

"""
Testing strategy for selection sort

Input space can be partitioned into: homogeneous list, heterogeneous list, 
    null list, list with single element

Test 1: Homogeneous list of ints, returns sorted list
Test 2: Homogeneous list of floats, returns sorted list
Test 2: Heterogeneous list, throws error
Test 3: list with single element, returns list
"""


class TestQuicksort:

    @pytest.mark.parametrize(
        "test_input, expected_output",
        [
            ([11, 25, 12, 22, 64], [11, 12, 22, 25, 64]),
            ([11.5, 11.3, 20.0, 18.0, 15.1], [11.3, 11.5, 15.1, 18.0, 20.0])
        ]

    )
    def test_selection_sort(self, test_input, expected_output):
        output = quicksort(test_input)
        assert output == expected_output

    @pytest.mark.parametrize(
        "test_input, expected_output",
        [
            ([12, 43, 'banana', 1.0], AssertionError)
        ]
    )
    def test_selection_sort_throws_error(self, test_input, expected_output):
        with pytest.raises(expected_output):
            quicksort(test_input)
