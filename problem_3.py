#What is the largest prime factor of the number 600851475143

#Function returns prime if it is a factor, 0 if it isn’t, and 1 if the number trying to be #factored is 1
def factor(n,p):
	if n==1:
		return 1
	if n%p==0:
		return p
	else:
		return 0
x=600851475143
f=3
fact=0
max_fact=0
while fact!=1:
	fact=factor(x,f)
	if fact>max_fact:
		max_fact=fact
	if fact==0:
		f+=1
	else:
		x=x/fact
print max_fact
#Answer=6857
	
	

