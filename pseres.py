def fac(o):
	f=1
	for i in range (1,o+1):
		f=f*i
	return f
x=float(input('Enter a number: '))
y=float(input('Enter a limit: '))
i=0
while(i<=y):
	print((x**i)/(fac(i)))
	i+=1

