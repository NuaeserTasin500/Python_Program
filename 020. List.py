## List

list1 = [3, 5, 6] #this is list1
print(list1)
print(type(list1))
print(len(list1)) #length of list1, which is 3
print()

#printing individual elements of list by index
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[-1]) #here list1[-1] = list1[len(list1)-1] = list1[3-1] = list[2]
print() 

#we can change elements of list by indexing
list1[0] = 8
print(list1)
print() 


# List can contain different datatype values
list2 = [3, 3.5, "Hello", True]
print(list2)
print()

# element manipulation
if "Hello" in list2:
    print("Yes") #obviously prints "Yes" because "Hello" is in list2
else:
    print("No")
print()

#using for loop for printing all elements of list
department = ['CSE', 'EEE', 'ME', 'BBA']
for x in department:
    print(x) 
print()

#indexing
print(department[:]) #prints whole list with all elements
print(department[:3]) #prints ['CSE', 'EEE', 'ME'] 
print(department[::2]) #prints ['CSE', 'ME'], here 2 is jump index like i = i+2in
print()

#adding/removing elements in list
list3 = [1, 2, 3, 4]
print("list3 is = ", list3)
list3.append(5)
print("after adding 5, now list3 is = ", list3)
list3.remove(5)
print("after removing 5, now list3 is = ", list3)
print()

#sorting elements in list (ascending order)
list4 = [11, 100, 5, 45, 33, 50]
print("Before sorting list: ", list4)
list4.sort()
print("After sorting list: ", list4)
print()

#sorting elements in list (descending order)
list4 = [11, 100, 5, 45, 33, 50]
print("Before sorting list: ", list4)
list4.sort(reverse=True)
print("After sorting list: ", list4)
print()

#mirror elements in list
list4 = [11, 100, 5, 45, 33, 50] 
print("list4 = ", list4) 
list4.reverse()
print("mirror of list4 = ", list4)
print()

#getting index of any elements
list5 = [3, 4, 5, 6]
print(list5)
print("The index of 3 is", list5.index(3))
print("The index of 4 is", list5.index(4))
print("The index of 5 is", list5.index(5))
print("The index of 6 is", list5.index(6))
print()

#count elements
list5 = [4, 5, 6, 4, 7, 5, 4, 0, 6, 5, 4]
print(list5)
print("In this list, 4 occurs", list5.count(4), "times")
print("In this list, 5 occurs", list5.count(5), "times")
print("In this list, 6 occurs", list5.count(6), "times")
print("In this list, 7 occurs", list5.count(7), "times")
print()

#keeping list into another variable
m = list5
print(m)
print()

# adding elements by insert method
m.insert(1, 899) #insert(index, element)
print(m) #index 1 has 899
print()

# merging two lists
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = list_a + list_b
print(list_c)
print()

# Creating Naive Method List by multiply 
n = 5
odlist = [0]*n
print(odlist) #prints '[0, 0, 0, 0, 0]'
odlist[0] = 1
print(odlist) #prints '[1, 0, 0, 0, 0]'
print()


# Creating Naive Method List by for-loop statement
odlist1 = [0 for _ in range(n)]
print(odlist1) #prints '[0, 0, 0, 0, 0]'
odlist1[0] = 1
print(odlist1) #prints '[1, 0, 0, 0, 0]'
print()


# Sum all elements of a list by sum() function
list_d = [1, 2, 3, 4, 5]
sumlist = sum(list_d)
print(sumlist) #prints '15'
print()
