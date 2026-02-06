## Giving short name of a library

#We have known that how to import library. 
#For example: We know that if we write 'import math', we can use sqrt() function by writing math.sqrt()
#But we can give short name of a library using as.
#For example: import math as mt
#As a result, we don't need to write math.sqrt() but we can write mt.sqrt()

import math as mt

result = mt.sqrt(9)
print(result) #prints '3.0'
