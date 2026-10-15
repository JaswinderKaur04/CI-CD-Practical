# from app import add


# def test_add():
#     assert add(10, 20) == 30


# def test_add_negative():
#     assert add(-5, 2) == -3



from app import add, multiply


def test_add():
    assert add(10, 20) == 30


def test_add_negative():
    assert add(-5, 2) == -3


def test_multiply():
    assert multiply(10, 20) == 200
