import re

print('? section')
batRegex = re.compile(r'Bat(wo)?man')
#? tracks if the group appears 0 or 1 times
mot = batRegex.search('The adventures of Batman')
mo = batRegex.search('The adventures of Batwoman')
print(mot.group())
print(mo.group())
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
jer = phoneRegex.search("yo jerry, I don't think you got my text, its alright \
just call be back. Oh don't call my phone tho I don't wanna see that \
call the number 987-654-3210")
print(jer.group())
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(phoneRegex.search("yo jerry, I don't think you got my text, its alright \
just call be back. Oh don't call my phone tho I don't wanna see that \
call the number 987-654-3210"))
print(phoneRegex.search("yo jerry, I don't think you got my text, its alright \
just call be back. Oh don't call my phone tho I don't wanna see that \
call the number 654-3210"),'\n')

#the reg for adding a ? to a pattern is \?
#additionally, if you are only looking for one specific word like dinner
#you can just have (r'dinner'), and if you need a question mark:(r'dinner\?')
print('* section')
batRegex = re.compile(r'Bat(wo)*man')
#* tracks if the group appears 0 or more times
print(batRegex.search('The adventures of Batman'))
print(batRegex.search('The adventures of Batwoman'))
print(batRegex.search('The adventures of Batwowowowowowoman'),'\n')

#the reg for adding a * to a pattern is \*?
print('+ section')
batRegex = re.compile(r'Bat(wo)+man')
#+ tracks if the group appears 1 or more times
print(batRegex.search('The adventures of Batman'))#doesn't find it here
print(batRegex.search('The adventures of Batwoman'))
print(batRegex.search('The adventures of Batwowowowowowoman'),'\n')

#the reg for adding a + to a pattern is \+

print('light recap section')
regex = re.compile(r'\+\*\?')
print(regex.search("I learned about +*? regex syntax, which seem kinda self \
explanatory now..."))
regex = re.compile(r'(\+\*\?)+')
print(regex.search("I learned about +*?+*?+*?+*?+*?+*?+*? regex syntax, \
which seem kinda self explanatory now..."),'\n')

print('{x} section')
haRegex = re.compile(r'(Ha){3}')
#{x} tracks if the group appears exactly x number of times
print(haRegex.search('He said HaHaHa'))

phoneRegex = re.compile       \
(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?(, )?( )?(, and )?){3}')#this shit is wild
#it checks for all of those optional endings and ignores if they aren't there
#just remember the {3} means we need three of the phone numbers in a row
print(phoneRegex.search("My phone numbers aren't \
333-333-3333444-4444,212-212-2121"))
print(phoneRegex.search("My phone numbers aren't \
333-333-3333444-4444, 212-212-2121"))
print(phoneRegex.search("My phone numbers aren't \
333-333-3333444-4444, and 212-212-2121"),'\n')

print('{x,y}/min max section')
haRegex = re.compile(r'(Ha){3,5}')
#{x,y} tracks if the group appears minimum x and maximim y number of times
print(haRegex.search('He said HaHaHa'))
print(haRegex.search('He said HaHaHaHaHa'))
print(haRegex.search('He said HaHaHaHaHaHa'))
#this one directly above still matches but only the first 5 'Ha's, not the 6th
haRegex = re.compile(r'(Ha){5,}')#this works like a slice, making it 5 - more
print(haRegex.search('He said HaHaHaHaHaHa'))

digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))
'''     ^^^^^^^^
By default, python is greedy. It will look for the first 5 digits that
match. Even though it would also have found a match at 23456, python
returned with the match 12345 since it looks for the first possible
match. Also worth noting is that it returned the maximum 5 variables
instead of the minimum and quicker first 3 digits 123. This is again
because by default, regular expressions in python do greedy matches.
It will try to match the longest possible string that matches this pattern
Instead of matching 123, regular expressions will try to match the longest
possible string, being 12345
'''
print(digitRegex.search('1234 567890'))
print(digitRegex.search('123 4 567890'))
#in these cases if it can't find 5 digits, it will instead give a more
#minimum amount, the first one being 4, and the second being 3 since
#there was no larger option.
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1234567890'))
'''to do a none greedy match, put a ? after the {x,y} pattern.
this isn't the same as the normal ?, as when it is after the {x,y}
pattern instead of a group, it means to do a 'non greedy match'.'''


