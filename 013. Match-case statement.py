# Match-case statements

a = int(input("Enter a number: "))
match a:
    case 0:
        print("Your number is zero")
    case 1:
        print("Your number is one")
    case 2:
        print("Your number is two")
    case 3:
        print("Your number is three")
    case 4:
        print("Your number is four")
    case 5:
        print("Your number is five")
    case _ if a > 0:
        print("Your number is more than five")
    case _:
        print("Your number is negative")
        
