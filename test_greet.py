from greet import greet

def test_greet():
    assert greet("world") == "hello, world"
    print("CI PASS: greet works")

if __name__ == "__main__":
    test_greet()
