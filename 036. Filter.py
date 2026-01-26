## filter() function
#In Python programming, filter() function creates and iterator that filters elements from an iterable (i.e., list, tuple etc.)
#Syntax is:- filter(function, iterable)

#suppose there is a list a = [1, 2, 3, 4, 5, 6, 7, 8]
a = [1, 2, 3, 4, 5, 6, 7, 8]

#now we want a list 'b' where we will store even numbers of list 'a'
#using for-loop for that would be lengthy
#that's why we are using filter here

b = list(filter(lambda x: x % 2 == 0, a))
print(b) #prints '[2, 4, 6, 8]'

# in this filter(lambda x: x % 2 == 0, a), those elements of list 'a' were excluded which returns false in lambda x: x % 2 == 0
# So this is how 1, 3, 6, 8 were excluded by filter function


#if we only write filter(lambda x: x % 2 == 0, a) then it will print filter object
c = filter(lambda x: x % 2 == 0, a)
print(c) #prints '<filter object at 0x%SOMETHING%>'

