## reduce() function
#In Python Programming, reduce() function is used for applying function cumulatively to elements of an iterable (i.e. list, tuple etc.) from left to right and reduce it to a single value
#Basic syntax: reduce(function, iterable)
#suppose we want to get the sum of the elements of list a = [1, 2, 3, 4, 5]

import functools as ft
a = [1, 2, 3, 4, 5]
def mysum (x, y):
    return x + y
result = ft.reduce(mysum, a) 
print(result) #prints '15'
print()
#This works as (((1 + 2) + 3) + 4) + 5 = 15 


# We can use lambda function in reduce.
b = [1, 11, 2.5, 3, 14]
mul_func = lambda x, y: x * y
mul_result = ft.reduce(mul_func, b)
print(mul_result) #prints '1155.0'
print()


# We can use anonymous lambda function in reduce
c = [5, 10, 15, 20, 25]
sub_result = ft.reduce(lambda x, y: x - y, b)
print(sub_result) #prints '-29.5'
print()


# We can use initializer in reduce
#Basic syntax: reduce(function, iterable, initializer)
d = [10, 20, 30, 40, 50]
h_result = ft.reduce(lambda x, y: x + y, d, 30)
print(h_result) #prints '180'
print()
#This works as ((((30 + 10) + 20) + 30) + 40) + 50 = 180


# We can place iterable directly in reduce
h = ft.reduce(lambda x, y: x + y, [100, 200, 300])
print(h) #prints '600'
print()
