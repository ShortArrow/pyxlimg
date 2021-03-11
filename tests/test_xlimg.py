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


imagesCountData = [(0, 0), (1, 2), (2, 1)]


@pytest.mark.parametrize("index,count", imagesCountData)
def test_count_images(TargetBook, index, count):
    thisTarget: xlimg.ImageBook = TargetBook
    assert len(thisTarget.Sheets[index].Pictures) == count


def test_get_sheetname(TargetBook):
    thisTarget: xlimg.ImageBook = TargetBook
    assert thisTarget.Sheets[0].displayName == "Marshmallow"
