from twttr import shorten

def test_shorten():
    assert shorten("Samar!1234") == "Smr!1234"
    assert shorten("twItter") == "twttr"
    assert shorten("vibhu") == "vbh"
    assert shorten("sanjeev") == "snjv"
    assert shorten("ritu,") == "rt,"

