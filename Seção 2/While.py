#Example of While
spam = 5
while (spam > 0):
    print('Hi Victor')
    spam = spam - 1

#Another example
name= ' '
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

#You can use break
name = ' '
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break  #here will stop the will structure
print('Thank you!')

#You can use continue
spam = 0
while (spam < 0):
    spam = spam + 1
    if spam == 3:
        continue  #will jump for next step of the loop, the print above will not run
    print('spam is '+ str(spam))
    