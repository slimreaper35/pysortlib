from __future__ import annotations

from typing import Callable

import pytest
from hypothesis import given
from hypothesis.strategies import integers, lists

from pysortlib.sorting import (
    bubble_sort,
    cycle_sort,
    heap_sort,
    insert_sort,
    merge_sort,
    pancake_sort,
    quick_sort,
    selection_sort,
    shell_sort,
)


@pytest.mark.parametrize(
    "func",
    [
        bubble_sort,
        cycle_sort,
        heap_sort,
        insert_sort,
        pancake_sort,
        selection_sort,
        shell_sort,
    ],
)
@given(lists(integers()))
def test_sorting_common(func: Callable[[list[int]], None], array: list[int]) -> None:
    sorted_copy = sorted(array)
    func(array)
    assert array == sorted_copy


@given(lists(integers()))
def test_merge_sort(array: list[int]) -> None:
    result = merge_sort(array)
    assert result == sorted(array)


@given(lists(integers()))
def test_quick_sort(array: list[int]) -> None:
    sorted_copy = sorted(array)
    quick_sort(array, 0, len(array) - 1)
    assert array == sorted_copy
