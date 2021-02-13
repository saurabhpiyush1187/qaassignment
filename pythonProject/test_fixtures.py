import pytest
@pytest.fixture()
def setup():
    print("\n Fixture calling set up")

@pytest.mark.usefixtures("setup")
def test1():
    print("\n Calling test1")

def test2(setup):
    print("\n Calling test2")
