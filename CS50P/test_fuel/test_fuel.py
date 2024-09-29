from fuel import convert, gauge
from pytest import raises

def test_convertValue():
    with raises(ValueError):
        convert("four/three")
        convert("1.5/3")
        convert("1/1.5")


def test_convertZero():
    with raises(ZeroDivisionError):
        convert("1/0")


def test_convert():
    assert convert("4/4") == 100
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("1/101") == 1


def test_guage():
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'
    assert gauge(1) == 'E'

