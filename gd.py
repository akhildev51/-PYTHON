n=float(input("Enter the TIME(24 hour format): "))
if n<12.0:
	print 'GOOD MORNING'
elif n>19.0:
	print 'GOOD NIGHT'
else:
	print 'GOOD EVENING'
