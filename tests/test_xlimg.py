import os
# import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from pyxlimg import xlimg


def test_openbook():
    TestBookName = "./tests/testdata/TestBook.xlsx"
    TargetBook:xlimg.ImageBook = xlimg.ImageBook()
    TargetBook.open(TestBookName)
    assert TargetBook.name == TestBookName


def test_count_sheets():
    TestBookName = "./tests/testdata/TestBook.xlsx"
    TargetBook:xlimg.ImageBook = xlimg.ImageBook()
    TargetBook.open(TestBookName)
    assert len(TargetBook.Sheets) == 3