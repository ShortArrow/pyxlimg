import pytest
from pyxlimg import xlimg
from time import time


TestBookName = "./tests/testdata/TestBook.xlsx"


@pytest.fixture
def TargetBook() -> xlimg.ImageBook:
    theBook: xlimg.ImageBook = xlimg.ImageBook()
    theBook.open(TestBookName)
    yield theBook


def test_openspeed():
    startTime = time()
    theBook: xlimg.ImageBook = xlimg.ImageBook()
    theBook.open(TestBookName)
    finishTime = time()
    spentTime = finishTime - startTime
    assert spentTime <= 0.2


def test_openbook(TargetBook):
    assert TargetBook.name == TestBookName


def test_count_sheets(TargetBook):
    assert len(TargetBook.Sheets) == 3


imagesCountData = [(0, 0), (1, 2), (2, 2)]


@pytest.mark.parametrize("index,count", imagesCountData)
def test_count_images(TargetBook, index, count):
    thisTarget: xlimg.ImageBook = TargetBook
    assert len(thisTarget.Sheets[index].Pictures) == count


SheetNameData = [(0, "Marshmallow"), (1, "containSVG"), (2, "PolkaDot")]


@pytest.mark.parametrize("index,sheetname", SheetNameData)
def test_get_sheetname(TargetBook, index, sheetname):
    thisTarget: xlimg.ImageBook = TargetBook
    assert thisTarget.Sheets[index].displayName == sheetname
