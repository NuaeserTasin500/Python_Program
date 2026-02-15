## Built-in Methods (Part-2)
#Note: This topic is made by the help of AI and help(list) documentation
#<AI>



# .clear()
#clears the list
list1 = [1, 2, 3, 4, 5]
list1.clear()
print() #prints ' '
print()



# .copy()
#returns a shallow copy of the list
a = [2, 3, 7, 8]
b = a.copy()
print(b) #prints '[2, 3, 7, 8]'
print()



# .extend()
#Extend list by appending elements from the iterable.
num = [1, 2, 3]
num.extend([4, 5])
print(num) #prints '[1, 2, 3, 4, 5]'



# .insert()
#Insert an element before index.
#Syntax: .insert(index, element)
num.insert(1, 99)
print(num) #prints '[1, 99, 2, 3, 4, 5]'



# .pop()
#remove last element
num.pop()
print(num) #prints '[1, 99, 2, 3, 4]'



# .remove()
#remove first occurence of value
num.remove(99)
print(num) #prints '[1, 2, 3, 4]'



# .reverse()
num.reverse()
print(num) #prints '[4, 3, 2, 1]
print()



# .sort()
xd = [1, 6, 3, 7, 0, 2]
xd.sort()
print(xd) #prints '[0, 1, 2, 3, 6, 7]'
xd.sort(reverse=True)
print(xd) #prints '[7, 6, 3, 2, 1, 0]'
print()



# ================================================================= #
#Note: This topic is made by the help of AI and help(dict) documentation
#<AI>



# .get()
#Returns the value for key if it exists, otherwise returns default
dict1 = {'Name':'Jill', 'Age':30, 'Occupation':'Doctor'}
print(dict1.get('Name')) #prints 'Jill'
print(dict1.get('Address')) #prints 'None'
print(dict1.get('Address', '11 Street Road')) #prints '11 Street Road'



# .items()  
#Returns a view object of (key, value) pairs.
print(list(dict1.items())) #prints '[('Name', 'Jill'), ('Age', 30), ('Occupation', 'Doctor')]'

# .keys()  
#Returns a view object of all keys.
print(list(dict1.keys())) #prints '['Name', 'Age', 'Occupation']'



# .pop(key, default)  
#Removes the key and returns its value. If not found, returns default (if given) or raises 
dict1.pop("Occupation")
print(dict1) #prints '{'Name':'Jill', 'Age':30}'
print()



# .popitem()  
#Removes and returns the last inserted (key, value) pair. Raises KeyError if empty.
dict2 = {"x": 10, "y": 20}
print(dict2.popitem()) #prints '('y', 20)'
print(dict2) #prints '{'x': 10}'
print()



# .setdefault(key, default=None)  
#If key exists, returns its value. Otherwise, inserts key with default and returns default.
dict3 = {}
dict3.setdefault("z", 99)
print(dict3) #prints '{'z': 99}'
print()



# .update()  
#Updates dictionary with another mapping or iterable of pairs.
dict4 = {"a": 1}
dict4.update({"b": 2, "c": 3})
print(dict4) #prints '{'a': 1, 'b': 2, 'c': 3}
dict4.update(d=4, e=3)
print(dict4) #prints '{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 3}'
print()



# .values()  
#Returns a view object of all values.
dict5 = {'Name':'Gomez', 'Age':32}
print(list(dict5.values()))  #prints '[Gomez, 32]'
print()



# ================================================================= #
#Note: This topic is made by the help of AI and help(set) documentation
#<AI>



# .add(), .discard(), .remove(), .update()
#.add(): Adds an element to the set. No effect if already present.
#.discard(): Removes an element if present; does nothing if absent (no error).
#.remove(): Removes an element if present; raise error if absent.
#.update(): Updates the set in place, adding elements from others.
set1 = {1, 2, 3}
set1.add(4)
print(set1) #prints '{1, 2, 3, 4}'
set1.discard(2)
print(set1) #prints '{1, 3, 4}'
set1.remove(4)
print(set1) #prints '{1, 3}
set1.update({8, 9})
print(set1) #prints '{1, 3, 8, 9}'
print()



# .clear(), .copy()
#.clear(): Removes all elements from the set.
#.copy(): Returns a shallow copy of the set.
set6 = {1, 2, 3, 4, 5}
set6.clear()
print(set6) #prints 'set()' as empty set
set7 = {1, 2, 3, 4, 5}
set8 = set7.copy()
print(set8) #prints '{1, 2, 3, 4, 5}'
print()



# .difference(), .intersection(), .union(), .symmetric_difference()
#if a and b are two sets....
#.difference(): Returns (a - b)
#.intersection(): Returns (a ∩ b)
#.union(): Returns (a U b)
#.symmetric_difference(): Returns ((a - b) U (b - a))
a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
print(a.difference(b)) #prints '{1, 2, 3}' 
print(a.intersection(b)) #prints '{4}'
print(a.union(b)) #prints '{1, 2, 3, 4, 5, 6, 7}'
print(a.symmetric_difference(b)) #prints '{1, 2, 3, 5, 6, 7}'
print()



# .difference_update(), .intersection_update(), .symmetric_difference_update()
#if a1 and b1 are sets....
#.difference_update(): Assigns a1 as (a1 - b1)
#.intersection_update(): Assigns a1 as (a1 ∩ b1)
#.symmetric_difference_update(): Assigns a1 as ((a1 - b1) U (b1 - a1))
a1 = {1, 2, 3, 4}
b1 = {3, 4, 5, 6}
a1.difference_update(b1)
print(a1) #prints '{1, 2}'
a1 = {1, 2, 3, 4} #keeping a1 set elements as {1, 2, 3, 4} again
a1.intersection_update(b1)
print(a1) #prints '{3, 4}'
a1 = {1, 2, 3, 4} #keeping a1 set elements as {1, 2, 3, 4} again
a1.symmetric_difference_update(b1)
print(a1) #prints '{1, 2, 5, 6}'
print()



# .isdisjoint(), .issubset(), .issuperset()
#.isdisjoint(): Returns True if two sets have no elements in common.
#.issubset(): Returns True if this set is contained in another.
#.issuperset(): Returns True if this set contains another.
a3 = {1, 2, 3, 4, 5, 6}
b3 = {1, 2, 3}
c3 = {100, 200, 300}
print(a3.isdisjoint(c3)) #prints 'True' because a3.intersection(b3) = set() = {Ø}
print(b3.issubset(a3)) #prints 'True' because b3 ⊂ a3
print(a3.issuperset(b3)) #prints 'True' because a3 ⊃ b3
print()



