from seasons import minutes, convertToWords, check
from pytest import raises


def test_minutes_and_convertToWords():
    assert minutes("2004-08-22") == 9453600 and convertToWords(9453600) == "Nine million, four hundred fifty-three thousand, six hundred minutes"
    assert minutes("1999-01-01") == 12420000 and convertToWords(12420000) == "Twelve million, four hundred twenty thousand minutes"


def test_check():
    with raises(SystemExit):
        check("cat")
        check("August 8, 2004")
        