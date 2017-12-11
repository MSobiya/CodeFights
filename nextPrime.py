'''
Find the smallest prime number strictly greater than the given n.

Example

For n = 7, the output should be
nextPrime(n) = 11.

'''
def nextPrime(n):
    j = n + 1
    while True:
        if(isPrime(j)):
            print(j)
            break
        j += 1
def isPrime(n):
    for i in range(2,n):
        if(n%i == 0):
            return False
            break
    return True
nextPrime(7)
