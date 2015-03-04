PRODUCT = 600851475143  #Number whose largest prime factor is desired
rem = PRODUCT #remainder after dividing out prime factors
sieve = range(2, int(PRODUCT ** 0.5) + 1, 1) #sieve for possible prime factors
while (len(sieve) > 0): #while there are possible prime factors remaining
    prime = sieve.pop(0) #smallest possible prime factor
    while (rem % prime == 0 and rem != prime): #does prime properly divide it
        rem /= prime #if so factor it out
        if (rem % prime != 0): #reduce seive to possible remainder factors
            i = 0
            while (i < len(sieve) and sieve[i] <= rem ** 0.5):
                i += 1
            sieve = sieve[0:i]
    sieve = [num for num in sieve if num % prime != 0] #sieve out multiples
print rem #print remainder, the largets prime factor of PRODUCT
