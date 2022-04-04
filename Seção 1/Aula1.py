# This program says hello and asks for my name

print('Hello World')

print('What is your name?') # ask for their name
myName = input()
print('It is good to mmet you, '+ myName)

print('The length of your name is: ')
print(len(myName))

print('What is your age') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

#print() displays the value passed to it
#input() lets user type in a value
#len() takes a string value and returns an integer value of the string's length
#int(), str(), and float() convert values data type
