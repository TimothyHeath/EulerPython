#Find the largest palindrome which is the product of two three-digit numbers
lside=997 #largest possible left half of such a palindrome
is_ans = False #have we found the answer?
while (not is_ans):
    pal = lside*1000 + int(str(lside)[::-1]) #create palindrome from left half
    for i in range(100,int(pal**0.5)+1,1): #check product of two 3-digit nos
        if pal % i == 0 and pal / i < 1000:
            is_ans = True
            i = pal
    lside -= 1 #check smaller left half
print pal
