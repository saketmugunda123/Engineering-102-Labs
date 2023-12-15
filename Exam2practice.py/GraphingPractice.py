import matplotlib.pyplot as plt
import numpy as np

f1 =2
f2 = 6
x = np.linspace(-2,2,20)
y = (1/4*f1)*(x**2)
y2 = (1/4*f2)*(x**2)
plt.plot(x,y,'r^-',markerfacecolor='b',markeredgecolor='b',linewidth=2,label = 'f1')#line connecting red triangles
plt.plot(x,y2,'bo',linewidth=6,label='f2')
plt.legend()
#plt.ylabel('y')
#plt.xlabel = ('x')
plt.title("Parabolic plots with varying focal length")
plt.show()


x = np.linspace(-4,4,25) #x always has to come first
y = 2*(x**3) + 3*(x**2) - 11*x - 6
plt.plot(x,y,'y*')
#plt.xlabel('x values')
#plt.ylabel('y values')
plt.title('Plot of cubic polynomial')
plt.show()

x = np.linspace(-2*(np.pi),2*(np.pi),30)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure()

plt.subplot(2,1,1)
plt.plot(x,y1,'r',label='sin(x)')
plt.ylabel('sin(x)')
plt.legend

plt.subplot(2,1,2)
plt.plot(x,y2,'b',label='cos(x)')
plt.ylabel('cos(x)')
plt.xlabel('x')
plt.legend()
plt.suptitle('Plot of cosx and sinx')
plt.show()


