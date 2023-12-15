# import numpy as np
# x = np.linspace(1.0, 10.0, 10)
# y = x ** 2 - 1
# with open('zfile.txt', 'w') as zfile:
#     zfile.write('x\ty\n')
#     for i in range(len(x)):
#         mystr = str(x[i]) + '\t' + str(y[i])
#         zfile.write(mystr + '\n')
# with open('zfile.txt') as myfile:
#     all_of_it = myfile.read().split('\t')
# print(all_of_it)
# output = ','.join(all_of_it) #joins together the list into a big string where each element is separated by a comma
# print(output)

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-2, 2, 25)
# y1 = x
# y2 = x ** 2
# plt.plot(x, y1, 'g', linewidth = 3)
# plt.plot(x, y2, 'k', marker = 'o', markerfacecolor = 'b')
# plt.axis([-2, 2, -2, 4])
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Plots for 2 polynomials')
# plt.legend(['straight', 'curved'], loc = 'upper center')
# plt.show()

#Try and except
# while True:
#     try:
#         num = int(input('Give me an integer '))
#         if num < 1:
#             print('Try again')
#         else:
#             break
#     except ValueError:
#         print('Bad input try again')
#         continue

# import numpy as np
# list = [['1','2','3'],['5','3','7'],['6','4','6']]
# newList = []
# for slist in list:
#     temp = [float(num) for num in slist]
#     newList.append(temp)

# newList = np.array(newList)
# sum = np.sum(newList[:,1])
# print(sum)

c = 50

def outer():
    c = 55

    def inner():
        global c
        c = 60

    inner()
    print(c)

outer()
print(c)  # What will happen when this line is executed?
