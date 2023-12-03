'''
By Eng. Hosam El Nagar
On 1-12-2023
'''

def isprime(num):
    '''
    takes an integer and returns True
    if it is a prime number, and False otherwise.
    A prime number is an integer larger than 1
    that can only be divided by 1 and itself.
    '''
    x = [num%i for i in range(num-1,1,-1)]
    return all(x)

def isprime2(n):
  for i in range(2, n):
    if n % i == 0:
        return False
  return True


def allprimes(num):
    '''
    returns all prime numbers equal
    or less than num
    '''
    return [i for i in range(num+1) if isprime(i)]
