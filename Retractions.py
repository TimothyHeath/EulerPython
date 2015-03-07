#Euler Project 447 - Timothy Heath
N = 10000
MOD = 1000000007
from numbthy import *
from math import ceil
#Compute the number of retractions in Z/NZ for N <= MAX_N

print eulerphi(15349)

retractions = -1 * N * (N - 1) / 2 #running total of retractions
for d in range (2, N + 1): #possible gcds of n and a
	retractions = retractions + int(ceil(float((N / d) * eulerphi(d)) / d)) * d
print retractions