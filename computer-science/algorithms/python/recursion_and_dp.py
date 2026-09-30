"""Recursion and dynamic-programming examples curated from searchs/algorithms."""


def countdown(n: int) -> list[int]:
    """Return a recursive countdown sequence ending at zero."""
    if n <= 0:
        return [0]
    return [n, *countdown(n - 1)]


def fibonacci(n: int, memo: dict[int, int] | None = None) -> int:
    """Return the nth Fibonacci value using top-down memoisation."""
    if n < 0:
        raise ValueError("n must be non-negative")

    cache = memo if memo is not None else {0: 0, 1: 1}
    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]


def least_missing_positive(values: list[int]) -> int:
    """Return the smallest missing positive integer."""
    candidates = {value for value in values if value > 0}
    expected = 1
    while expected in candidates:
        expected += 1
    return expected


if __name__ == "__main__":
    assert countdown(3) == [3, 2, 1, 0]
    assert fibonacci(0) == 0
    assert fibonacci(5) == 5
    assert least_missing_positive([1, 3, 6, 4, 1, 2]) == 5
    assert least_missing_positive([1, 2, 3]) == 4
    assert least_missing_positive([-1, -3]) == 1
