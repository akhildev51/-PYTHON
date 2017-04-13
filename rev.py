def rev(s):
	n=len(s)
	for i in range(1,n+1):
		print s[n-i]
x=raw_input('Enter a string to reverse: ')
rev(x)
