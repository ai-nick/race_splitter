import os

def setRaces(parties):
    heatDict = {}
    remain = parties%16
    heatDict['remainder'] = remain
    if (parties < 6):
        return heatDict
    if (5<parties):
        if(remain != 0):
            #diff = parties%heats
            heats = (parties//16) + 1
            diff = parties%heats
            for x in range(1, heats+1):
                if(x <= diff):
                    heatDict[x] = parties//heats +1
                else:
                    heatDict[x] = (parties//heats)
        else:
            heats = (parties//16)
            for x in range(1, heats+1):
                heatDict[x] = 16
    return heatDict

print(setRaces(7))
print(setRaces(111))
print(setRaces(360))
print(setRaces(46))
'''

def fixTestData():
    with open('test100.txt') as f:
        for line in f:
            print(line)
        
fixTestData()
'''
