## Arithmetic operation precedence
# precedence 1: ()
# precedence 2: **
# precedence 3: +x, -x (unary plus, unary minus)
#precedence 4: *, /, //, %
#precedence 5: +, -


a = 10
b = 2
c = 3

d = a + b * c 
print(d) #result is 16 because "*" precedence is 4 and "+" is 5. 
#Low number precedence works first. 

e = (a + b) * c
print(e) #result is 36 because "()" precedence is 1 and "*" is 4.
#Low number precedence works first. 
