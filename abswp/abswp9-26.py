op = 'one piece'
print(op.upper())
print(op)
yell = 'YO ONE PIECE IS AWESOME'
print(yell.lower())
yelle = 'YO OnE PIEce IS aWEsOmE'
print(yelle.lower())
print(yelle.upper())
print(yelle.islower())
print(yelle.isupper(),'\n')
print(yell.isupper())
whoasked = ''           #there needs to be at least 1 upper
print(whoasked.isupper()) #or lower digit for it to be true, but also only
print(whoasked.islower()) #upper or lower for the entire message to be true
print(yelle.upper().isupper())


#there are a bunch of other is##### cases, like:
#isalpha() = letters only
#isdecimal() = numbers only,
#isalnum() = letters and numbers only
#isspace() = whitespace only
#istitle() = words with only the first letter capitalized and the rest lowercase


print('this shit is cold ngl'[4].isspace()) #only looking at 4 in index
print('Im Gonna Be Serious, This One Is Weird'.istitle())
print('the akatsuki is now assembled'.startswith('the ak'))
print('the akatsuki is now assembled'.endswith('bled'))
print(','.join(['zou','whole cake','wano']))
print('zou','whole cake','wano')
print('\t\t'.join(['zou','whole cake','wano']))
print('oh it takes more than meets the eye'.split())
courtcall = 'oh it takes more than meets the eye'.split()
print(courtcall)
print('oh it takes more than meets the eye'.split('m'))
print('hello world'.rjust(23))
print('hello world'.ljust(23) + 'after just')
print('hello world'.rjust(23, '-'))
print('hello world'.ljust(23,'*')) #all of these fill spaces have to be 1 unit
print('hello world'.center(28,'='))
taco = 'skiddlywiffers'
print(taco.center(22,'^'))
taco1 = taco.rjust(22)
print(taco1)
print(taco1.strip())
print('          yooo          '.lstrip())
print('spamspambaconeggsspamspamdinnerspammer'.strip('spa'))
print(taco.replace('d', 'XXX'))  #replace any 'd' in taco with 'XXX'
print('hey there everybody I just wanted to know if this worked or not\
 no big deal')
