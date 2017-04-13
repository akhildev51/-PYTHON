def gre(a,b):
	gcd=1
	for i in range(2,(b+1),1):
		if(a%i==0 and b%i==0):
			gcd=i
	return gcd
x=input('Enter a number: ')
y=input('Enter a number: ')
if(x>y):
	print (gre(x,y))
else:
	print (gre(y,x))
