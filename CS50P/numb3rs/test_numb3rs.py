from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("256.255.255.255") == False
    assert validate("512.512.512.512") == False
    assert validate("64.128.256.512") == False
    assert validate("cat") == False
