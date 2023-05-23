def isPrime(num):

    for i in range(2, num-1):

        if num%i == 0:

            return False
        
    return True

def getPrimesInRange(min, max):

    primes = []

    for i in range(min, max+1):

        if i == 0: continue

        if isPrime(i):

            primes.append(i)

    return primes

print(getPrimesInRange(0,17))