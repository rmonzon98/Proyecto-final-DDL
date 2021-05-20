#Scanner created with Double.ATG data
from AFDFixed.AFD import *

def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "key doesn't exist"

def isHigher(val1, val2):
    if val1 < val2:
        return True
    else:
        return False
    


exceptions = ['while','do','if','switch']
precedence = {'number': 0, 'decnumber': 1, 'white': 2}

adfArray = []
number= 'number'
temp = AFD(number)
tempnumberAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempnumberAcceptance)
tempnumberTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempnumberTransitions)
adfArray.append(temp)
decnumber= 'decnumber'
temp = AFD(decnumber)
tempdecnumberAcceptance = {0: False, 1: False, 2: False, 3: True}

temp.setDictAcceptance(tempdecnumberAcceptance)
tempdecnumberTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}], 2: [{46}]}, 2: {3: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 3: {3: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempdecnumberTransitions)
adfArray.append(temp)
white= 'white'
temp = AFD(white)
tempwhiteAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempwhiteAcceptance)
tempwhiteTransitions = {0: {1: [{32, 9, 10, 13}]}, 1: {1: [{32, 9, 10, 13}]}}

temp.setTransition(tempwhiteTransitions)
adfArray.append(temp)
f = open("tareas.txt", "r")
text = f.read()

temp = ''
name = ""
previousName = ''
previousFound = False
previousAcceptance = False
found = False
tokensFound = []

foundArray = []
for i in range (0,len(precedence)):
    foundArray.append(None)

acceptanceArray = []
for i in range (0,len(precedence)):
    acceptanceArray.append(None)
    

for i in text: 
    for k in range (0,len(precedence)):
        foundArray[k] = None
    
    for k in range (0,len(precedence)):
        acceptanceArray[k] = None

    temp = temp + i

    for j in range (0,len(precedence)):
        found, acceptance = adfArray[j].simulation(temp)
        foundArray[j] = found
        acceptanceArray[j] = acceptance

    if True in foundArray:
        if True in acceptanceArray:
            previousName = get_key(acceptanceArray.index(True),precedence)
            previousFound = True
            previousAcceptance = True
        else:
            previousName = get_key(foundArray.index(True),precedence)
            previousFound = True

    else:

        if not(previousName == ''):
            tokensFound.append([temp[:len(temp)-1],previousName])
            temp = temp[len(temp)-1]
            found = False
            previousName = ''

            for k in range (0,len(precedence)):
                foundArray[k] = None

            for k in range (0,len(precedence)):
                acceptanceArray[k] = None

            for l in range (0,len(adfArray)):
                found, acceptance = adfArray[l].simulation(temp)
                foundArray[l] = found
                acceptanceArray[l] = acceptance

            if True in foundArray:
                if True in acceptanceArray:
                    previousName = get_key(acceptanceArray.index(True),precedence)
                    previousFound = True
                    previousAcceptance = True
                else:
                    previousName = get_key(foundArray.index(True),precedence)
                    previousFound = True
        
        else:
            temp = ''

if True in foundArray:
    previousName = get_key(foundArray.index(True),precedence)
    tokensFound.append([temp,previousName])

for i in tokensFound:
    print(i)
    
