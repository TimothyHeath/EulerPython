#Euler Project 495 - Timothy Heath
def W(ppows,k):
	if k == 1:
		print ppows, k, 1
		return 1
	total = 0
	for dup in range(1,k):
		duptotal = 0
		for dpows in divs(ppows,dup):
			duptotal += W(dpows,)
		if dup % 2 == 0:
			duptotal *= -1
		total += duptotal
	print ppows, k, total/k
	return total/k
	
print W([2,2],2)
