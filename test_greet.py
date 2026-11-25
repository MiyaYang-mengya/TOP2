from greet import greet, farewell


def test_greet():
    assert greet("world") == "hello, world"
    print("CI PASS: greet works")


def test_farewell():
    assert farewell("world") == "bye, world"
    print("CI PASS: farewell works")


if __name__ == "__main__":
    test_greet()
    test_farewell()
