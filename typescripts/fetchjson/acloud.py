colors = ['blue', 'red', 'green', 'purple']
for color in colors:
    # print(color)
    if color == 'blue':
        continue
    if color == 'green':
        break
    else:
        print(color)



def multi(m):
    """Multiplies strings
    >>> multi("p")
    'p p '
    """
    return (m + " ") * 2


print(map(multi, colors))

def add(a,b):
    """
    Sum of 2 numbers
    >>> add(2,3)
    5
    """
    return a + b

from functools import reduce
def addNumbers(numList):
    return reduce(add, numList)


nums = list(range(0,11))
print(addNumbers(nums))
