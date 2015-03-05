#Euler Project 175 -Timothy Heath
P = 123456789
Q = 987654321
#Let g(n)=f(n)/f(n-1) inv computes g inverse of P/Q
from fractions import gcd
def cont_frac(p, q):
	#Computes continued fraction of p/q
	d = gcd(p, q)
	return cont_frac_exp([], p / d, q / d)

def cont_frac_exp(expan, p, q):
	#appends continued fraction expansion for p/q to expan	
	if q == 1:
		return expan + [p]
	expan.append(p / q + 1)
	return cont_frac_exp(expan, q, q * (p / q) + q - p)
	
def cfe_to_sbe(cfe):
	#converse continued fraction expansion to shortened binary exp of g inv
	sbe = []
	cfe[0] += 1
	ones = 1 #number of ones encountered in a row
	while(cfe != []):
		term = cfe.pop()
		if term == 2:
			ones += 1
		else:
			#term - 2 zeroes encountered before a 1
			sbe.append(ones)
			sbe.append(term - 2)
			ones = 1
	if ones > 1:
		sbe.append(ones - 1)
	return sbe

def inv(p,q):
	#computes g inverse of p/q in shortened binary expansion
	return cfe_to_sbe(cont_frac(p,q))

print inv(P,Q)
