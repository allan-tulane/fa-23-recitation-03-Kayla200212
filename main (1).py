"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    ### TODO
    yvec = y.binary_vec #step 1
    xvec = x.binary_vec #step 1
    
    #step 2 (padding 0's)
    #we decide how many 0s to pad based on the diff in length of x and y
    #ex if y is 421 and x is 32, add len(y)(3) minus len(x)(2) zeros (one 0)
    if len(yvec) != len(xvec):#if their lengths r unequal
      if len(yvec) > len(xvec):#if length of y is longer
        xvec.zfill(len(yvec)-len(xvec))
        n = len(yvec)
      elif len(xvec) > len(yvec):
        yvec.zfill(len(yvec)-len(xvec))
        n = len(xvec)
    else:
      n = len(xvec)#if lengths are the same just make n the len of x
    #do i need an else bc if theyre equal we don't need to do anything to len
    #Base: If both x and y are <= 1, then return their product (step 3)
    #their values or their lengths?
    if len(xvec) <= 1 & len(yvec) <= 1:
      return xvec * yvec #or x&y?
    else:#split `xvec` and `yvec` into two halves each
      x_left, x_right = split_number(xvec)
      y_left, y_right = split_number(yvec)

    #Anywhere there is a multiply(xy), call `_quadratic_multiply`(step 5)
    prod1 = _quadratic_multiply(x_left, y_left)
    prod2 = _quadratic_multiply(x_left, y_right)
    prod3 = _quadratic_multiply(x_right, y_left)
    prod4 = _quadratic_multiply(x_right, y_right)
    #Use `bit_shift` to do the 2^n and 2^{n/2} multiplications.(step 6)
    exp = bit_shift(BinaryNumber(2), n).decimal_val#2^n
    exp2 = bit_shift(BinaryNumber(2), n//2).decimal_val#2^n/2
    #combine it all (step 7)
    return exp*prod1 + exp2*(prod2+prod3)+prod4
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    #return _quadratic_multiply(x, y)
    f(x,y)
    return (time.time() - start)*1000


    
    

