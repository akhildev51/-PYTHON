n=input('Enter a number')
def fac(n):
	if(n==1):
		return 1
	else:
		f=n*fac(n-1)
		return f
s=fac(n)
print s
