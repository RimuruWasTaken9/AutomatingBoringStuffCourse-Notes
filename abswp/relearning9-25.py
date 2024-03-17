"""
#Guessing game but updated a bit
import random
b = random.randint(1,500)
for i in range(50):
    try:
        guess = int(input("you know the drill: "))
        if guess + 100 < b:
            print('WAYYY too low')
        elif guess - 100 > b:
            print('''can't get much higher''')
        elif guess + 50 < b:
            print('at least 50 too low')
        elif guess - 50 > b:
            print('at least 50 too high')
        elif guess + 10 < b:
            print('at least 10 too low')
        elif guess - 10 > b :
            print('at least 10 too high')
        elif guess < b:
            print('bit higher')
        elif guess > b:
            print('bit lower')
        
        
            
        else:
            print('we really do have the luck of a king')
            break
    except ValueError:
        print("I'll fucking eat you I stg")
print('cable cord')
"""
diseases = ['cancer', 'aids', 'cold', 'flu', 'dementia', 'bubonic plague',\
            'dementia', 'dementia', 'dementia', 'dementia','dementia', 'dementia','diabetes']

'''''
print(diseases)
for i in range(len(diseases)):
    print('disease ' + str(i) + ' in the list is: ' + diseases[i])
#Explaining above thing^^^: creates a list(diseases in this case)
    #sets up a for loop traditionally until we get to range
    #inside the range function, we add the length function
    #^^^this means the for loop goes for however many items are in the list
    #put the name of the list inside the length function
    #convert the variable in the for loop from an int into a string
    #^^^ this will tell us what number we're on in the list
    #call the list name and put the variable as the argument, so each item
    #on the list is shown in that loop of the for loop.

    #Use this shit
print('\n\nDiseases: ')
for i in range(len(diseases)):
    print(diseases[i])
'''''
"""
diseases.index('flu') #shows what number it is in the list
diseases.index('dementia')
print(diseases)    
diseases.append('Lung Cancer Stage 4')
diseases.insert(4,'Fever')
diseases.remove('aids')
print(diseases)
del diseases[3]
print (diseases)
print ('the diseases list has: ',len(diseases),' items.' ) #these basically
print (f'the diseases list has: {len(diseases)} items.' )  #print the same
"""
'''
import copy
opc = ['luffy','nami','zoro','stuart','enel','Eneru'
        ,'blackbeard','doffy','donut boi','joyboi']
print(opc)
opc.sort()
print(opc)
opc.sort(reverse=True)
print(opc)
opc.sort(key=str.lower)
print(opc)
for i in opc:
    print(i)
cheese = opc
print(cheese)
cheese[2] = 'robin'
print(cheese)
print(opc)
def within(cheese):
    cheese.append('chopper')
opc
within(opc)
print(opc)
chess = copy.deepcopy(opc)
chess[1:4] = ['bishop','knight','queen','king']
print(chess)
print(opc)
def withine(opc):
    copy.deepcopy(opc.append('kaido'))
opc
withine(chess)
print(chess)

print(opc)
l = 'bug'
print('can I really get', \
      l,'and still make it to the finals?')
print('can I really get', l,'and\
 still make it to the finals?')
'''
