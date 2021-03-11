# import os
# import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from pyxlimg import xlimg


def test_openbook():
    TargetBook:xlimg.ImageBook = xlimg.ImageBook
    TargetBook.open("testdata/TestBook.xlsx")
    assert TargetBook.name == "TestBook"