import pytest
from src.algorithms import selection_sort

"""
Testing strategy for selection sort

Input space can be partitioned into: homogeneous list, heterogeneous list, 
    null list, list with single element

Test 1: Homogeneous list, returns sorted list
Test 2: Heterogeneous list, throws error
Test 3: empty list, throws error
Test 4: list with single element, returns list
"""

class TestSelectionSort:

    @pytest.mark.parametrize(
        "test_input, expected_output",
        [
            ([11, 25, 12, 22, 64], [11, 12, 22, 25, 64])
        ]

    )
    def test_selection_sort(self, test_input, expected_output):
        output = selection_sort(test_input)
        assert output == expected_output

    @pytest.mark.parametrize(
        "test_input, expected_output",
        [
            ([12, 43, 'banana', 1.0], AssertionError),
            ([], AssertionError)
        ]
    )
    def test_selection_sort_throws_error(self, test_input, expected_output):
        with pytest.raises(expected_output):
            selection_sort(test_input)


