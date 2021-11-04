# More collections: counters,d efaultdict, chainmap

import urllib.request

url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
response = urllib.request.urlopen(url)
words = response.read().decode().split()
word_count = len(words)  # 858
print(word_count)

import collections

word_counter = collections.Counter(words)

for word, count in word_counter.most_common(5):
    print(word, " - ", count)


# DefaultDict
# Plain code


d = {}


def func_x(x):
    try:
        d[x] += 1
    except KeyError:
        d[x] = 1


# defaultdict
dd = collections.defaultdict(list)


def funcs(x):
    dd[x] += 1


# Audit Trail
_audit = collections.defaultdict(lambda: ["Area created"])


def add_audit(area, action):
    _audit[area].append(action)


def report_audit():
    for area, actions in _audit.items():
        print(f"{area} audit:")
        for action in actions:
            print(f" - {action}")
        print()


# test
print("\n\tValidating Audit Trail\n")
add_audit("\tHR", "Hired Sam")
add_audit("\tFinance".upper(), "Used 1000£")
add_audit("\tHR", "Hired Tom")
report_audit()


# ChainMaps
import collections

_defaults = {
    "appetizers": "Hummus",
    "main": "Pizza",
    "dessert": "Chocolate cake",
    "drink": "Water",
}


def prepare_menu(customizations):
    return collections.ChainMap(customizations, _defaults)


def print_menu(menu):
    for key, value in menu.items():
        print(f"As {key}: {value}.")


# test ChainMaps
print("\n\tChecking ChainMaps\n")
menu1 = prepare_menu({})
print(menu1)
