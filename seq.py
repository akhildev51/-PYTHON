def seq(n):
	while(n<22):
		print n,','
		if (n%2==0):
			n=(n/2)
			return n,','
		else:
			n=(n*3)+1
			return n,','
		print n,','
seq(3)
