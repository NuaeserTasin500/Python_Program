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


