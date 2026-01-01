## If-else condition

a = int(input("Enter your age: "))
print("Your age is ", a)

if(a > 18):
    print("You can vote")
elif(a == 18):
    print("You can vote")
else:
    print("You can not vote")



# Nested if-else
if(a >= 18):
    if(a < 47):
        print("Young adult person")
    else:
        print("Old person")
else:
    if(a > 5):
        print("non-infant child")
    else:
        print("infant child")
print()

# If else in short hand
a, b = 100, 200
print(a) if a > b else print(b) #prints '200'

#here print(a) if a > b else print(b) means:-
#   if(a > b):
#       print(a)
#   else:
#       print(b)
print()

# Elif in shorthand If else
g, h = 100, 100
print("greater than") if g > h else print("equal") if g == h else print("less than") #prints 'equal'

#here print("greater than") if g > h else print("equal") if g == h else print("less than") means:-
#   if(g > h):
#       print("greater than")
#   elif(g == h):
#       print("equal")
#   else:
#       print("less than")
print()

