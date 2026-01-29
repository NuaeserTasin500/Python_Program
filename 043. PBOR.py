## Pass-By-Object-Reference (PBOR) 
#In Python programming, there is no true Pass-By-Value (PBV) and Pass-By-Reference (PBR)

#Pass-By-Value (PBV): In PBV, the actual value of the variable is copied into the function's parameter. Changes to the parameter inside the function do not affect the original variable.
#Sometimes Pass-by-Value (PBV) is also called as Call-by-Value (CBV) 
#Example of PBV/CBV in C programming:
#
#include <stdio.h>
#void increment(int num) {
#    num = num + 1;
#
#}
#
#int main() {
#    int number = 10;    
#    increment(number);   
#    printf("%d", number); // still it is 10
#    return 0;
#}
#
#Here the original value of number can't be changed becuase the actual value of 'number' variable passed to the increment(int num) function as a copy
#
#
#Pass-By-Reference (PBR): A reference (address/memory location) to the original variable is passed. Changes to the parameter inside the function directly affect the original variable.
#Sometimes Pass-by-Reference (PBR) is also called as Call-by-Reference (CBR) 
#Example of PBR/CBR C programming:
#
#include <stdio.h>
#void increment(int *num) {
#    *num = *num + 1;
#
#}
#
#int main() {
#    int number = 10;    
#    increment(&number);   
#    printf("%d", number); // changed as 11
#    return 0;
#}
#
#Here the original value of number can be changed becuase the actual value of 'number' variable passed to the increment(int num) function as a reference
#
#Maximum programming language defaultly make function as PBV (not PBR), because defaultly making a function as PBR could be a high risk.
#
# 
#
#In Python programming, There is no true PBV and PBR in function. It is PBOR (Pass-by-Object-Reference). It depends on whether the variable is Mutable or Immutable



# PBOR for Immutable object
def func1(x):
    x = x + 1

a = 10
func1(10)
print(a) #prints '10' (not '11')


# PBOR for Mutable object
def func2(y):
    y.append(100)

b = [1, 2, 3]
func2(b)
print(b) #prints '[1, 2, 3, 100]'
