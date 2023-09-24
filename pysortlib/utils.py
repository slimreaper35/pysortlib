from __future__ import annotations


def swap(array: list[int], index_1: int, index_2: int) -> None:
    """Swap two elements in the array."""
    array[index_1], array[index_2] = array[index_2], array[index_1]
