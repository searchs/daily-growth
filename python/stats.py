from typing import List
from loguru import logger

"""Basic stats in pure Python"""


def for_each(items, function):
    """Give Python  list super powers with foreach.  FP"""
    for k, v in enumerate(items):
        function(k, v, items)


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grade_vals):
    """print args"""
    for grade in grade_vals:
        # print(grade)
        logger.info(grade)


def grades_sum_old(scores):
    """Sum values in list"""
    total = 0
    for grade in scores:
        total += grade
    return total


def grades_sum(scores: List) -> int:
    """Add scores using recursion"""
    if not scores:
        return 0
    return scores[0] + grades_sum(scores[1:])


def grades_average(grades_list):
    """Return the average of the values parsed"""
    sum_of_grades = grades_sum(grades_list)
    return sum_of_grades / float(len(grades_list))


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2

    return variance / float(len(scores))


print(grades_variance(grades))


def grades_std_deviation(var):
    """Standard deviation calculation with variance"""
    return var**0.5


variance = grades_variance(grades)


print_grades(grades)
print("Grade Sum: ", grades_sum(grades))
print("Grade Average: ", grades_average(grades))
print("Standard Deviation: ", grades_std_deviation(variance))

print("==" * 75)
for_each(grades, print)
