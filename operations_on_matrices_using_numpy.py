import numpy as np	#importing numpy as np
a=np.array(input("enter the first matrix a:"))		      #taking matrix a from the user
b=np.array(input("enter the second matrix b:"))		      #taking matrix b from the user
print ("The first matrix a:",a)		                      #printing first matrix a 
print ("The second matrix b:",b)	                    	#printing second matrix b
print ("The addition of matrices a,b:",np.add(a,b))	    #addition of matrices a,b
print ("The subtration of matrices a,b:",np.subtract(a,b))	#subtraction of matrices a,b
print ("The multiplication of matrices a,b:",np.multiply(a,b))	#multiplication of matrices a,b
print ("The division of matrices a,b:",np.divide(a,b))	#divide of matrices a,b
print ("The dot product of matrices a,b:",np.dot(a,b)) 	#dot product of a,b
print ("The square of the matrix a:",np.square(a))	    #squaring the matrix a
print ("The square root of the matrix a:",np.sqrt(a))  	#square root of a
print ("The sum of all the elements in the matrix a:",np.sum(a))	#summing of all the elements in matrix a
print ("The transpose of the matrix a:",a.T)		                  #the transpose of the matrix a
print ("The determinanat of the matrix:",np.linalg.det(a))		    #determinant of a
print ("The inverse of the matrix a:",np.linalg.inv(a))		        #inverse of the matrix a
print ("The eigen values of matrix a:",np.linalg.eig(a)[0])		    #eigen values of the matrix a
print ("The eigen vectors of the matrix a:",np.linalg.eig(a)[1])	#eigen values of the matrix a
print ("The rank of the matrix a:",np.rank(a))
print ("The minimum value of the matrix a:",np.min(a))		#the minimum value  of matrix a	
print ("The maximum value of the matrix a:",np.max(a))		#the maximum value  of matrix a	
print ("The median of matrix a:",np.median(a))		#medaian of the matrix a
print ("The zero matrix:",np.zeros((3,3)))	      #printing the zero matrix
print ("The ones matrix:",np.ones((3,3)))		      #printing the ones matrix
print ("The identity matrix:",np.eye(3))	        #printing the identity matrix	
print ("The random valued matrix:",np.random.random((3,3)))		#random valued matrix
