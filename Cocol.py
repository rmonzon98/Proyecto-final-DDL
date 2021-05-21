#Scanner created with Cocol.ATG data
from AFDFixed.AFD import *

def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "key doesn't exist"
 
exceptions = ['while','do','if','switch']
precedence = {'ident': 0, 'string': 1, 'char': 2, 'charnumber': 3, 'charinterval': 4, 'nontoken': 5, 'startcode': 6, 'endcode': 7}

adfArray = []
ident= 'ident'
temp = AFD(ident)
tempidentAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempidentAcceptance)
tempidentTransitions = {0: {1: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}]}, 1: {1: {48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}}}

temp.setTransition(tempidentTransitions)
adfArray.append(temp)
string= 'string'
temp = AFD(string)
tempstringAcceptance = {0: False, 1: False, 2: False, 3: True}

temp.setDictAcceptance(tempstringAcceptance)
tempstringTransitions = {0: {1: [{34}]}, 1: {2: [{0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255}]}, 2: {3: [{34}], 2: [{0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255}]}}

temp.setTransition(tempstringTransitions)
adfArray.append(temp)
char= 'char'
temp = AFD(char)
tempcharAcceptance = {0: False, 1: False, 2: False, 3: False, 4: True}

temp.setDictAcceptance(tempcharAcceptance)
tempcharTransitions = {0: {1: [{39}]}, 1: {2: [{47}], 3: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}]}, 2: {3: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}]}, 3: {4: [{39}]}}

temp.setTransition(tempcharTransitions)
adfArray.append(temp)
charnumber= 'charnumber'
temp = AFD(charnumber)
tempcharnumberAcceptance = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: True}

temp.setDictAcceptance(tempcharnumberAcceptance)
tempcharnumberTransitions = {0: {1: [{67}]}, 1: {2: [{72}]}, 2: {3: [{82}]}, 3: {4: [{40}]}, 4: {5: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 5: {5: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}], 6: [{41}]}}

temp.setTransition(tempcharnumberTransitions)
adfArray.append(temp)
charinterval= 'charinterval'
temp = AFD(charinterval)
tempcharintervalAcceptance = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11: False, 12: False, 13: False, 14: False, 15: False, 16: True}

temp.setDictAcceptance(tempcharintervalAcceptance)
tempcharintervalTransitions = {0: {1: [{67}]}, 1: {2: [{72}]}, 2: {3: [{82}]}, 3: {4: [{40}]}, 4: {5: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 5: {5: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}], 6: [{41}]}, 6: {7: [{32}]}, 7: {8: [{46}]}, 8: {9: [{46}]}, 9: {10: [{32}]}, 10: {11: [{67}]}, 11: {12: [{72}]}, 12: {13: [{82}]}, 13: {14: [{40}]}, 14: {15: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 15: {15: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}], 16: [{41}]}}

temp.setTransition(tempcharintervalTransitions)
adfArray.append(temp)
nontoken= 'nontoken'
temp = AFD(nontoken)
tempnontokenAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempnontokenAcceptance)
tempnontokenTransitions = {0: {1: [{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255}]}}

temp.setTransition(tempnontokenTransitions)
adfArray.append(temp)
startcode= 'startcode'
temp = AFD(startcode)
tempstartcodeAcceptance = {0: False, 1: False, 2: True}

temp.setDictAcceptance(tempstartcodeAcceptance)
tempstartcodeTransitions = {0: {1: [{40}]}, 1: {2: [{46}]}}

temp.setTransition(tempstartcodeTransitions)
adfArray.append(temp)
endcode= 'endcode'
temp = AFD(endcode)
tempendcodeAcceptance = {0: False, 1: False, 2: True}

temp.setDictAcceptance(tempendcodeAcceptance)
tempendcodeTransitions = {0: {1: [{46}]}, 1: {2: [{41}]}}

temp.setTransition(tempendcodeTransitions)
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

    temp = temp + i

    for k in range (0,len(precedence)):
        foundArray[k] = None
    for k in range (0,len(precedence)):
        acceptanceArray[k] = None

    for j in range (0,len(precedence)):
        found, acceptance = adfArray[j].simulation(temp)
        foundArray[j] = found
        acceptanceArray[j] = acceptance

    #print(temp, " ", foundArray)
    if True in foundArray:
        if True in acceptanceArray:
            tempAcceptanceArray = []
            for c in range(0,len(acceptanceArray)):
                if acceptanceArray[c]:
                    tempAcceptanceArray.append(c)
            index = min(tempAcceptanceArray)
            previousName = get_key(index,precedence)
            tokenName = get_key(index,precedence)
            previousFound = True
            previousAcceptance = True
            tempToken = temp 
        else:
            previousName = get_key(foundArray.index(True),precedence)
            previousFound = True

    else:

        if not(previousName == ''):
            tokensFound.append([tempToken,tokenName])
            #print("token", tempToken, " tipo", previousName)
            #print(temp)
            temp = temp.replace(tempToken,'')
            #print(temp)
            if len(temp) == 1:
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
                        tempAcceptanceArray = []
                        for c in range(0,len(acceptanceArray)):
                            if acceptanceArray[c]:
                                tempAcceptanceArray.append(c)
                        index = min(tempAcceptanceArray)
                        previousName = get_key(index,precedence)
                        tokenName = get_key(index,precedence)
                        previousFound = True
                        previousAcceptance = True
                        tempToken = temp 
                    else:
                        previousName = get_key(foundArray.index(True),precedence)
                        previousFound = True
            
            elif len(temp) > 0:

                for j in range (0,len(precedence)):
                    found, acceptance = adfArray[j].simulation(temp[0])
                    if acceptance:
                        tokensFound.append([temp[0], adfArray[j].getName()])
                        break

                for j in range (0,len(precedence)):
                    found, acceptance = adfArray[j].simulation(temp[1])
                    if acceptance:
                        tokensFound.append([temp[1], adfArray[j].getName()])
                        break
                
                for j in range (0,len(precedence)):
                    found, acceptance = adfArray[j].simulation(temp)
                    if acceptance:
                        tokensFound.append([temp, adfArray[j].getName()])
                        break

                temp = ''
                    
        
        else:
            temp = ''

if True in foundArray:
    previousName = get_key(foundArray.index(True),precedence)
    tokensFound.append([temp,previousName])

for i in tokensFound:
    print(i)
    
