"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
import sys

sys.setrecursionlimit(10000)


def test_extract():
    assert extract() == "dataset/listings.csv"


def test_transform_load():
    assert load() == "airbnb.db"


def test_query():
    assert query() == "Success"
