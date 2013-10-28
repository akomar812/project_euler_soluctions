#Find the difference between the sum of the squares of the first one hundred #natural numbers and the square of the sum.
#Based on sum of natural numbers formula, squared
def sqr_of_sum(n):
	return (((n)*(n+1))/2)*(((n)*(n+1))/2)
#rolling sum of squares of natural numbers as they are computed
def sum_of_sqr(lim):
	i=0
	sum=0
	while(i<=lim):
		sum+=i*i
		i+=1
	return sum
	
x=sqr_of_sum(100)
y=sum_of_sqr(100)

print x-y
#Answer= 25164150