## ID function <AI>
#In python programming, ID function returns the unique identifier (memory address) of an object
#In python, everything is object

a = 5
a_id = id(a)
print(a_id) #prints 'a' variable's memory address

b = 5
b_id = id(b)
print(b_id) #prints same memory address of 'a' because both a and b has same value

c = 6
c_id = id(c)
print(c_id) #prints different memory address of a and b because value is different than a and b

#  In Python, id() returns the memory address of an object for that specific execution. If you run the same code again, the memory address may differ due to operating system security measures and dynamic memory allocation. 
# That's why, if you run this code again, the memory address will show different.
# In CMD or Powershell, running same code won't show different.

