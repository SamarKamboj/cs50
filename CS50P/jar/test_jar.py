from jar import Jar
from pytest import raises


def test_init():
    jar = Jar(20)
    assert jar.capacity == 20

    with raises(ValueError):
        Jar(-2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12

    with raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9

    with raises(ValueError):
        jar.withdraw(10)

