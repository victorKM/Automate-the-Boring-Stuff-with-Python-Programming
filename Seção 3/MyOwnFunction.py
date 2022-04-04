#def function_name() allow you to
#make your own function
def hello():
    print('Victor')
    print('Victor')
    print('AAAAAAAA')

#Definition of a function with arguments
def print_name(name):
    print(name)
    print(name+'!')
    print('Hello '+name)

#Another creation of function
def plusOne(number):
    return number+1

hello()
print('Coloque seu nome')
myName = input()
print_name(myName)

#If a functiona doesnt have a return
#the default return value is None

#ATTENTION WITH FUNCTION print()

#print('cat', 'dog', 'mouse')
#output: cat dog mouse

#print('cat', 'dog', 'mouse', sep='ABC')
#output: catABCdogABCmouse

#print('Hello', end=' ')
#print('World')
#output: Hello World

#print('Hello')
#print('World')
#output: HelloWorld


