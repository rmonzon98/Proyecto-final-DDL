from os import write
from EscrituraPy.fileWritter import *
from LecturaATG.fileReader import read_file
from converter import *
from Productions.Productions import *
from AFDFixed.AFD import *


if __name__ == "__main__":
    archivo = input('Ingrese el nombre del archivo: ')
    characters, keywords, tokens, productions, nameATG = read_file(archivo)
    print("-"*40,nameATG,"-"*40)
    print("Characters:")
    for i in characters:
        print(chr(9)+i)
    print("Keywords:")
    for i in keywords:
        print(chr(9)+i)
    print("Tokens:")
    for i in tokens:
        print(chr(9)+i)
    print("Productions:")
    for i in productions:
        print(chr(9)+i)
    
    print("")
    print("")

    print("Escribiendo .py")

    charactersDict = createCharactersDict(characters)
    #print('charactersDict',charactersDict)
    KeywordsDict = createKeywordsDict(charactersDict,keywords)
    #print('KeywordsDict',KeywordsDict)
    tokensDict, exceptions = createTokensDict(charactersDict, tokens)
    #print('tokensDict',tokensDict)
    tokensArray = functionsCreator(tokensDict, charactersDict)
    
    print("Escribiendo listas de characters, keywords y tokens")

    adfArray = []
    for i in tokensArray:
        name = i.getName()
        temp = AFD(name)
        acceptanceDict = i.getAcceptance()
        temp.setDictAcceptance(acceptanceDict)
        transitionsDict = i.getTransitions()
        temp.setTransition(transitionsDict)
        adfArray.append(temp)
    
    for i in tokensArray:
        i.unifyTransitions()
        i.deleteNulls()
    
    precedence = {}
    for i in range (0,len(tokensArray)):
        name = tokensArray[i].getName()
        precedence.update({name:i})
    #print(precedence)

    print("Automatas generados")

    exceptions = ['while','do','if','switch']

    
    scanner = fileWritter(nameATG)
    scanner.writeImport('from AFDFixed.AFD import *')
    scanner.writeSentence('')
    paragraph="""def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "key doesn't exist"

def isHigher(val1, val2):
    if val1 < val2:
        return True
    else:
        return False
    """
    scanner.addParagraph(paragraph)
    scanner.writeSentence('')
    scanner.writeSentence("exceptions = ['while','do','if','switch']")
    scanner.writeSentence('')
    scanner.addDict("precedence", precedence)
    adfArray = []
    scanner.writeSentence('adfArray = []')
    print("Escribiendo automatas")
    for i in tokensArray:
        name = i.getName()
        scanner.addString(name, name)
        temp = AFD(name)
        scanner.writeSentence('temp = AFD('+name+')')
        acceptanceDict = i.getAcceptance()
        temp.setDictAcceptance(acceptanceDict)
        scanner.writeEnter()
        scanner.addDict('temp'+name+'Acceptance',acceptanceDict)
        scanner.writeSentence('temp.setDictAcceptance('+'temp'+name+'Acceptance'+')')
        scanner.writeEnter()
        transitionsDict = i.getTransitions()
        scanner.addDict('temp'+name+'Transitions',transitionsDict)
        temp.setTransition(transitionsDict)
        scanner.writeSentence('temp.setTransition('+'temp'+name+'Transitions'+')')
        adfArray.append(temp)
        scanner.writeSentence('adfArray.append(temp)')
    scanner.substractTab() 
    scanner.writeSentence('')
    paragraph = """f = open("tareas.txt", "r")
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
        temp_file.write("%s"""
    paragraph = paragraph + chr(92) + 'n" % item)'
    scanner.addParagraph(paragraph)
    scanner.writeSentence('print("Documento con tokens escrito con exito")')
    scanner.writeSentence('')
    scanner.writeSentence('')
    print("Se inicia a escribir la clase parser dentro del .py")
    print("Se crean las productions")
    paragraph = """class Parser:
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
    
    """
    scanner.addParagraph(paragraph)
    productions = createProductions(productions)
    for i in productions:
        scanner.addParagraph(productions.get(i))
    paragraph= """parser = Parser(tokensFound)
parser.Expr()
    """
    scanner.addParagraph(paragraph)

    
    print(".py escrito con exito")