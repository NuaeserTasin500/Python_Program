## Nested Tuple
#nested tuple looks as same as two dimensional tuple but not exactly it is two dimensional tuple


#suppose a student's name is John. His roll is 10. He got 99 in mathematics, 95 in physics, 90 in chemistry. We want to store that in a tuple
student_name_1 = "John"
student_roll_1 = 10
mat_phy_che_1 = (99, 95, 90)

student_data_1 = (student_name_1, student_roll_1, mat_phy_che_1) #This is nested tuple
print(student_data_1) #prints '('John', 10, (99, 95, 90))'
print()


# simple way we can declare nested tuple
student_data_2 = ("Max", 11, (95, 84, 87))
print(student_data_2) #prints '('Max', 11, (95, 84, 87))'
print()


# indexing 
print(student_data_2[0]) #prints 'Max'
print(student_data_2[1]) #prints '11'
print(student_data_2[2]) #prints '(95, 84, 87)'
print(student_data_2[2][0]) #prints '95'
print(student_data_2[2][1]) #prints '84'
print(student_data_2[2][2]) #prints '87'
print()


# Two dimensional tuple <S>
tdtuple = ((20, 30), (40, 50), (60, 70))
print(tdtuple)
