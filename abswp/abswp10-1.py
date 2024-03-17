
import re
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
#using the carrot symbol means it needs to be at the start of the string

endswithWorldRegex = re.compile(r'world$')
print(endswithWorldRegex.search('Hello world'))
print(endswithWorldRegex.search('Hello world!'))
#using the dollar sign means it needs to be at the end of the string

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('289640257500'))
print(allDigitsRegex.search('2896402x57500'))
#Having both the carrot and dollar means it needs to match the entire string

atRegex = re.compile(r'.at')
print(atRegex.findall('the cat in the hat sat on the flat mat.'))
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('the cat in the hat sat on the flat mat.'))
#having a . means any character at all, except for a newline

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Jimmy Last Name: Neutron'))
#having a .* means zero or more of any character at all, except for newline


serve = '<to serve humans> for dinner.>'

nonGreedyRegex = re.compile(r'<(.*?)>')
print(nonGreedyRegex.search(serve))
greedyRegex = re.compile(r'<(.*)>')
print(greedyRegex.search(serve))
#   .* uses greedy mode, matching as much as possible
#   .*? uses non greedy mode, matching the quickest one, usually minimum


prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))
#this greedy search goes up to the newline. Since . doesn't include newlines


dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))
#by adding re.DOTALL, the . now includes newlines as well


vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Hey guys, look, a birdie. Alright you know what \
nvm lets make a backrooms joke instead to celebrate the new update.'))
vowelRegex = re.compile(r'[aeiou]',re.I)
print(vowelRegex.findall('Hey guys, look, a birdie. Alright you know what \
nvm lets make a backrooms joke instead to celebrate the new update.'))
#by adding re.I , short for re.IGNORECASE , it looks for both uppercase
#and lowercase in the string despite only the lowercase being specified
#in the pattern. Making it case-insensitive.


#New lesson/video:
import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to \
Agent Neutron'))
print(namesRegex.sub('REDACTED','Agent Alice gave the secret documents to \
Agent Neutron'))
#.sub is short for .substitute, its does the same thing as find and replace
#you put what you want replaced in the first string, and what you want
#to replace in the second string.

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to \
Agent Neutron'))
print(namesRegex.sub(r'Agent \1****','Agent Alice gave the secret documents\
to Agent Neutron'))
#the \1 is for wanting to keep some part of the original text the same.
#the number after the backslash corresponds to the group in the compile

re.compile(r'''
(\d\d\d-)|    # area code (without parens, with dash)
(\(\d\d\d\) ) # -or- area code with parens and no dash
-          #first dash
\d\d\d     #first 3 digits
-          #second dash
\d\d\d\d   #last 4 digits''', re.VERBOSE)
#re.VERBOSE first ignores empty spaces and newlines, allowing you to expand
#the pattern to multiple lines to make it clearer. You can also add comments
#within the string itself. They aren't actually python comments but they
#have the same syntax. TLDR re.VERBOSE lets you format better

multipleRegex = re.compile(r'''Hey guys, look, a birdie. #ttg reference
Alright you know what nvm lets make a backrooms joke #backrooms reference
instead to celebrate the new update. #more backrooms reference
''', re.I | re.VERBOSE | re.DOTALL)
#if you ever wanted to use multiple of these options, you have to seperate
#them using the pipeline. Its an old design thing. (Probably will never use)



