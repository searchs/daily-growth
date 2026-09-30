from word_lengths import longest_words, shortest_words


def test_longest_words_returns_all_ties() -> None:
    result = longest_words("The cow jumped over the rock beside the moon.")
    assert result is not None
    assert set(result.words) == {"beside", "jumped"}
    assert result.length == 6


def test_shortest_words_returns_all_ties() -> None:
    result = shortest_words("The cow jumped over the rock beside the moon.")
    assert result is not None
    assert set(result.words) == {"cow", "the"}
    assert result.length == 3


def test_numbers_are_not_treated_as_words() -> None:
    result = longest_words("Please do not count 123456789 in the poem.")
    assert result is not None
    assert "123456789" not in result.words


def test_empty_input_returns_none() -> None:
    assert longest_words(None) is None
    assert shortest_words("") is None
