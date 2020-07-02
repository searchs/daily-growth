from functools import partial


def add(a, b):
    return a + b


add_two = partial(add, 2)
print(add_two(7))


def add(A):
    def inner(b):
        # Use `A` from the argument in
        # the parent add() function.
        return A + b

    return inner


add_two = add(2)
print(add_two(7))
