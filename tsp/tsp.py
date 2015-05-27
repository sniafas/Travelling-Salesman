#!/usr/bin/env python

import itertools, time
import numpy as np, fileinput, math
from numpy import loadtxt

def menu():

	print "1-> Standard Trip (autoload 'matrix.txt') "
	print "2-> Custom Trip  "

	print "0-> exit "

	return None

def tsp(cities):

    mintrip = 1000
    start = 0 #town A as 0

    node = []
    for i in range(len(cities)-1): node.append(i+1) ## create trips
    trip = list(itertools.permutations(node))       ## find all possible trips


    ### len(trip)/2 === math.factorial( (len(cities)-1))/2 ### isodunama
    for permute in range( len(trip)/2 ):        ## start travelling excluding double trips

        ctrip = 0
        town = 0

        #print "*************-------******"
        #print "Trip " + str(permute+1)
        #print "*************-------******"
        for town in range(len(node)-1):

            ctrip = cities[ trip[permute][town] ][ trip[permute][town+1]  ] + ctrip
             #print "Town" + str(town) + "->" + "Town" + str(town+1) + ":" + str(ctrip)

        ctrip = ctrip + cities[ trip[permute][town+1] ][start] + cities[start][ trip[permute][start] ]

        #print "Total Distance for trip " + str(permute+1) + ": " + str(ctrip) + "\n"
        if ctrip < mintrip:
            mintrip = ctrip
            bestrip = trip[permute]

    #print "*************************\n"
    #print cities
    print "There are " + str(math.factorial((len(cities)-1))/2) + " alternative trips\n"
    #print trip[:math.factorial((len(cities)-1))/2]

    #print "*************************\n"
    #print "Shortest trip is:" + str((start,) + bestrip + (start,))
    #print "Distance:" + str(mintrip) + "km"


if __name__ == '__main__':


    menu()

    choice = raw_input('\n->')

    if (choice==str(1)):

        cities = loadtxt("matrix.txt", delimiter=",", unpack=False)
        t0 = time.time()
        tsp(cities)
        print time.time() - t0, "seconds process"

    elif(choice==str(2)):           # random trip

        nodes = raw_input('Enter Number of Cities->')

        cities = np.random.randint(100, size=( int(nodes), int(nodes) )) ## random cities


        for k in range(len(cities)): cities[k][k] = 0           ## diagonios 0
        cities = np.tril(cities) + np.tril(cities, -1).T        ## city trip symmetry

        t0 = time.time()
        tsp(cities)
        print time.time() - t0, "seconds process"

    elif(choice==str(0)): sys.exit(0)
