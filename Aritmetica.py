#Scanner created with Aritmetica.ATG data
from AFDFixed.AFD import *


exceptions = ['while','do','if','switch']
adfArray = []
ident= 'ident'
temp = AFD(ident)
tempidentAcceptance = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: True, 7: False, 8: False, 9: False, 10: False, 11: False, 12: False, 13: False, 14: False, 15: False}

temp.setDictAcceptance(tempidentAcceptance)
tempidentTransitions = {0: {1: ['l']}, 1: {2: {41}}, 2: {3: ['t']}, 3: {4: ['t']}, 4: {5: {41}}, 5: {6: ['r']}, 6: {7: ['l'], 8: ['d']}, 7: {9: {41}}, 8: {10: ['i']}, 9: {11: ['t']}, 10: {12: {46}}, 11: {13: ['t']}, 12: {14: ['i']}, 13: {15: {41}}, 14: {6: ['t']}, 15: {6: ['r']}}

temp.setTransition(tempidentTransitions)
adfArray.append(temp)
number= 'number'
temp = AFD(number)
tempnumberAcceptance = {0: False, 1: False, 2: False, 3: False, 4: False, 5: True, 6: False, 7: False, 8: False, 9: False}

temp.setDictAcceptance(tempnumberAcceptance)
tempnumberTransitions = {0: {1: {40}}, 1: {2: ['i']}, 2: {3: {46}}, 3: {4: ['i']}, 4: {5: ['t']}, 5: {6: {40}}, 6: {7: ['i']}, 7: {8: {46}}, 8: {9: ['i']}, 9: {5: ['t']}}

temp.setTransition(tempnumberTransitions)
adfArray.append(temp)
temp = ''
name = ""
previousName = ''
previousAcceptance = ''
found = False
tokensFound = []
#text = 'ho(la  10 123dsa2 sad as ads32 93r 2( sa0d ] &  + s  +  ==1 1 ?823?'
f = open("tareas.txt", "r")
text = f.read()
for i in text:
    temp = temp + i
    for j in range (0,len(adfArray)):
        found, acceptance, name= adfArray[j].simulation(temp)
        if found:
            previousName = name
            previousAcceptance = acceptance
            break
        else:
            if not(j == len(adfArray)-1):
                pass
            else:
                temp = temp[:len(temp)-1]
                if not(previousName == '') and not(previousAcceptance == ''):
                    tokensFound.append((temp,previousName))
                previousName = ''
                temp = i
                for k in adfArray:
                    found, acceptance, name= k.simulation(temp)
                    if found:
                        previousName = name
                        previousAcceptance = acceptance
                        break
                if found:
                    break
if acceptance:
    tokensFound.append((temp,name))
for i in range(0, len(tokensFound)):
    temp = list(tokensFound[i])
    if temp[0] in exceptions:
        index = exceptions.index(temp[0])
        temp[0] = exceptions[index]
        temp[1] = exceptions[index]
        tokensFound[i] = temp
for i in tokensFound:
    print(i)
#print(tokensFound)