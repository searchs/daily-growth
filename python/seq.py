"""Implement Sequences from scratch"""


class Items:
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)


# Test
nums = [1, 2, 3, 4, 5]
items = Items(1, 2, 3, 4, 5)
assert items.__len__() == 5
assert items.__getitem__(3) == 4
