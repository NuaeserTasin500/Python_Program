## Break and Continue in loop

# Break statement 
for i in range(0, 12, 1):
    if(i == 8):
        break #when i == 8, then for-loop ends automatically
    else:
        print(i) #prints 1 to 7
print()

# Continue statement
for j in range(0, 12, 1):
    if (j == 8):
        continue #when i == 8, then for-loop ignore i = 8 and go to i = 9;
    else:
        print(j) #prints 1 to 12 without 8 
