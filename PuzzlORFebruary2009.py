# PuzzlOR February 2009 Supply & Demand
# $74,465 (or $90,000

import sys
import math
import operator
import itertools

def manhattan_distance(a,b):
    return sum([abs(a[i] - b[i]) for i in range(len(b))])

def generate_coordinate(value,alist):
    return [int(alist.index(value[0])) + 1,int(value[1])]
    
def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]

def main():
    xVal = ["A","B","C","D","E"]
    yVal = [1,2,3,4,5]
    area = generate_area(xVal,yVal)
    #1 km = $10, distance is in km

    factories = ["A1","A5","C3","E2"]
    towns = ["A4","B2","C4","E1","E5"]

    supplyData = {
    "A1":500,"A5":1000,"C3":1500,"E2":1000,"A4":-500,
    "B2":-2000,"C4":-500,"E1":-1500,"E5":-500
    }

    possibileArea = [i for i in area if i not in factories and i not in towns]
    possibleAreaCapacity = 1000

    c
