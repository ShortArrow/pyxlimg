from PIL import Image
import PIL
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


def test_openbook(TargetBook: xlimg.ImageBook):
    assert TargetBook.name == TestBookName


def test_count_sheets(TargetBook: xlimg.ImageBook):
    assert len(TargetBook.Sheets) == 3


imagesCountData = [(0, 0), (1, 2), (2, 2)]


@pytest.mark.parametrize("index,count", imagesCountData)
def test_count_images(TargetBook: xlimg.ImageBook, index, count):
    assert len(TargetBook.Sheets[index].Pictures) == count


SheetNameData = [(0, "Marshmallow"), (1, "containSVG"), (2, "PolkaDot")]


@pytest.mark.parametrize("index,sheetname", SheetNameData)
def test_get_sheetname(TargetBook: xlimg.ImageBook, index, sheetname):
    assert TargetBook.Sheets[index].displayName == sheetname


def test_get_image(TargetBook: xlimg.ImageBook):
    targetImage: Image.Image = TargetBook.Sheets[1].Pictures[0].Image()
    assert isinstance(targetImage, Image.Image)
