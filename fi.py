x=input ('enter a number : ')
def fib(x):
	if x<=1:
		return 1
	else:
		f=fib(x-1)+fib(x-2)
		return f
for i in range(x):
	print fib(i)
