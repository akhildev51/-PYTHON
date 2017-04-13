def fac(o):
	f=1
	for i in range(1,o+1):
		f=f*i
	return f

a=float(input ('enter a number '))
b=float(input ('enter a limit '))
sum=1.0+a
if(b>2.0):
	i=2
	while(i<=b):
		sum=sum+((a**i)/(fac(i)))
		i=i+1
print sum
		
