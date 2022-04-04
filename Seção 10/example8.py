import re

# TODO: Create a regex for phone number

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d) | (\(\d\d\d)))?          # area code (optional)
(\s | -)                           # first separator
\d\d\d                             # first 3 digits
-                                  # separator
\d\d\d\d                           # last 4 digits
((ext(\.)?\s) |x)                  # last 4 digits
(\d{2,5})                          # extension number-part(optional)
)

''', re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+ #name part
@               #@ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# TODO: Get the text off the clipboard
# use text = pyperclip.paste()

# TODO: Extract the email/phone form this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy the extracted email/phone to the clipboard
'\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
#pyperclip.copy(results)
