#author @AuthoredEntropy
import random
import math
def higher(a, b):
      
    if a >= b:
        return a
    else:
        return b
def roll(dice, takeAver = False, trueAverage=False, takeAdv=False):
    if(takeAdv):
        if( "d" in str(dice)):
            tempArr = dice.split("d")
            diceType =int(tempArr[1])
            numOfDice =int(tempArr[0])
            diceRolls = []
            for x in range(numOfDice):
                roll1=random.randint(1,diceType)
                roll2=random.randint(1,diceType)
                diceRolls.append(higher(roll1,roll2))
            return(diceRolls)
    elif(takeAver == False):
        if( "d" in str(dice)):
            tempArr = dice.split("d")
            diceType =int(tempArr[1])
            numOfDice =int(tempArr[0])
            diceRolls = []
            for x in range(numOfDice):
                diceRolls.append(random.randint(1,diceType))
            return(diceRolls)
    elif(trueAverage == False):
        if( "d" in str(dice)):
            tempArr = dice.split("d")
            diceType =int(tempArr[1])
            numOfDice =int(tempArr[0])
            adv = math.ceil((diceType + 1)/2)
            return(adv*numOfDice)
    else:
        if( "d" in str(dice)):
            tempArr = dice.split("d")
            diceType =int(tempArr[1])
            numOfDice =int(tempArr[0])
            adv = math.ceil((diceType/2))
            return(adv*numOfDice)


def testBalance(tests=[{"num":10000,"type":6}]):
    allTypes = []
    for test in tests:
        allTypes.append(test["type"])
    maxDiceType = max(allTypes)
    allNumbers = []    
    for test in tests:
        for x in range (test["num"]):
            allNumbers.append(sum(roll("1d"+str(test["type"]))))
            
    for num in allNumbers:
        try:
            exec(f"x{num} +=1")
        except NameError:
            exec(f"x{num} = 1")
    results = []
    for x in range(maxDiceType+1):
        if(x != 0):
            try:
                exec(f"results.append(\"{x} =\"+str(x{x}))")
            except NameError:
                exec(f"x{x}=0")
                exec(f"results.append(\"{x} =\"+str(x{x}))")
    return results
def getAverageBalance(tests=[{"num":10000,"type":6}]):
    results = []
    condensedDict = {}
    for test in tests:
        for x in range(test["type"]+1):
            if(x != 0):
                try:
                    condensedDict[x] += (test["num"]/test["type"])
                except KeyError:
                    condensedDict[x] = (test["num"]/test["type"])
    workaround = "type"
    workaround2 = "num"
    x =1
    for item in condensedDict:
        results.append(f"{x}={str(round(condensedDict[x], 3))}")
        x+=1
    return results
def getTotalRolls(tests=[{"num":10000,"type":6}]):
    total = 0
    for test in tests:
        total += int(test["num"])
    return total