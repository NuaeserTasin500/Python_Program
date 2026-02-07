## Getter and Setter
class MyClass: 
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f'Value is {self._value}')

    @property #setting getter
    def ten_value(self): #getter
        return 10*self._value
    
    @ten_value.setter #setting setter
    def ten_value(self, new_value): #setter
        self._value = new_value
        return 10*self._value
    
    
obj = MyClass(10)
print(obj._value) #prints '10'
print(obj.ten_value) #prints '100'
obj.show() #prints 'Value is 10'
print()

# For changing values, it needs setter
obj.ten_value = 12 #it goes to @ten_value.setter
print(obj.ten_value) #prints '120' 
