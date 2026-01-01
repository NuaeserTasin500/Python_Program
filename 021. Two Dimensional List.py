## Two dimensional list

phone = ["iPhone", "Realme", "Samsung", "Vivo"]
laptop = ["Acer", "Asus", "Vaio", "HP"]
pendrive = ["SanDisk", "Kingston", "Transcend"]

electronic_brands = [phone, laptop, pendrive] #this is two dimensional list

#in two-dimensional lists - phone, laptop, pendrive are considered inner-lists of electronic_brands list
#inner-lists are considered as rows. So phone is row 0; laptop is row 1; pendrive is row 2.

print(electronic_brands) #prints '[['iPhone', 'Realme', 'Samsung', 'Vivo'], ['Acer', 'Asus', 'Vaio', 'HP'], ['SanDisk', 'Kingston', 'Transcend']]'
print()



# Indexing of two dimensional list
#in two dimensional list, [rows_index][column_index]
#more precisely, [innerList_index][innerList_element_index]

print(electronic_brands[0]) #prints '['iPhone', 'Realme', 'Samsung', 'Vivo']'
print(electronic_brands[1]) #prints '['Acer', 'Asus', 'Vaio', 'HP']'
print(electronic_brands[2]) #prints '['SanDisk', 'Kingston', 'Transcend']'
print(electronic_brands[0][2]) #prints 'Samsung'
print(electronic_brands[0][1]) #prints 'Realme'
print(electronic_brands[1][2]) #prints 'Vaio'
print(electronic_brands[2][0]) #prints 'Sandisk'
print()


# Another way we can declare two dimension array
electronic_brands = [["iPhone", "Realme", "Samsung", "Vivo"], 
                     ["Acer", "Asus", "Vaio", "HP"], 
                     ["SanDisk", "Kingston", "Transcend"]]


# Using For loop for printing inner-lists
for x in electronic_brands:
    print(x)
print() 


# Using Nested For loop for printing all individual elements of inner-lists
for category in electronic_brands:
    for brands in category:
        print(brands, end=", ")
    print()

print()


# Creating Naive Method Two Dimensional List by multiply 
rows = cols = 5
tdlist = [[0]*cols]*rows
print(tdlist) #prints '[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]'
tdlist[0][0] = 1
print(tdlist) #prints '[[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]'
print()



# Creating Naive Method Two Dimensional List by for-loop statement
tdlist1 = [[0 for _ in range(cols)] for _ in range(rows)]
print(tdlist1) #prints '[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]'
tdlist1[0][0] = 1
print(tdlist1) #prints '[[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]'
print()
