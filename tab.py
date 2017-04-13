a=input('Enter the years :')
b=input('Enter the balance :')
x=input('Enter the rate :')
c=(a*b)/100
d=b+c
print '%4s'%('YEAR'),'%-13s'%('STRT_BALANCE'),'%-8s'%('INTEREST'),'%-14s'%('END BALANCE')

for i in range(1,a+1,1):
	print '%4d'%(i),'%-13d'%(b),'%-8d'%(c),'%-14d'%(d)
	b=d
	a=a+1
	c=(a*b)/100
	d=b+c

	
