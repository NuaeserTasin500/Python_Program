## Docstring
#In docstring, you don't need variable store
'''Hello World'''
'''Hello 
How are you'''
print(__doc__) #only prints 'Hello World'
#That's why it is recommended to use only one docstring, if you don't need variables
print()


#using funnction
def abcd():
    '''Hello. 
What's up?''' #end of abcd function

print(abcd.__doc__) #prints 'Hello <newline> What's up?'
