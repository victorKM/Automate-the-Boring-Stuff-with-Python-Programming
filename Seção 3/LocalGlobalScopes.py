# =================================================================== #
print('1 Example')
spam = 42 #global variable

def eggs():
    spam = 55 #local variable

print(spam) #output 42
eggs() #this dont change of the spam value outside the scope
print(spam) #output 42
print('===================')

# =================================================================== #

#Another example
print('2 Example')
def first():
    car = 99
    second()
    print(car)

def second():
    moto = 101
    car = 0

first() #will just print 99
print('====================')

# =================================================================== #

#Another example
print('3 Example')
def test_global():
    print(global_varible)

global_varible = 42  #its a global variable
test_global() #prints 42
print('========================')

# =================================================================== #

#Another example
print('4 Example')
def spamming():
    #but if u put here "global milk", milk=hello will change to hello everywhere
    milk = 'Hello'
    print(milk)

milk = 42
spamming() #prints Hello
print(milk) #prints 42

print('========================')

# =================================================================== #

#to declare a global variable u need to put "global" prefixe on variable


