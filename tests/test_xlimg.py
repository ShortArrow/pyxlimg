import pytest
from pyxlimg import xlimg


TestBookName = "./tests/testdata/TestBook.xlsx"


@pytest.fixture
def TargetBook() -> xlimg.ImageBook:
    theBook: xlimg.ImageBook = xlimg.ImageBook()
    theBook.open(TestBookName)
    yield theBook


def test_openbook(TargetBook):
    assert TargetBook.name == TestBookName


def test_count_sheets(TargetBook):
    assert len(TargetBook.Sheets) == 3


def test_count_images1(TargetBook):
    thisTarget: xlimg.ImageBook = TargetBook
    assert len(thisTarget.Sheets[1].Pictures)