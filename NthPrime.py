#Euler Project 7 - Timothy Heath
from math import log
DES_PRIME = 10001 #Nth prime desired (must be at least 6)
#Initialize sieve up to Rosser's thm bound
sieve_max = int(DES_PRIME*(log(DES_PRIME)+log(log(DES_PRIME))))+1
sieve = range(2,sieve_max)
for i in range(0,DES_PRIME):#Sieve DES_PRIME times
    prime = sieve.pop(0)
    if prime <= sieve_max ** 0.5:
        sieve = [num for num in sieve if num % prime != 0]
print prime