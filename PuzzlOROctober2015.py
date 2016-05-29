# PuzzlOR October 2015 Racecar design


import operator

def calc_parts(config,scores):
    distanceCalc = 0
    for value in config:
        distanceCalc += scores[value]
    return distanceCalc

outputList = []
engines = ["AE","BE","CE"]
tires = ["AT","BT","CT"]
transmissions = ["ATR","BTR","CTR"]
brakes = ["AB","BB","CB"]
allConfiguration = ["AE","BE","CE","AT","BT","CT","ATR","BTR","CTR","AB","BB","CB"]

scores = {
"AE": 3,
"BE": 1,
"CE": 5,
"AT": 1,
"BT": 4,
"CT": 6,
"ATR": 7,
"BTR": 1,
"CTR": 2,
"AB": 7,
"BB": 7,
"CB": 1
}

for engine in engines:
    for tire in tires:
        for transmission in transmissions:
            for brake in brakes:
                config = [engine,tire,transmission,brake]
                outputList.append([config,calc_parts(config,scores)])
outputListSorted = sorted(outputList,key=operator.itemgetter(1))
print(outputListSorted[0])

