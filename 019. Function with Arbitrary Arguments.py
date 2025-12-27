## Function with Arbitrary Arguments

def sum(*numbers):
    result = 0
    for i in numbers:
        result = result + i
    return result

summation = sum(1, 2, 3, 4)
print(summation) #prints 10, the result of 1+2+3+4
