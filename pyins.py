"""Using in-built Python features to solve problems faster"""

countries = ["Netherlands", "Nigeria", "Jordan", "Nepal", "Niger", "Japan"]
capitals = ["Amsterdam", "Abuja", "Amman", "Kathmandu", "Niamey", "Tokyo"]
pairs = list(zip(countries, capitals))
print(pairs)

country, capital = zip(*pairs)
print(country)
print(capital)


years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
births = [
    723_165,
    723_913,
    729_674,
    698_512,
    695_233,
    697_852,
    696_271,
    679_106,
    657_076,
    640_370,
]


def annual_births_average(years=years, births=births):
    """Return a list of tuples with each entry in this format
    (year, birth, running_average)
    Round the running average to the nearest integer"""
    result = []
    sum_ = 0
    for index, (year, birth) in enumerate(zip(years, births), start=1):
        sum_ += birth
        result.append((year, birth, round(sum_ / index)))
    return result


year_births = list(zip(years, births))
print(year_births)
print(annual_births_average(years=years, births=births))

import re


def remove_punctuation(words):
    return re.sub("\W+", "", words)


tword = "What is the door?!"
print(remove_punctuation(tword))


def is_palindrome(term):
    word = remove_punctuation(term).lower()
    return word == "".join(reversed(word))


print(is_palindrome("Mallam"))
print(is_palindrome("madam"))
print(is_palindrome("bosch"))

