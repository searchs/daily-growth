"""Small, dependency-free word-length exercise migrated from the old pybox sandbox."""

from __future__ import annotations

import re
from dataclasses import dataclass

_WORD = re.compile(r"[A-Za-z]+")


@dataclass(frozen=True)
class WordLengthResult:
    words: tuple[str, ...]
    length: int


def normalise_words(sentence: str | None) -> tuple[str, ...]:
    """Return unique lowercase alphabetic words in stable sorted order."""
    if not sentence:
        return ()
    return tuple(sorted(set(word.lower() for word in _WORD.findall(sentence))))


def longest_words(sentence: str | None) -> WordLengthResult | None:
    words = normalise_words(sentence)
    if not words:
        return None
    length = max(map(len, words))
    return WordLengthResult(tuple(word for word in words if len(word) == length), length)


def shortest_words(sentence: str | None) -> WordLengthResult | None:
    words = normalise_words(sentence)
    if not words:
        return None
    length = min(map(len, words))
    return WordLengthResult(tuple(word for word in words if len(word) == length), length)
