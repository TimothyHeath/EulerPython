from math import log
DES_PRIME = 10001 #Nth prime desired (must be at least 6)
#Generate sieve up to Rosser's thm bound
sieve = range(2,int(DES_PRIME*(log(DES_PRIME)+log(log(DES_PRIME)))+1))
for i in range(0,DES_PRIME):#Sieve DES_PRIME times
    prime = sieve.pop(0)
    sieve = [num for num in sieve if num % prime != 0]
print prime