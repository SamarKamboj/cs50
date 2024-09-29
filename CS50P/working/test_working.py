from pytest import raises
from working import convert

def test_convert1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:20 AM to 5:30 PM") == "09:20 to 17:30"
    assert convert("10:50 AM to 6 PM") == "10:50 to 18:00"
    assert convert("11 AM to 3:59 PM") == "11:00 to 15:59"
    assert convert("10 PM to 3 AM") == "22:00 to 03:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_convert2():
    with raises(ValueError):
        convert("9:00 to 17:00")
        convert("9:60 AM to 5:60 PM")
        convert("9AM to 5PM")


def test_convert3():
    with raises(ValueError):
        convert("9 AM - 5 PM")
        convert("10:7 AM - 5:1 PM")
