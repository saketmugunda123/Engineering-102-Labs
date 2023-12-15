import matplotlib.pyplot as plt
import numpy as np

#plots numbers 1,2,3,4 against each other
plt.plot([1,2,3,4])
plt.ylabel('some numbers') #labels y axis
plt.show()#shows plot

plt.plot([1,2,3,4],[1,4,9,16]) #plots x against y (first list x second y)
plt.plot([1,2,3,4],[1,4,9,16],'ro')#creates red circles
plt.axis((0,6,0,20)) #first two numbers are x bounds, second two are y bounds

# evenly sampled time at 200ms intervals (normally use linspace)
t = np.arange(0., 5., 0.2)

# red dashes (r--), blue squares (bs) and green triangles (g^)
#syntax is x,y,format and it keeps going
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()#This plots on the same graph

#plotting categorical data
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
#sets figure size
plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values) #*
plt.subplot(132)
plt.scatter(names, values) #*
plt.subplot(133)
plt.plot(names, values) #*
plt.suptitle('Categorical Plotting') #overarching title


#Keyword arguments
x = [1,3]
y= [2,4]
plt.plot(x, y, label="My Line") #label used for legend
plt.plot(x, y, color="red") #color of line
plt.plot(x, y, linestyle="--") #style of line
plt.plot(x, y, linewidth=2) #width of line
plt.plot(x, y, marker="o") #style for data points
plt.plot(x, y, marker="o", markerfacecolor="blue")
plt.plot(x, y, marker="o", markeredgecolor="black")


#subplots
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)


plt.subplot(2,1,1) #(number of row, number of col,plot number)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')#'k'shows black line

plt.subplot(2,1,2) #(number of row, number of col,plot number)
plt.plot(t2, np.cos(2*np.pi*t2),'k')
plt.show() #prints 2 subplots with same y axis and separate x axis