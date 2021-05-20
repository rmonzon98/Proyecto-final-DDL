#Scanner created with .ATG data
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
precedence = {}

adfArray = []
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

if True in foundArray:
    previousName = get_key(foundArray.index(True),precedence)
    tokensFound.append([temp,previousName])

for i in tokensFound:
    print(i)
    
