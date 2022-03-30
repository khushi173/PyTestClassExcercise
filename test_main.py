import main
import pytest

@pytest.mark.skip()
@pytest.mark.parametrize("num,output",[(5,True),(4,True),(7,True),(10,False)])
def test_isprime(num,output):
    result = main.isprime(num)
    assert result == output

@pytest.mark.xfail
@pytest.mark.parametrize("num,output",[(151,True),(144,False),(717,True),(101,False)])
def test_ispalindrome(num,output):
    result = main.ispalindrome(num)
    assert result == output
