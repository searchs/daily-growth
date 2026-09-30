"""Sorting algorithm examples migrated and curated from searchs/algorithms."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def bubble_sort(items: Sequence[T]) -> list[T]:
    """Return a sorted copy using bubble sort. O(n²)."""
    result = list(items)
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(result) - 1):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
    return result


def insertion_sort(items: Sequence[T]) -> list[T]:
    """Return a sorted copy using insertion sort. O(n²)."""
    result = list(items)
    for marker in range(1, len(result)):
        current = result[marker]
        index = marker - 1
        while index >= 0 and result[index] > current:
            result[index + 1] = result[index]
            index -= 1
        result[index + 1] = current
    return result


def selection_sort(items: Sequence[T]) -> list[T]:
    """Return a sorted copy using selection sort. O(n²)."""
    result = list(items)
    for marker in range(len(result)):
        smallest = marker
        for index in range(marker + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        result[marker], result[smallest] = result[smallest], result[marker]
    return result


def merge(left: Sequence[T], right: Sequence[T]) -> list[T]:
    """Merge two sorted sequences."""
    result: list[T] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(items: Sequence[T]) -> list[T]:
    """Return a sorted copy using merge sort. O(n log n)."""
    if len(items) < 2:
        return list(items)

    midpoint = len(items) // 2
    return merge(merge_sort(items[:midpoint]), merge_sort(items[midpoint:]))


def quick_sort(items: Sequence[T]) -> list[T]:
    """Return a sorted copy using a simple three-way quicksort."""
    if len(items) < 2:
        return list(items)

    pivot = items[-1]
    smaller = [value for value in items if value < pivot]
    equal = [value for value in items if value == pivot]
    larger = [value for value in items if value > pivot]
    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    values = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
    expected = sorted(values)

    assert bubble_sort(values) == expected
    assert insertion_sort(values) == expected
    assert selection_sort(values) == expected
    assert merge_sort(values) == expected
    assert quick_sort(values) == expected
