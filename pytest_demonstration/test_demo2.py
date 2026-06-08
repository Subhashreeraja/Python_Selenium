import pytest
@pytest.mark.greater
def test_sample_one():
    assert 6>1
    # print("hai")
@pytest.mark.equal    
def test_sample_two():
    assert 4==4
    # print("hello")
    
@pytest.mark.not_equal   
def test_sample_three():
    assert 6!=0
    # print("subha")    
    
 