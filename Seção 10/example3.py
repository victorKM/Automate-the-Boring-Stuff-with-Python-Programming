import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group()) #will print 'Batmobile'

mo = batRegex.search('Batmotorcycle lost a wheel')
print(mo.group())  #will cause an error

