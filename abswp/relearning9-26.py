'''
opjobs = {'luffy':'captain','zoro':'swordsman','nami':'navigator',\
          'Go. D. Usopp':'sniper','sanji':'cook','chopper':'doctor',\
          'robin':'archeologist','franky':'shipwright',\
          'brook':'musician','jimbei':'helmsmen'}
oporder = {'luffy':1,'zoro':2,'nami':3,\
          'Go. D. Usopp':4,'sanji':5,'chopper':6,\
          'robin':7,'franky':8,\
          'brook':9,'jimbei':10}
print(opjobs == oporder, 'blackbeard' not in oporder)
print(f"in one piece, Luffy is the {opjobs['luffy']}. And Nami is the \
{opjobs['nami']}.")
#You can't make a ranking since dictionaries are unordered, it doesn't know
#luffy is the first 1 and jimbei is the last.
print(list(opjobs.keys()))
opsh = opjobs.keys() #this one will still work but it will show dict_keys
    #in the front. To avoid this you need to add the list function in front
print(opsh)
print(opjobs.values())
print(list(opjobs.values()))
print(list(opjobs.items()))
for i in oporder.keys():
    print(i)
for k in opjobs.items():
    print(k)
for k, v in opjobs.items():
    print(f'{k} is the {v}.')
print(opjobs.get('luffy', 'nope'))
print(opjobs.get('luffi', 'nope'))
print(f"If i'm remembering right, then nami was \
{oporder.get('nami','not actually fit')} to join the crew.")
print(f"If i'm remembering right, then nami was \
{oporder.get('namy','not actually fit')} to join the crew.")
oporder.setdefault('nami', 6.5)
print(oporder)
'''
import pprint
message = "we're really quite suprised that we get to see you another night \
you should have looked for another job, you should have said to this place \
goodbye. Its like your so much more, like you've been in this place before \
we remember a face like yours, you seem aquainted with those doors."
count = {}
"""
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1
print(count)
for i in message.upper():   #.upper() makes it so it counts both an
    #uppercase letter and a lowercase letter in the same category
    count.setdefault(i, 0) #if we don't do this we get an error that count
    #doesn't exist, as it didn't before that
    count[i] = count[i] + 1
print(count)
"""
for i in message.upper():  
    count.setdefault(i, 0) 
    count[i] = count[i] + 1
pprint.pprint(count) #pprint just makes the print lists look nicer.






