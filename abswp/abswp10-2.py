#! python3

import re
import pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-2934, 333-0000, (302) 444-0000, 920-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    # area code(optional)
(\s|-)   #first seperator
\d\d\d    #first 3 digits
-    #seperator
\d\d\d\d    #last 4 digits
(((ext(\.)?\s)|x)        #extension word-part (optional)
 (\d{2,5}))?         #extension number-part(optional)
)
''',re.VERBOSE)
"""IMPORTANT: When you got the problem earlier with the phone numbers giving
you a jumble of spaces and underscores with .findall, there is a MUCH
easier fix we can implement. By putting the ENTIRE raw string in a group,
all we have to do now is call group 0 in the findall for that 1 group that
contains the entire thing, most of the problem is straight up solved
that way. Then we use the for loop shown below to solve the rest of it"""
# Create a regex for email addresses
emailRegex = re.compile(r'''
    #some.+_thing@something.com

[a-zA-Z0-9_.+]+    #name part   #if you have a .or+ in square brackets, you don't need to put backslashes for them, python will just know
@   #@ symbol
[a-zA-Z0-9_.+]+    domain name part
    
''',re,VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()
# TODO: Extract all emails/phone numbers from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    
print(allPhoneNumbers) #just to check we got it right
# TODO: Copy the extracted email/phone to the clipboard
'\n'.join(allPhoneNumbers)
#^^^forgot this one existed, takes a list and removes all the things that
#aren't values and joins everything together. The only thing seperating
#the values are what we put in front of .join, in this case, a newline
'\n'.join(extractedEmail)
#were supposed to delete these two lines above and replace with line below
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)


#The result of this program shouldn't have any output, what it does is scan
#a document for phone numbers and emails and nicely formats it into your
#clipboard(ctrl + c thing)
