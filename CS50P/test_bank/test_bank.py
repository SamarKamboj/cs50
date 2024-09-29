from bank import value

def test_value():
    assert value("Hello, Newman") == 0
    assert value("Hey!") == 20
    assert value("What's up?") == 100
    assert value("hey, Samar") == 20
    assert value("hello, Samar") == 0
