import math
import re
from rollDice import roll
from colr import color

from random import randrange
class mathParser:
    def __init__(self):
        allowDice = True
        allowMultiplication = True
        allowAddition = True
        allowSubtraction =True
        allowDivision = True
        allowExponents =True
        allowSqrRoot =  True
        allowAbsVal = True
        allowParenthisis = True
    def allowParenMult(self,string):
        string = ''.join(string.split())
        openSqrBrk = self.findOccurrences(string,"\(")
        indexFix = 0
        for brk in openSqrBrk:
            charBefore = string[brk+indexFix-1:brk+indexFix]
            #print(f"char{charBefore} tempString={tempString}")
            if(self.checkInt(charBefore)or charBefore==")"or charBefore=="]"):
                before =string[:brk+indexFix]
                after =string[brk+indexFix:]
                string=before+ "*"+after
                indexFix+=1
        return string

    def parseString(self,string,removeMFromMstring=True,shouldRound=True):
        
        mString = False
        restOfString = None
        if("!m" in string):
            mString=True
            if(removeMFromMstring):
                restOfString = string[:string.index("!m")]
            else:
                restOfString = string[:string.index("!m")+2]
            string = string[string.index("!m")+2:]
            #print(string)
        string =self.allowParenMult(string)
        dOccDict=self.findDice(string)
        #print(dOccDict)
        rolledString = self.replaceAndRollDice(string,dOccDict)
        #print(rolledString)
        if(mString==False):
            if(shouldRound):
                return(round(eval(rolledString)))
            else:
                 return(eval(rolledString))
        else:
            if(shouldRound):
                return(restOfString + str(round(eval(rolledString))))
            else:
                return(restOfString + str(eval(rolledString)))
    def replaceAndRollDice(self,string,dOccDict):
        fixIndex = 0
        for item in dOccDict:
            start=item["start"]
            end=item["end"]
            die =string[start+fixIndex:end+fixIndex+1]
            #print(die)
            result = str(sum(roll(die)))
            #print(f"result={result}")
            #print(die)
            tempstring = string[:start+fixIndex]+result+string[end+1+fixIndex:]
            fixIndex+=len(result)-len(die)
            string=tempstring
        return(string)
    def findDice(self,string):
        dOcc= self.findOccurrences(string,"d")
        dOccDict = []
        for d in dOcc:
            
            char = string[d]
            end = d
            start =d
            while char not in [" ", "(",")", "[", "*","+","/","-","^"] and end < len(string):
                end+=1
                if(end < len(string)):
                    char= str(string[end])
            char = d
            while char not in [" ", "(",")", "[", "*","+","/","-","^"] and start!=0:
                start+=-1
                char= string[start]
            end+=-1
            #print(start!=0 and char not in [" ", "(",")", "[", "*","+","/","-","^"])
            if(char not in [" ", "(",")", "[", "*","+","/","-","^"]):
                if(start!=0):
                    start+=1
            else:
                start+=1
            dOccDict.append({"start":start,"end":end})
        return(dOccDict)
    def findOccurrences(self,text,searchFor):
        arr = []
        #https://stackoverflow.com/questions/13009675/find-all-the-occurrences-of-a-character-in-a-string
        for m in re.finditer(searchFor, text):
            arr.append(m.start(0))
        return arr
    
    def checkInt(self,num):
        try:
            int(num)
        except:
            return False
        return True
  

