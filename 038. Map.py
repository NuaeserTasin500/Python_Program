## map() function
#In python programming, map() function applies a given function to every elements of an iterable (i.e. list, tuple, etc.) and returns a map object.
#Syntax is:- map(function, iterable)

#Suppose we have a list a = [1, 2, 3, 4, 5]
a = [1, 2, 3, 4, 5]

#we want to square the elements of list 'a', so that it becomes [1, 4, 9, 16, 25] and store it in a new list 'b'
#basically it will be lengthy by using for-loop for that
#so we will use map() function here
def square(x):
    return x ** 2
b = list(map(square, a)) 
print(b) #prints '[1, 4, 9, 16, 25]'

#if we only write map(square, a), it will only return map object,
c = map(square, a)
print(c) #prints '<map object at 0x%SOMETHING%>'


# Using lambda function in map()
func_a = lambda x: x / 10
list_a = [10, 20, 30, 40, 50]
list_b = list(map(func_a, list_a)) 
print(list_b) #prints '[1.0, 2.0, 3.0, 4.0, 5.0]'


# Using anonymous lambda function in map()
tuple_a = (100, 200, 300, 400, 500)
tuple_b = tuple(map(lambda x: x/100, tuple_a))
print(tuple_b) #prints '(1.0, 2.0, 3.0, 4.0, 5.0)'


# We can directly place iterable in map
list_c = list(map(lambda x: x * 5, [1, 2, 3, 4, 5]))
tuple_c = tuple(map(lambda x: x * 4, (2, 5, 9, 14)))
print(list_c) #prints '[5, 10, 15, 20, 25]'
print(tuple_c) #prints '(8, 20, 36, 56)'


# Other iterables (set, range)
range_a = list(map(lambda x: x * 3, range(1, 10))) 
set_a = set(map(lambda x: x - 9, {99, 94, 87, 90}))
print(range_a) #prints '[3, 6, 9, 12, 15, 18, 21, 24, 27]'
print(set_a) #prints '{81, 90, 85, 78}'

