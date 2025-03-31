import pytest


#new
@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')




#new
def test_demo1():
    assert  1==1

#new
def test_demo2(before_after):
    assert  2==3
