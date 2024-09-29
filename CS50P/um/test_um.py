from um import count

def test_count0():
    assert count("Hello, Samar!") == 0


def test_count1():
    assert count("Um, thanks for the album.") == 1
    assert count("um?") == 1


def test_count2():
    assert count("Um, are these yours? um, I guess so") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2


