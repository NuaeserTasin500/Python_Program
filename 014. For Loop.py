## For loop

#same as for(int i=0; i<5; i++)
for i in range(5): 
    print(i)
print()

#same as for(int j=4; j<9; j++)
for j in range(4, 9): 
    print(j)
print()

#same as for(int k=4; k<20; k=k+2)
for k in range(4, 20, 2): 
    print(k)
print()


#printing a string's every letters
name = 'Dalton'
for m in name:
    print(m)
print()

#printing every element of a list
color = ['Red', 'Green', 'Blue']
for x in color:
    print(x)
print()


#for loop with else
for i in range(6):
    print(i)
else:
    print("Sorry no", i) #prints 'sorry no 5' 
print()


# Short form of for loop (used for creating list of consecutive numbers and so on)
list_e = [x for x in range(5)] #using short form of for loop creates 1, 2, 3, 4, 5 into the list
print(list_e) #prints '[1, 2, 3, 4, 5]'
