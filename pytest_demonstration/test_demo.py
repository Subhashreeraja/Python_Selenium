import pytest
@pytest.mark.greater
def test_sample_one():
    assert 6>1
    # print("hai")
@pytest.mark.equal    
def test_sample_two():
    assert 4==3
    # print("hello") 
def test_sample_three():
    assert 6!=0
    # print("subha")
@pytest.mark.xfail  
def test_sample_four():
     a="subha"
     b="subhas"
     assert a.__eq__(b)    
@pytest.mark.xfail  
def test_sample_five():
     a="subhashree"
     b="subhashree"
     assert a.__eq__(b)        