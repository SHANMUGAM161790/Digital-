import numpy as np	#importing the numpy as np
a=np.array(input("enter the first matrix a:"))
b=np.array(input("enter the second matrix b:"))
c=np.array(a,dtype=np.int64)
d=np.array(b,dtype=np.int64)
print("the first matrix :",a)
print("the second matrix :",b)
print("additon",np.subtract((c,d)))
