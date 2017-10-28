# PuzzlOR August 2008 Markov Prison

#1,5,6,10,11,12,16, 0.4712


import random
import numpy as np 
from scipy import stats as st

import scipy as sp

def prison_route():
    #do something
    

def main():
    #do something

if __name__ == "__main__":
    main()

# import random
# from bisect import bisect
# import numpy as np
# from scipy import stats as st
# import scipy as sp


# def weighted_choice(choices):
#     values, weights = zip(*choices)
#     total = 0
#     cum_weights = []
#     for w in weights:
#         total += w
#         cum_weights.append(total)
#     x = random.random() * total
#     i = bisect(cum_weights, x)
#     return values[i]

# def generate_random(alist):
#     return random.randint(0,len(alist)-1)

# def prisoner_move(position,prison):
    
#     tempList = prison[position]
#     tempValue = max(tempList)
#     return tempValue#tempList[tempValue]

# def guard_move(position,prison,guardData):
#     output = weighted_choice(guardData)
#     if output == "North":
#         tempval = 0
#     elif output == "South":
#         tempval = 1
#     elif output == "East":
#         tempval = 2
#     else:
#         tempval = 3
#     nextMoves = prison[position]
#     nextMove = nextMoves[tempval]
#     if nextMove == 0:
#         nextMove = position
#     return nextMove

# def main():
#     prison = {
#     1:[0,5,0,2],
#     2:[0,6,3,1],
#     3:[0,7,4,2],
#     4:[0,8,0,3],
#     5:[1,9,6,0],
#     6:[2,10,7,5],
#     7:[3,11,8,6],
#     8:[4,12,0,7],
#     9:[5,13,10,0],
#     10:[6,14,11,9],
#     11:[7,15,12,10],
#     12:[8,16,0,11],
#     13:[9,0,14,0],
#     14:[10,0,15,13],
#     15:[11,0,16,14],
#     16:[12,0,0,15]
#     }
    
#     prison_route = {
#     1:[5,2],
#     2:[6,3,1],
#     3:[7,4,2],
#     4:[8,3],
#     5:[1,9,6],
#     6:[2,10,7,5],
#     7:[3,11,8,6],
#     8:[4,12,7],
#     9:[5,13,10],
#     10:[6,14,11,9],
#     11:[7,15,12,10],
#     12:[8,16,11],
#     13:[9,14],
#     14:[10,15,13],
#     15:[11,16,14],
#     16:[12,15]
#     }
    
#     guard1_data = [("North",20),("South",40),("East",20),("West",20)]
#     guard2_data = [("North",40),("South",10),("East",20),("West",30)]

#     countval = 0
#     maxcountval = 10000
#     outcome = []
#     escape_Route = []
#     while countval < maxcountval:
#         prisoner_Position = []
#         guard1_Position = []
#         guard2_Position = []
#         chase_End = False
#         prisoner = 1
#         guard1 = 16
#         guard2 = 16
#         while not chase_End:
#             if prisoner == guard1 or prisoner == guard2:
#                 outcome.append("caught")
#                 chase_End = True
#                 break
#             elif prisoner == 16:
#                 prisoner_Position.append(16)
#                 escape_Route.append(prisoner_Position)
#                 outcome.append("escaped")
#                 chase_End = True
#                 break
#             else:
#                 if prisoner not in prisoner_Position:
#                     prisoner_Position.append(prisoner)
#                     prisoner = prisoner_move(prisoner,prison_route)
#                 if guard1 not in guard1_Position:
#                     guard1 = guard_move(guard1,prison,guard1_data)
#                 if guard2 not in guard2_Position:
#                     guard2 = guard_move(guard2,prison,guard2_data)
#         countval +=1

#     print("Caught: " + str(len([value for value in outcome if value == "caught"])))
#     print("Escaped: " +  str(len([value for value in outcome if value == "escaped"])))
#     print(escape_Route[0:5])

# if __name__ == "__main__":
#     main()