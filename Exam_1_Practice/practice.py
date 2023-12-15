#define the function that creates the lists

def min_max(list):

#set i =1 so the first value isn't accounted for

    i = 1

#create the min and max lists

    max_list = []

    min_list = []

#run this condition for i so the last value isn't checked

    while i < len(list)-1:

#check to see if the element is greater than its neighbors

        if (list[i] > list[i-1]) and (list[i] > list[i+1]):

            max_list.append(i)

#check to see if the element is less than its neighbors

        elif  (list[i] < list[i-1]) and (list[i] < list[i+1]):

            min_list.append(i)

#increments i by 1

        i+=1

#return the values of the list

    return min_list, max_list

min_max([2,4,6,4,3,2,1])
