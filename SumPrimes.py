#Euler Project 10 - Timothy Heath
PRIME_BOUND = 2000000 #Sum all primes below PRIME_BOUND
sieve_bound = PRIME_BOUND ** 0.5 #No primes need sieve above this point
prime = 2
psum = 0 #Our running sum of primes
sieve = range(3,PRIME_BOUND) #Initialize sieve
while(prime <= sieve_bound): #Sieve of Eratosthenes
    psum += prime 
    sieve = [num for num in sieve if num % prime !=0]
    prime = sieve.pop(0)
print psum + prime + sum(sieve) #All primes sieved on + all primes left
