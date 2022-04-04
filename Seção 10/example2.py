import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search ('Call me 415-555-1011 tomorrow, or at 415-555-9999')
no = phoneNumRegex.findall ('Call me 415-555-1011 tomorrow, or at 415-555-9999')

print(mo.group())
print(mo.group(1)) #numbers in the first parentesis
print(mo.group(2)) #numbers in the second parentesis
print(no)

#phoneNumRegex.search will find just the first number on the text
#phoneNumRegex.findall will find all the numbers on the text