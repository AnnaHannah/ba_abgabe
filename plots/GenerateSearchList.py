import sys
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import random
from _socket import close
from _operator import concat

# my files BAUSTELLE
import sys 

# try to find Modules RedBlackTree and Skiplist 
from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 
from fingerManagement.MinMaxFinger import *
from fingerManagement.LazyFinger import *

# Beispiel test fälle mit Listen

data_list = []
x = [1]
a = list(range(1,25))
b = list(range(1,50))
c = list(range(1,75))
d = list(range(1,100))
e = list(range(1,125))
f = list(range(1,150))
g = list(range(1,175))
h = list(range(1,200))

# verteilungen:

def make_oneNumber(list, number):
    res = []
    for i in list:
        res.append(number)
    return res

def make_zickzack(list):
    max = int(list[-1])
    res = []
    for i in list:
        if (i % 2 != 0):
           res.append(1) 
        else:
           res.append(max)  
    #print ("make_zickzack %r list lenght with list:" % str(len(res)+1),  res )
    return res

def make_oneCluster_left(list, x_spread):
    res = []
    for i in list:
        y = random.randrange(0, x_spread)
        res.append(y)
    return res
         
def make_oneCluster_right(list, x_spread):
    max = int(list[-1])
    res = []
    cluster_middle = (max - x_spread)
    for i in list:
        y = random.randrange(cluster_middle, max)
        res.append(y)
    return res

def make_oneCluster_middle(list, x_spread):
    res = []
    max = int(list[-1])
    list_middle = int(max//2 - x_spread)
    list_middle_limit = list_middle + 2*x_spread
    for i in list:
        y = random.randrange(list_middle, list_middle_limit)
        res.append(y)
    return res
    
def make_total_random(list):
    # Achtung, es macht nur Sinn nach Elementen zusuchen die auch da sind! => maximum der gegeben Listen ist größtest Elemeent
    res=[]
    max = int(list [-1])
    for i in list:
        y = random.randrange(0, max)
        res.append(y)
    return res

# --------------------------------------------------------------------------------

def makeBigLists(listOfList):
    print("\n1. Generating with makeBigLists - method is starting")
    ouput_list=[]
    print("2. ... ")
    # verarbeitung der Listen mit verteilungen 
    
    make_total_random(a)
    make_total_random(b)
    make_total_random(c)
    make_total_random(d)
    make_total_random(e)
    make_total_random(f)
    make_total_random(g)
    make_total_random(h) 
    
    # Beispiel um alle Listen anzuhängen 
    ouput_list.append(x) 
    ouput_list.append(a) 
    ouput_list.append(b) 
    ouput_list.append(c) 
    ouput_list.append(d)   
    ouput_list.append(e) 
    ouput_list.append(f) 
    ouput_list.append(g)
    ouput_list.append(h)
    print ("3. Generated number of sublists/Testcase is: ", len(ouput_list))     
    return ouput_list


# erstelle test csv file mit mini data listen:
def writeMYfile(filename, data):
    with open (filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter =',')
        writer.writerows(data)      
    print ("\n-> Done with writing data in", filename)
    

if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    print("\n -> Recursion allowed in this program:", sys.getrecursionlimit())
    
    #print(make_zickzack(a))
    #print(make_oneCluster_middle(a, 2))
    #print(make_total_random(a))
    print("\n Spample of list values :", make_total_random(a))
  
    
    # schreibe test1 csv mit datalisten:
    dataForCSV = makeBigLists(data_list)
    writeMYfile("searchLists.csv", dataForCSV) 
