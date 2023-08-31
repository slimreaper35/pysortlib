from __future__ import annotations

import pytest
from hypothesis import given
from hypothesis.strategies import integers, lists

from pysortlib.sorting import (
    bubble_sort,
    counting_sort,
    heap_sort,
    insert_sort,
    merge_sort,
    quick_sort,
    radix_sort,
    selection_sort,
)


@given(lists(integers()))
def test_insert_sort(array: list[int]) -> None:
    sorted_copy = sorted(array)
    insert_sort(array)
    assert array == sorted_copy


@given(lists(integers()))
def test_bubble_sort(array: list[int]) -> None:
    sorted_copy = sorted(array)
    bubble_sort(array)
    assert array == sorted_copy


@given(lists(integers()))
def test_merge_sort(array: list[int]) -> None:
    result = merge_sort(array)
    assert result == sorted(array)


@given(lists(integers()))
def test_selection_sort(array: list[int]) -> None:
    sorted_copy = sorted(array)
    selection_sort(array)
    assert array == sorted_copy


@given(lists(integers()))
def test_quick_sort(array: list[int]) -> None:
    sorted_copy = sorted(array)
    quick_sort(array, 0, len(array) - 1)
    assert array == sorted_copy


@given(lists(integers()))
def test_heap_sort(array: list[int]) -> None:
    sorted_copy = sorted(array)
    heap_sort(array)
    assert array == sorted_copy


@given(lists(integers(min_value=0, max_value=10)))
def test_counting_sort(array: list[int]) -> None:
    result = counting_sort(array, max_value=10)
    assert result == sorted(array)


@pytest.mark.parametrize("array", [[-1, 0], [0, -1]])
def test_counting_sort_with_negative_integers(array: list[int]) -> None:
    with pytest.raises(ValueError) as exc:
        counting_sort(array, max_value=1)
    assert str(exc.value) == "The array should contain only non-negative integers"


@given(lists(integers(min_value=0, max_value=999)))
def test_radix_sort(array: list[int]) -> None:
    result = radix_sort(array, max_digits=3)  # 999 -> max_digits = 3
    assert result == sorted(array)


@pytest.mark.parametrize("array", [[-1, 0], [0, -1]])
def test_radix_sort_with_negative_integers(array: list[int]) -> None:
    with pytest.raises(ValueError) as exc:
        radix_sort(array, max_digits=1)
    assert str(exc.value) == "The array should contain only non-negative integers"
