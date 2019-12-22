a=input("enter the first array:")
b=input("enter the second array:")
c=input("enter the third array:")
for i in range(len(a)):			#loop for appending the elements of first to second array 
	b.append(a[i])
print("combined array of a and b:",b)
for j in range(len(b)):			#loop for appending the third array elements which are divided by 2 
	if(c[j]%2==0):
		b.append(c[j])
print("total combined array of a,b and c:",b)
