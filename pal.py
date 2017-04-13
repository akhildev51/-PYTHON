s=raw_input("Enter A String: ")
n=len(s)
i=0
j=n-1
while(i<(n/2)):
	if(s[i]!=s[j]):
		break
	i=i+1
	j=j-1
if(i==(n/2)):
	print 'given string is PALINDROME'
else:
	print 'given string is NOT-PALINDROME'
