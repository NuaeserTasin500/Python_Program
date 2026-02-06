## Import A Function of a Library

#We have known that how to import library. 
#For example: We know that if we write 'import math', we can use sqrt() function by writing math.sqrt()
#But we also can import only a function of a library, which means, we can import only sqrt() too
#As a result, we don't need to write math.sqrt() but we can write only sqrt()

from math import sqrt

result = sqrt(9)
print(result) #prints '3.0'
