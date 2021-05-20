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
    
    specialCharacters = {}
    special = {}
    specialCharacters.update({'C' : set([67]), 'H' : set([72]), 'R' : set([82]), '(' : set([40]), ')' : set([41]), '/' : set([47]), '.' : set([46]), "'" : set([39])})
    special.update({'C':'a', 'H':'b', 'R':'c', '(':'d', ')':'e', '/':'f', '.':'g', "'" :'h'})

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


    exceptions = ['while','do','if','switch']

    scanner = fileWritter(nameATG)
    scanner.writeImport('from AFDFixed.AFD import *')
    scanner.writeSentence('')
    scanner.writeSentence("exceptions = ['while','do','if','switch']")
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
    scanner.writeSentence("temp = ''")
    scanner.writeSentence('name = ""')
    scanner.writeSentence("previousName = ''")
    scanner.writeSentence("previousAcceptance = ''")
    scanner.writeSentence("found = False")
    scanner.writeSentence("tokensFound = []")
    scanner.writeSentence("#text = 'ho(la  10 123dsa2 sad as ads32 93r 2( sa0d ] &  + s  +  ==1 1 ?823?'")
    scanner.writeSentence('f = open("tareas.txt", "r")')
    scanner.writeSentence('text = f.read()')
    scanner.writeFor('for i in text:')
    scanner.writeSentence('temp = temp + i')
    scanner.writeFor('for j in range (0,len(adfArray)):')
    scanner.writeSentence('found, acceptance, name= adfArray[j].simulation(temp)')
    scanner.writeIf('if found:')
    scanner.writeSentence('previousName = name')
    scanner.writeSentence('previousAcceptance = acceptance')
    scanner.writeSentence('break')
    scanner.substractTab()
    scanner.writeIf('else:')
    scanner.writeIf('if not(j == len(adfArray)-1):')
    scanner.writeSentence('pass')
    scanner.substractTab()
    scanner.writeIf('else:')
    scanner.writeSentence('temp = temp[:len(temp)-1]')
    scanner.writeIf("if not(previousName == '') and not(previousAcceptance == ''):")
    scanner.writeSentence('tokensFound.append((temp,previousName))')
    scanner.substractTab()
    scanner.writeSentence("previousName = ''")
    scanner.writeSentence('temp = i')
    scanner.writeFor('for k in adfArray:')
    scanner.writeSentence('found, acceptance, name= k.simulation(temp)')
    scanner.writeIf('if found:')
    scanner.writeSentence('previousName = name')
    scanner.writeSentence('previousAcceptance = acceptance')
    scanner.writeSentence('break')
    scanner.substractTab()
    scanner.substractTab()
    scanner.writeIf('if found:')
    scanner.writeSentence('break')
    scanner.substractTab()
    scanner.substractTab()
    scanner.substractTab()
    scanner.substractTab()
    scanner.substractTab()
    scanner.writeIf('if acceptance:')
    scanner.writeSentence('tokensFound.append((temp,name))')
    scanner.substractTab()
    scanner.writeFor('for i in range(0, len(tokensFound)):')
    scanner.writeSentence('temp = list(tokensFound[i])')
    scanner.writeIf('if temp[0] in exceptions:')
    scanner.writeSentence('index = exceptions.index(temp[0])')
    scanner.writeSentence('temp[0] = exceptions[index]')
    scanner.writeSentence('temp[1] = exceptions[index]')
    scanner.writeSentence('tokensFound[i] = temp')
    scanner.substractTab()
    scanner.substractTab()
    scanner.writeFor('for i in tokensFound:')
    scanner.writeSentence('print(i)')
    scanner.substractTab()
    scanner.writeSentence('#print(tokensFound)')

    print(".py escrito con exito")