#Scanner created with HexNumber.ATG data
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
precedence = {'ident': 0, 'hexnumber': 1, 'number': 2, 'signnumber': 3, 'whitetoken': 4, 'ANY': 5}

adfArray = []
ident= 'ident'
temp = AFD(ident)
tempidentAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempidentAcceptance)
tempidentTransitions = {0: {1: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}]}, 1: {1: {48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}}}

temp.setTransition(tempidentTransitions)
adfArray.append(temp)
hexnumber= 'hexnumber'
temp = AFD(hexnumber)
temphexnumberAcceptance = {0: False, 1: False, 2: True}

temp.setDictAcceptance(temphexnumberAcceptance)
temphexnumberTransitions = {0: {1: [{65, 66, 67, 68, 69, 70, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: [{65, 66, 67, 68, 69, 70, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57}], 2: [{72}]}}

temp.setTransition(temphexnumberTransitions)
adfArray.append(temp)
number= 'number'
temp = AFD(number)
tempnumberAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempnumberAcceptance)
tempnumberTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempnumberTransitions)
adfArray.append(temp)
signnumber= 'signnumber'
temp = AFD(signnumber)
tempsignnumberAcceptance = {0: False, 1: False, 2: True}

temp.setDictAcceptance(tempsignnumberAcceptance)
tempsignnumberTransitions = {0: {1: [{45}], 2: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {2: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 2: {2: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempsignnumberTransitions)
adfArray.append(temp)
whitetoken= 'whitetoken'
temp = AFD(whitetoken)
tempwhitetokenAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempwhitetokenAcceptance)
tempwhitetokenTransitions = {0: {1: [{9, 10, 13}]}, 1: {1: [{9, 10, 13}]}}

temp.setTransition(tempwhitetokenTransitions)
adfArray.append(temp)
ANY= 'ANY'
temp = AFD(ANY)
tempANYAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempANYAcceptance)
tempANYTransitions = {0: {1: [{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255}]}}

temp.setTransition(tempANYTransitions)
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
            previousToken = temp
        else:
            try:
                previousName = get_key(acceptanceArray.index(True),precedence)
                previousFound = True
                previousAcceptance = False
            except:
                pass

    else:
        
        if previousFound and not(previousName == ''):
            tokensFound.append([previousToken,previousName])

            found = False
            previousName = ''

            for k in range (0,len(precedence)):
                foundArray[k] = None

            for k in range (0,len(precedence)):
                acceptanceArray[k] = None

            temp = temp.replace(previousToken,'')

            for l in range (0,len(adfArray)):
                found, acceptance = adfArray[l].simulation(temp)
                foundArray[l] = found
                acceptanceArray[l] = acceptance

            if True in foundArray:
                if True in acceptanceArray:
                    previousName = get_key(acceptanceArray.index(True),precedence)
                    previousFound = True
                    previousAcceptance = True
                    previousToken = temp
                else:
                    try:
                        previousName = get_key(acceptanceArray.index(True),precedence)
                        previousFound = True
                        previousAcceptance = False
                    except:
                        pass

            else:
                temp = ''
            
        else:
            temp = ''

if True in foundArray and not(previousName == ''):
    previousName = get_key(foundArray.index(True),precedence)
    tokensFound.append([temp,previousName])

with open('tokens.txt', 'w') as temp_file:
    for item in tokensFound:
        temp_file.write("%s\n" % item)

print("Documento con tokens escrito con exito")

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.pos_token = 0
        self.actual_token = tokens[self.pos_token]
        self.last_token = ''
    
    def getType(self, token):
        try:
            return token[1]
        except:
            return token

    def getValue(self, token):
        try:
            return token[0]
        except:
            return token
    
    def advance(self):
        self.pos_token += 1
        if self.pos_token < len(self.tokens):
            self.actual_token = self.tokens[self.pos_token]
            self.last_token = self.tokens[self.pos_token -1]
    
    def read (self, value, typeToken = False, end = False):
        if typeToken:
            if self.getType(self.actual_token) == value:
                self.advance()
                return True
            else:
                print("Ha ocurrido un error")
                return False
        else:
            if self.getValue(self.actual_token) == value:
                self.advance()
                return True
            else:
                if end:
                    print("Ha ocurrido un error")
                return False
                
    def hextofloat(self,value):
        value = value[:len(value)-1]
        newvalue = 0 
        for n in range(0,len(value)):

            exp = len(value)-(n+1)
            if value[n] in ["A", "B", "C", "D", "E", "F"]:
                if value[n] == "A":
                    newvalue = newvalue + (10 * (16**exp))
                if value[n] == "B":
                    newvalue = newvalue + (11 * (16**exp))
                if value[n] == "C":
                    newvalue = newvalue + (12 * (16**exp))
                if value[n] == "D":
                    newvalue = newvalue + (13 * (16**exp))
                if value[n] == "E":
                    newvalue = newvalue + (14 * (16**exp))
                if value[n] == "F":
                    newvalue = newvalue + (15 * (16**exp))

            else:
                newvalue = newvalue + (int(value[n]) * (16**exp))

        print(value," se convierte en ", newvalue)
        return newvalue
    
    
    def Expr(self):

        while self.getType(self.actual_token) in ["number","decnumber","hexnumber"] or self.getValue(self.actual_token) in ["-","("]:
            print("Resultado: ", self.Stat())
            self.read(";", False, True)
        self.read(".", False, True)
            
    def Stat(self):

        value = 0
        value = self.Expression(value)
        return value
            
    def Expression(self, result):

        result1, result2 = 0,0
        result1 = self.Term(result1)

        while self.getValue(self.actual_token) in ["-","+"]:

            if self.getValue(self.actual_token) == "-":
                self.read('-', False, True)
                result2 = self.Term(result2)
                result1-=result2

            if self.getValue(self.actual_token) == "+":
                self.read('+', False, True)
                result2 = self.Term(result2)
                result1+=result2

        result = result1

        return result
            
    def Term(self, result):
        result1, result2 = 0, 0
        result1 = self.Factor(result1)

        while self.getValue(self.actual_token) in ["*", "/"]:

            if self.getValue(self.actual_token) == "/":
                self.read("/", False, True)
                result2 = self.Factor(result2)
                result1/=result2

            if self.getValue(self.actual_token) == "*":
                self.read("*", False, True)
                result2 = self.Factor(result2)
                result1/=result2

        result = result1

        return result
            
    def Factor(self, result):
        signo = 1

        if self.getValue(self.actual_token) == '-':
            self.read('-', False, True)
            signo = -1

        elif self.getValue(self.actual_token) == '(':
            self.read('(', False, True)
            result = self.Expression(result)
            self.read(')', False, True)

        elif self.getType(self.actual_token) == 'number':
            self.read('number', True, True)
            result = self.Number(result)

        elif self.getType(self.actual_token) == 'decnumber':
            self.read('decnumber', True, True)
            result = self.Number(result)

        elif self.getType(self.actual_token) == 'hexnumber':
            self.read('hexnumber', True, True)
            result = self.Number(result)
        
        result*=signo
        return result

            
    def Number(self, result):

        if self.getType(self.actual_token) == 'number':
            self.read('number',True, True)
            
        if self.getType(self.actual_token) == 'decnumber':
            self.read('decnumber',True, True)

        if self.getType(self.actual_token) == 'hexnumber':
            self. read('hexnumber', True, True)

        try:
            result = float(self.getValue(self.last_token))
        except:
            result = self.hextofloat(self.getValue(self.last_token))

        return result
            
parser = Parser(tokensFound)
parser.Expr()
    
