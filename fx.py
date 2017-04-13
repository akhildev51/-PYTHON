def abs(x):
	if x>1:
		return 1
	elif x==0:
		return 0
	else:
		return -1
n=input('Enter a number: ')
print n*(abs(n))
