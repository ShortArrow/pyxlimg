import pytest
from pyxlimg import xlimg


TestBookName = "./tests/testdata/TestBook.xlsx"

@pytest.fixture
def TargetBook():
    theBook: xlimg.ImageBook = xlimg.ImageBook()
    theBook.open(TestBookName)
    yield theBook

def test_openbook(TargetBook):
    assert TargetBook.name == TestBookName


def test_count_sheets(TargetBook):
    assert len(TargetBook.Sheets) == 3