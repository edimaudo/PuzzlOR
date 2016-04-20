#PuzzlOR February 2010 Planet Colonisation
# area 19

import operator

def calc_distance(position,resources,positionData):
    distance = 0
    resourceData = []
    while len(resourceData) < 4:
        
       resources[position] 
    return [position,distance]

landingPosition = range(1,21)



resources = {
2:"energy",
7:"food",
8:"water",
12:"power",
14:"oxygen",
16:"water",
19:"oxygen",
20:"food",
}

#positionData = {
#1:[2],
#2:[3,10],
#3:[2,4,12],
#4:[3,5,14],
#5:[4,6],
#6:[5,7,15],
#7:[6,8,17],
#8:[7,9],
#9:[8,10,20],
#10:[2,9,11],
#11:[10,12,19],
#12:[3,11,13],
#13:[12,14,18],
#14:[4,13,15],
#15:[6,14,16],
#16:[15,17,18],
#17:[7,16,19,20],
#18:[13,16,19],
#19:[11,17,18,20],
#20:[9,17,19],
#}

positionData = {
1:[2,8,5],
2:[1,10,3],
3:[4,12,2],
4:[3,14,5],
5:[4,1,6],
6:[7,5,15],
7:[6,8,17],
8:[7,1,9],
9:[8,10,20],
10:[9,2,11],
11:[10,19,12],
12:[11,3,13],
13:[12,14,18],
14:[13,4,15],
15:[14,16,6],
16:[15,18,17],
17:[16,20,7],
18:[16,19,13],
19:[18,11,20],
20:[19,17,9]
}

distanceCalc = [calc_distance(position, resources, positionData) for position in landingPosition]
sorted_distance = sorted(distanceCalc,key=operator.itemgetter(1))
print(sorted_distance[0])
    
    
