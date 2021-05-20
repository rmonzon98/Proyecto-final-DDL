#Scanner created with Aritmetica.ATG data
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
precedence = {'ident': 0, 'number': 1}

adfArray = []
ident= 'ident'
temp = AFD(ident)
tempidentAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempidentAcceptance)
tempidentTransitions = {0: {1: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}]}, 1: {1: {48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}}}

temp.setTransition(tempidentTransitions)
adfArray.append(temp)
number= 'number'
temp = AFD(number)
tempnumberAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempnumberAcceptance)
tempnumberTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempnumberTransitions)
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
            previousName = get_key(acceptanceArray.index(True),precedence)
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
    
