import math
from perf_measurer import log_time


@log_time
def solve(A): 
    """
    iterate from 2 to A
    if a number 'x' can be divided completely by a number inside primes array, it is not a prime
    else add 'x' to primes.

    drawback of this soln:
    ---------------------
    - the use of modulo % operation which is costly

    see sieve_of_eratosthenes for a better soln.
    """
    if A < 2:
         return 0
    primes =[]
    count = 0
    for x in range(2, A+1):
        for prime in primes:
                if x%prime == 0:
                   break
        else:
             primes.append(x)
             count+=1
    return count

@log_time
def solve1(A):
    cnt = 0
    # Looping from 1 to A
    for i in range(1,A+1) :
        factors = 0
        # Looping from 1 to i
        for j in range(1,i+1) :
            if i%j==0 :
                factors = factors + 1
        if factors==2 :
            cnt = cnt + 1

    return cnt


# Python program to count all primes smaller than or equal to N using Sieve of Eratosthenes
# advantage: faster than using modulo operation.
def sieve_of_eratosthenes(N):
    """
    1. Assume all numbers from 2 to N are prime
    2. Start from 2 and mark all multiples of 2 as not-prime
    3. After #2, count of numbers that are still marked as prime 
    """
    rbound = N+1
    isPrime = [True]*rbound # idx is a prime if isPrime[idx] == True
    isPrime[0] = isPrime[1] = False # 0 and 1 are not a prime
    i=2
    while i*i <= N: # iterate through all numbers from 2 to sqrt(N)
        if isPrime[i]: # if the number is prime, mark all of its mulitples as not-prime
            for j in range(i * i, rbound, i): # step count is i. iterate from [i*i, N]
                """
                the reason for starting from i*i -> all mulitples of 'i' which are less than i*i, 
                are already a multiple of a number less than i
                multiples of i = i*1, i*2...i*(i-1), i*i....
                they will be marked for numbers less than i.
                """
                isPrime[j] = False
        i+=1
    # count all prime numbers
    count = 0
    for _ in range(rbound):
        if isPrime[_]:
            count += 1 
    return count





# solve(1000)
# solve1(1000)
sieve_of_eratosthenes(1000)