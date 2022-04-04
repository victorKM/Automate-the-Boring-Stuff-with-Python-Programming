import re


print('Regex 1: ')
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The adventures of Batwowowowoman')
print(mo == None)

print(' ====================================================== ')

print('Regex 2: ')

batRegex2 = re.compile(r'Bat(wo)*man') #* means that wo need to appear zero or more times
mo = batRegex2.search('The Adventures of Batman')
print(mo.group())

mo = batRegex2.search('The adventures of Batwoman')
print(mo.group())

mo = batRegex2.search('The adventures of Batwowowowoman')
print(mo.group())

print(' ====================================================== ')

print('Regex 3: ')

batRegex3 = re.compile(r'Bat(wo)+man') #+ means that wo need to appearone or more times
mo = batRegex3.search('The Adventures of Batman')
print(mo == None)

mo = batRegex3.search('The adventures of Batwoman')
print(mo.group())

mo = batRegex3.search('The adventures of Batwowowowoman')
print(mo.group())

print(' ====================================================== ')

print('Regex 4: ') #find the +, * or ? symbols

regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())

regex = re.compile(r'(\+\*\?)+') #appear one or more times
mo = regex.search('I learned about +*?+*?+*?+*? regex syntax')
print(mo.group())

print(' ====================================================== ')

print('Regex 5: ') #HaHaHa

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo)

haRegex = re.compile(r'(Ha){3,5}') #at least 3, at max 5 times
mo = haRegex.search('He said "HaHaHa"')
print(mo)
#if has HaHaHaHaHaHaHaHaHa will match just the first 5 Ha

# The ? says the group matches zero or one times
# The * says the group matches zero or more times
# The + says the group matches one or more times
# The { } can match a specific number of times
# The { } with two numbers matches a mininum and maximum number of times
# Leaving out the first or seconde number in the { } says there is no minimum or maximum
# Greedy matching match the longest string possible, nongreedy matching match the shortest string possible
# Putting a question mark after the { } makes it do a nongreedy match









