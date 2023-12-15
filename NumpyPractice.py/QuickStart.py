#Creating a numpy array
import numpy as np
a = [1,2,3,4,5]
a = np.array(a)

#Arange creates a numpy array from 0-x (exclusive) 
a = np.arange(15)
#reshape turns it into a shape of 3x5
a = a.reshape(3,5)


a.dtype #Gives the data type of the array (int32 in this case)

type (a) #gives type (numpy.ndarray) of object

#Array creation is used with either a tuple or list
#Dont forget extra set of parenthesis to transform it form an argument
a = np.array((1,2,3,4))
a = np.array ([1,2,3,5])

#Prints a 3x4 of zeros also works for ones (make sure you don't forget extra parenthesis)
np.zeros((3,4))
np.ones((3,4)) 
#values are random bc it finds random values from memory location
np.empty((2,3))

#arange is ass with floats bc it can create infintely long numbers
#use linspace (start,stop,#of values you want)
x = np.linspace(0,2,9) #Gives 9 numbers from 0 to 2
f = np.sin(x) #takes the sin of each value in the linspace
#DONT USE EXTRA PARENTHESIS because those values are each arguments

b = np.arange(12).reshape(4,3)
#if array too large, it just prints corners

#any arthemetic changes across every element in the list
b = np.arange(7)
b = b**2
b = 10 * np.sin(b) #use np for sin bc its a function apart of np module

A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])

c = A - B #can add and subtract matricies with same dimensions


#Matrix mult works if (m x n) by (n x p) m and p can be equal
Product = A*B


# += and *= modify existing array rather than creating new one

#other notable functions
a.sum()
a.min()
a.max()

#How to get functions of each row or column
b = np.arange(12).reshape(3,4)
b = b.sum(axis=0) #sum of each column (vertical axis represented by axis=0)
# b = b.max(axis=1) #min of each row
# b.cumsum(axis=1) #culmulative sum along each row

#Universial functions (exp,sqrt,sin,cos,etc) use np.function notation
b = np.arange(3)
np.sin(b)
print(b)

#list indexing notation (row:column:)
a= np.arange(25).reshape(5,5)
b = a[0:3,3] #gives 1st 3 values in 3rd column

#reshpaing
a = np.arange(20).reshape(5,4)
m,n = a.shape
print(m,n)
