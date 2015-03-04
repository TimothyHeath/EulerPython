#Euler Project 12 - Timothy Heath
DIV_BOUND = 500
#Find the first triangular number with more than DIV_BOUND divisors
n = 2 #step to next triangular number
tri = 3 #triangular number being checked; skips 1
divs = 2 #cummulative total of divisors for current no.
while(divs <= DIV_BOUND): #keep searching if this no. doesn't have enough divs 
    n += 1
    tri += n #gen next triangular number
    sieve = range(2,int(tri ** 0.5) + 1) #initialize sieve for prime divs
    rem = tri #product of remaining prime divisors of tri
    divs = 1
    while (sieve != [ ]):
        prime = sieve.pop(0) #take prime off sieve
        ppow = 1 #number of times prime divides rem + 1 
        while rem % prime == 0: #divide out prime power from rem
            ppow += 1
            rem /= prime
            if (rem % prime != 0): #reduce seive to possible remainder factors
                i = 0
                while (i < len(sieve) and sieve[i] <= rem ** 0.5):
                    i += 1
                sieve = sieve[0:i]
        divs *= ppow #update divs to those using prime divs found thus far
        sieve = [num for num in sieve if num % prime != 0] #sieve on prime
    if rem != 1: #at most one remaining prime factor which would double divs
        divs *= 2
print tri #answer when divs > DIV_BOUND
