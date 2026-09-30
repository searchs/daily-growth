"""Search algorithm examples migrated and curated from searchs/algorithms."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def linear_search(items: Sequence[T], key: T) -> bool:
    """Return True when *key* exists in *items*. O(n)."""
    return any(item == key for item in items)


def binary_search_recursive(items: Sequence[T], key: T) -> bool:
    """Recursively search a sorted sequence. O(log n) comparisons."""
    if not items:
        return False

    mid = len(items) // 2
    if items[mid] == key:
        return True
    if key < items[mid]:
        return binary_search_recursive(items[:mid], key)
    return binary_search_recursive(items[mid + 1 :], key)


def binary_search_iterative(items: Sequence[T], key: T) -> int | None:
    """Return the index of *key* in a sorted sequence, or None."""
    start = 0
    stop = len(items) - 1

    while start <= stop:
        mid = (start + stop) // 2
        if items[mid] == key:
            return mid
        if key > items[mid]:
            start = mid + 1
        else:
            stop = mid - 1

    return None


if __name__ == "__main__":
    values = [1, 2, 3, 5, 8, 13, 21]
    assert linear_search(values, 8)
    assert binary_search_recursive(values, 13)
    assert binary_search_iterative(values, 5) == 3
    assert binary_search_iterative(values, 4) is None
