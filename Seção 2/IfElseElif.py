#Example of If Else
print('Whats your name?')
myName = input()
if myName == 'Alice':
   print('Hi Alice')
else:
    print('Hi Stranger')



#Example of Elif (igual a else if)
name ='Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

#Another example
print('Enter a name.')
name = input()
if name:
    print('Thank you for entering a name.')
else: print('You did not enter a name')

