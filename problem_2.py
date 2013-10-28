#Problem 2: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of #the even-valued terms.

#All work done in fibonacci function. Simply checks if fibonacci number is even, if it is it is added to a rolling sum
def fibonacci(lim):
	fnm2=0
	fnm1=1
	fn=fnm2+fnm1
	sum=0
	while fn<lim:
		fn=fnm2+fnm1
		fnm2=fnm1
		fnm1=fn
		if fn%2==0:
			sum+=fn
	return sum

print fibonacci(4000000)
#Answer=4613732
	
	

	