## map() function
#In python programming, map() function applies a given function to every elements of an iterable (i.e. list, tuple, etc.) and returns a map object.

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
print(list_b) #prints '[1, 2, 3, 4, 5]'


# Using anonymous lambda function in map()
tuple_a = (100, 200, 300, 400, 500)
tuple_b = tuple(map(lambda x: x/100, tuple_a))
print(tuple_b) #prints '(1, 2, 3, 4, 5)'

