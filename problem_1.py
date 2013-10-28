#Problem 1: Find the sum of all the multiples of 3 or 5 below 1000.

#Multiples function to return the sum of all the multiples of some number up to but #excluding some limit

def mult(x,lim):
	i=0
	sum=0
	while x*i<lim:
		sum+=x*i
		i+=1
	return sum

#Remove function to capture all of the duplicate values for removal from total sum. For
#example, in this case remove is used to find all of the multiples of 5 which are 
#divisible by 3. The sum of all of these numbers is subtracted from the combined sum of 
#the multiples of 3 and the multiples of 5

def remove(x,mod,lim):
	i=0
	sum=0
	while x*i<lim:
		if x*i%mod==0:
			sum+=x*i
		i+=1
	return sum
	

sum1=mult(3,1000)
sum2=mult(5,1000)
sum3=remove(5,3,1000)
total_sum=sum1+sum2-sum3
print total_sum
#Answer=233168