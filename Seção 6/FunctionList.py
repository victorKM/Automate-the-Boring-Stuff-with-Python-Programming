import copy

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)
#Will print [1,2,3,'Hello']


#this function copy allows you to modify
#cheese without modifying the spam
#if you did cheese = spam, the cheese[1] = 42
#would affect the string of spam
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
