#!/usr/bin/env python

import json
import xml.etree.ElementTree as etree
import sqlite3


class JSONDataExtractor(object):
    """docstring for JSONDataExtractor."""
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


# import xml.etree.ElementTree as etree


class XMLDataExtractor(object):
    """docstring for JSONDataExtractor."""
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


class SQLiteDataExtractor(object):
    """docstring for JSONDataExtractor."""
    def __init__(self, filepath):
        self.data = sqlite3.connect(filepath)

    @property
    def parsed_data(self):
        return self.data


def data_extraction_factory(filepath):
    if filepath.endswith("json"):
        extractor = JSONDataExtractor
    elif filepath.endswith("xml"):
        extractor = XMLDataExtractor
    else:
        raise ValueError("Cannot extract data from {}".format(filepath))
    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    sqlite_factory = extract_data_from("data/person.sq3")
    print(sqlite_factory)


print("\n" + "==" * 65 + "\n")
print("Reading JSON file ")
json_factory = extract_data_from("data/movies.json")
json_data = json_factory.parsed_data
print("Found: {} movies.".format(len(json_data)))
for movie in json_data:
    print("Title: {}".format(movie['title']))
    year = movie["year"]
    if year:
        print("Year: {}".format(year))
    director = movie["director"]
    if year:
        print("Director: {}".format(director))
    genre = movie["genre"]
    if genre:
        print("Genre: {}".format(genre))

print("\n" + "==" * 65 + "\n")
print("Reading XML file")
xml_factory = extract_data_from('data/person.xml')
xml_data = xml_factory.parsed_data
liars = xml_data.findall(f".//person[lastName='Liar']")
print(f'found: {len(liars)} persons')
for liar in liars:
    firstname = liar.find('firstName').text
    print(f'first name: {firstname}')
    lastname = liar.find('lastName').text
    print(f'last name: {lastname}')
    [
        print(f"phone number ({p.attrib['type']}):", p.text)
        for p in liar.find('phoneNumbers')
    ]
