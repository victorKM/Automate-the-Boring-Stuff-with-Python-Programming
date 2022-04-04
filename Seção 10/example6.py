import re

#Phrase begins with a specific word
beginsWithHelloRegex = re.compile(r'^Hello')
wo = beginsWithHelloRegex.search('Hello there!')
print(wo)

beginsWithHelloRegex.search('He said "Hello"!') == None

#Phrase ends with a specific word
endsWithWorldRegex = re.compile(r'world!$')
wo = endsWithWorldRegex.search('Hello world!')
print(wo)

#All phrase with this pattern
allDigitsRegex = re.compile(r'^\d+$')
wo = allDigitsRegex.search ('252377812381')
print(wo)

#Every word in the phrase that ends with "at"
atRegex = re.compile (r'.at')
wo = atRegex.findall('The cat in the hat sat on the flat man.')
print(wo)

atRegex = re.compile(r'.{1,2}at')
wo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(wo)

# .* means anything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
wo = nameRegex.findall('First Name: Al Last Name: Sweigart')
print(wo)

serve = '<To serve humans> for dinner.'

nongreedy = re.compile(r'<(.*?)>')
wo = nongreedy.findall(serve)
print(wo)

greedy = re.compile(r'<(.*)>')
wo = greedy.findall(serve)
print(wo)

prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law'
print(prime)

#will search until a breakline
dotStar = re.compile(r'.*')
wo = dotStar.search(prime)
print(wo)

#will search until the final of the phrase including the \n
dotStar = re.compile(r'.*', re.DOTALL)
wo = dotStar.findall(prime)
print(wo)

vowelRegex = re.compile(r'[aeiou]')
wo = vowelRegex.search('Al, why does your programming book talk about RoboCop so much?')
print(wo)

wo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(wo)

vowelRegex = re.compile(r'[aeiou]', re.I) #this re.I considerate the upper and lower case
wo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(wo)


