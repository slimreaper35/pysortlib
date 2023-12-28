from __future__ import annotations

import time

import pytest
from hypothesis import given
from hypothesis.strategies import integers, lists

from pysortlib.sorting_extra import counting_sort, radix_sort, sleep_sort


@given(lists(integers(min_value=0, max_value=10)))
def test_counting_sort(array: list[int]) -> None:
    result = counting_sort(array, max_value=10)
    assert result == sorted(array)


@pytest.mark.parametrize(
    "array",
    [
        [-1, 0],
        [0, -1],
    ],
)
def test_counting_sort_with_negative_integers(array: list[int]) -> None:
    with pytest.raises(ValueError) as exc:
        counting_sort(array, max_value=1)
    assert str(exc.value) == "The array should contain only non-negative integers"


@given(lists(integers(min_value=0, max_value=999)))
def test_radix_sort(array: list[int]) -> None:
    result = radix_sort(array, max_digits=3)
    assert result == sorted(array)


@pytest.mark.parametrize(
    "array",
    [
        [-1, 0],
        [0, -1],
    ],
)
def test_radix_sort_with_negative_integers(array: list[int]) -> None:
    with pytest.raises(ValueError) as exc:
        radix_sort(array, max_digits=1)
    assert str(exc.value) == "The array should contain only non-negative integers"


@pytest.mark.parametrize(
    "array",
    [
        [],
        [0, 0],
        [20, 15, 10],
        [1, 9, 6, 7, 8, 5, 2, 3, 4],
    ],
)
def test_sleep_sort(array: list[int]) -> None:
    timeout = max(array, default=0) + 1

    start = time.time()
    result = sleep_sort(array)
    end = time.time()

    assert (end - start) < timeout
    assert result == sorted(array)
