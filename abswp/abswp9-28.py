
'''
#"Regular Expression Basics"
import re

message = 'yo its ya boy skinny pete, call me at 415-575-1234 for my cell.\
If you dont wanna call that number its chill,call my boy combo up at\
343-298-8396 on his cell.'
yogabbagabba = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = yogabbagabba.search(message)
print(yogabbagabba.findall('yo its ya boy skinny pete, call me at 415-575-1234 for my cell.\
If you dont wanna call that number its chill,call my boy combo up at\
343-298-8396 on his cell.'))
print(mo.group())

#mo means matching object, but its just a regular variable, its name
#can be anything

#usual order for re : compile   search    group

#optionally, if you wanna find all patterns in a message, the order becomes:
#   compile     findall

#the regex for a numeric digit is \d
'''
#"Regex Groups and the pipe character"
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('the secret number to call the president is\
914-559-0101.')
print(mo.group())
print(mo.group(1)) #the parathesis in compile mark which group to look at
print(mo.group(2))

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mop = phoneNumRegex.search('My number is 444-454-4049, if not try (111) 111-1111')
mo = phoneNumRegex.search('My number is (134) 453-4039')
print(mop.group())
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('The Batmobile just lost a wheel and Batman let\
the joker get away. Also Batbat showed up at one point and ate a child')
print(mo.group())
#mo = batRegex.search('The Batmotorcycle just lost a wheel')#if you search 
#print(mo.group())   #for a pattern and there isn't one, it will give 
#return the none value and give an error, there needs to be a pattern found
print(mo.group(1))
print(batRegex.findall('The Batmobile just lost a wheel and Batman let\
the joker get away. Also Batbat showed up at one point and ate a child'))

#the regex for making parathesis is \( and \)
#if you wanna use parathesis to create groups don't put the backslash in









