def createProductions(productionsList):
    
    productions = []
    text = ''

    for i in productionsList:
        if i == '.':
            text = text + i + '\n'
            productions.append(text)
            text = ''
            
        else:
            text = text + i + '\n'
    
    productionsDef = {}
    for i in range (0,len(productions)):
        productions[i] = productions[i].replace('\t','\n')
        index = productions[i].find('=')
        name = productions[i][0:index-1].strip()
        if "<" in name:
            index = name.find("<")
            name = name[:index]
        productionsDef.update({name:None})
    
    productions = fill_productions(productionsDef)
    return productions

def fill_productions(productionsNames):
    for i in productionsNames:
        if i == 'Expr':
            #print()
            paragraph="""    def Expr(self):

        while self.getType(self.actual_token) in ["number","decnumber","hexnumber"] or self.getValue(self.actual_token) in ["-","("]:
            print("Resultado: ", self.Stat())
            self.read(";", False, True)
        self.read(".", False, True)
            """
            productionsNames.update({i:paragraph})

        if i == 'Stat':
            #print()
            paragraph="""    def Stat(self):

        value = 0
        value = self.Expression(value)
        return value
            """
            productionsNames.update({i:paragraph})

        if i == 'Expression':
            #print()
            paragraph="""    def Expression(self, result):

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
            """
            productionsNames.update({i:paragraph})
        if i == 'Term':
            #print()
            paragraph="""    def Term(self, result):
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
            """
            productionsNames.update({i:paragraph})
        if i == 'Factor':
            #print()
            paragraph="""    def Factor(self, result):
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

            """
            productionsNames.update({i:paragraph})
        if i == 'Number':
            #print()
            paragraph="""    def Number(self, result):

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
            """
            productionsNames.update({i:paragraph})
    #print(productionsNames)
    return productionsNames