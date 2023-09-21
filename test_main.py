from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(6)) == 4*6
    assert quadratic_multiply(BinaryNumber(9), BinaryNumber(10)) == 9*10
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(2)) == 5*2