## filter() function
#In Python programming, filter() function creates and iterator that filters elements from an iterable (i.e., list, tuple etc.)
#Syntax is:- filter(condition return function, iterable)

#suppose there is a list a = [1, 2, 3, 4, 5, 6, 7, 8]
a = [1, 2, 3, 4, 5, 6, 7, 8]

#now we want a list 'b' where we will store even numbers of list 'a'
#using for-loop for that would be lengthy
#that's why we are using filter here

def even_func(x):
    return x % 2 == 0


b = list(filter(even_func, a))
print(b) #prints '[2, 4, 6, 8]'

# in this filter(even_func, a), those elements of list 'a' have been excluded which return False in lambda x: x % 2 == 0
# So this is how 1, 3, 6, 8 have been excluded by filter function


#if we only write filter(even_func, a) then it will print filter object
c = filter(even_func, a)
print(c) #prints '<filter object at 0x%SOMETHING%>'



# We can use lambda function in filter function
d = {1, 2, 3, 4, 5, 6, 7, 8}
not_even = lambda x: x % 2 != 0
e = set(filter(not_even, d))
print(e) #prints '{1, 3, 5, 7}


# We can use anonymous lambda function in filter function
f = (1, 2, 3, 4, 5, 6, 7, 8)
g = tuple(filter(lambda x: x > 5, f)) 
print(g) #prints '(6, 7, 8)'


# We can directly write iterable in filter function
h = tuple(filter(lambda x: x % 5 == 0, (10, 3, 15, 4, 5, 20)))
i = list(filter(lambda x: x % 5 != 0, range(1, 20)))
print(h) #prints '(10, 15, 5, 20)'
print(i) #prints '[1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]'

