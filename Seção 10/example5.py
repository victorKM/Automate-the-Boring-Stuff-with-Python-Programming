import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # have 2 groups
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))') #have 3 groups


# \d Any numeric digit from 0 to 9
# \D Any character thaat is not a numeric digit from 0 to 9
# \w Any letter, numeric digit, or the underscore character. Think of this as matching "word" characters
# \W Any character that in not a letter, numeric digit, or the underscore character
# \s Any space, tab, or newline character. Think of this as matching "space" characters.
# \S Any character that is not a space, tab, or newline

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking'

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo)


vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex2 = re.compile(r'[aeiouAEIOU]{2}') #two vowels in a row
vowelRegex3 = re.compile(r'[^aeiouAEIOU]') #every character that is not on [ ]
especficRegex = re.compile(r'[a-f]') #a to f

mo = vowelRegex.findall('Robocop eats baby food.')
print(mo)

mo = vowelRegex2.findall('Robocop eats baby food.')
print(mo)

mo = vowelRegex3.findall('Robocop eats baby food.')
print(mo)

mo = especficRegex.findall('Robocop eats baby food.')
print(mo)






