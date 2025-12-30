## Exception Handling

a = input("Enter a number: ")
try:
    print(f"You have input: {int(a)}")

except:
    print(f"You have input: ∞")
print()



#specific error handling
try:
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(a)
    index = int(input("Input 0~7:"))
    print(a[index])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Index error") 
