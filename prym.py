x= int(input("Enter upper range: "))

print "Prime numbers between 1and",x,"are:"

for j in range(1,x+1):
   if j > 1:
       for i in range(2,j):
           if (j % i) == 0:
               break
       else:
           print(j)
