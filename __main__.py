from os import write
from EscrituraPy.fileWritter import *
from LecturaATG.fileReader import read_file
from converter import *
from AFDFixed.AFD import *


if __name__ == "__main__":
    archivo = input('Ingrese el nombre del archivo: ')
    characters, keywords, tokens, nameATG = read_file(archivo)
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
    """
    scanner.addParagraph(paragraph)

    
    print(".py escrito con exito")