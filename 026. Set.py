## Set
# set is a non-repeated collection system
# printing set sometimes don't follow orders.


list1 = ['a', 'b', 'c', 'a']
set1 = {'a', 'b', 'c', 'a'} 
print(list1) #prints '['a', 'b', 'c', 'a']'
print(set1) #prints '{'a', 'b', 'c'}' 
print(type(set1))
print()

# Empty set
empty_dict = {} #this is empty dictionary
empty_set = set() #this is empty set
print(empty_dict)
print(empty_set)
print(type(empty_dict))
print(type(empty_set))
print()

# Union in set
s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8, 4}
s3 = s1.union(s2)
print(s3) #prints '{1, 2, 3, 4, 5, 6, 7, 8}'
s1.update(s2) #s1 = s1.union(s2)
print(s1) #prints '{1, 2, 3, 4, 5, 6, 7, 8}'
print()


# Intersection in set and Disjoint issue check
s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8, 4}
s3 = {5, 6, 7, 8}
s4 = s1.intersection(s2)
s5 = s1.intersection(s3)
bool1 = s1.isdisjoint(s2)
bool2 = s1.isdisjoint(s3)
print(s4) #prints '{4}'
print(s5) #prints 'set()' (empty set)
print(bool1) #prints 'False'
print(bool2) #prints 'True'
print()



# Difference in set
s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 6, 9}
s3 = s1.difference(s2)
s4 = s2.difference(s1)
print(s3)
print(s4)
print()


#subset and superset
cities = {'Madrid', 'Paris', 'Dhaka', 'Islamabaad'}
eu_cities = {'Paris', 'Madrid'}
bool3 = cities.issuperset(eu_cities) #True
bool4 = cities.issubset(eu_cities) #False
bool5 = eu_cities.issubset(cities) #True
print(bool3) #prints 'True'
print(bool4) #prints 'False'
print(bool5) #prints 'True'
print()


# Remove/Discard
cities.discard('Paris')
print(cities) #prints '{'Madrid', 'Dhaka', 'Islamabaad'}'
cities.remove('Madrid')
print(cities) #prints '{'Dhaka', 'Islamabaad'}'

#The difference between remove and discard is, if we try to delete an item which is absent in set, then remove() shows error, but discard() never shows error
print()



# Pop method 
# pop removes last element of set. But we don't know which item will be last since set doesn't follow orders
cities = {'Madrid', 'Paris', 'Dhaka', 'Islamabaad'}
poped_item = cities.pop()
print(cities)
print(f'{poped_item} has been poped')
print()


# Clear and Delete
#clear deletes all elements of set.
#del deletes entire set
cities.clear()
print(cities) #prints 'set()'
del cities #delete entire set and it won't be printed

