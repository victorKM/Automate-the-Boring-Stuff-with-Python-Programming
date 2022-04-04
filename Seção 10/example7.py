import re

#
namesRegex = re.compile(r'Agent \w+')
wo = namesRegex.findall ('Agent Alice gave the secret documents to Agent Bob.')
print(wo)


#sub('word', 'phrase'), the word will substitute the thing specfied in the regex
wo = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(wo)


namesRegex = re.compile(r'Agent (\w)\w*')
wo = namesRegex.findall ('Agent Alice gave the secret documents to Agent Bob.')
print(wo)

wo = namesRegex.sub('Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')
print(wo)

# re.VERBOSE ignore all blank spaces on breaklines
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d', re.VERBOSE)


#you can do
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d', re.VERBOSE | re.IGNORECASE | re.DOTALL)


