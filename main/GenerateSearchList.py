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
import logging

# Beispiel test fälle mit Listen

data_list = []
#x = [1]
a = list(range(1,25))
b = list(range(1,50))
c = list(range(1,75))
d = list(range(1,100))
e = list(range(1,125))
f = list(range(1,150))
g = list(range(1,175))
h = list(range(1,200))

k = list(range(1,225))
l = list(range(1,250))
m = list(range(1,275))
n = list(range(1,300))
o = list(range(1,325))
p = list(range(1,350))
q = list(range(1,375))
r = list(range(1,400))


# a = list(range(1,2500))
# b = list(range(1,5000))
# c = list(range(1,7500))
# d = list(range(1,10000))
# e = list(range(1,12500))
# f = list(range(1,15000))
# g = list(range(1,17500))
# h = list(range(1,20000))
#
# k = list(range(1,22500))
# l = list(range(1,25000))
# m = list(range(1,27500))
# n = list(range(1,30000))
# o = list(range(1,32500))
# p = list(range(1,35000))
# q = list(range(1,37500))
# r = list(range(1,40000))


def make_oneNumber(list):
    number = (list[-1])//2
    res =[]
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
    #print (" make_oneCluster_right %r list lenght with list:" % str(len(res)+1),  res )
    #print (res)
    return res


def make_oneCluster_right(list):
    x_spread = int(len(list) * 0.2)
    #print(x_spread)
    max = int(list[-1])
    res = []
    cluster_middle = (max - x_spread)
    for i in list:
        y = random.randrange(cluster_middle, max)
        res.append(y)
    #print (res)
    return res

def make_oneCluster_middle(list):
    x_spread = int(len(list) * 0.1)
    res = []
    max = int(list[-1])
    list_middle = int(max//2 - x_spread)
    list_middle_limit = list_middle + 2*x_spread
    for i in list:
        y = random.randrange(list_middle, list_middle_limit)
        res.append(y)
        # print (res)
    return res

def make_random(list):
    # Achtung, es macht nur Sinn nach Elementen zusuchen die auch da sind! => maximum der gegeben Listen ist größtest Elemeent
    res=[]
    max = int(list [-1])
    for i in list:
        y = random.randrange(1, max)
        res.append(y)
    # print (res)
    return res

# --------------------------------------------------------------------------------

def makeBigLists(listOfList):
    print("\n1. Generating with makeBigLists - method is starting")
    ouput_list=[]
    print("2. ... ")
    # verarbeitung der Listen mit verteilungen

    a_new = make_oneCluster_right(a)
    b_new = make_oneCluster_right(b)
    c_new = make_oneCluster_right(c)
    d_new = make_oneCluster_right(d)
    e_new = make_oneCluster_right(e)
    f_new = make_oneCluster_right(f)
    g_new = make_oneCluster_right(g)
    h_new = make_oneCluster_right(h)

    k_new = make_oneCluster_right(k)
    l_new = make_oneCluster_right(l)
    m_new = make_oneCluster_right(m)
    n_new = make_oneCluster_right(n)
    o_new = make_oneCluster_right(o)
    p_new = make_oneCluster_right(p)
    q_new = make_oneCluster_right(q)
    r_new = make_oneCluster_right(r)

    # Logging for easy study
    logging.info("\n first list is logged here:")
    logging.info ("\n a_new = % r" % a_new)

    # Beispiel um alle Listen anzuhängen
    #ouput_list.append(x)

    ouput_list.append(a_new)
    ouput_list.append(b_new)
    ouput_list.append(c_new)
    ouput_list.append(d_new)
    ouput_list.append(e_new)
    ouput_list.append(f_new)
    ouput_list.append(g_new)
    ouput_list.append(h_new)

    ouput_list.append(k_new)
    ouput_list.append(l_new)
    ouput_list.append(m_new)
    ouput_list.append(n_new)
    ouput_list.append(o_new)
    ouput_list.append(p_new)
    ouput_list.append(q_new)
    ouput_list.append(r_new)


    print ("2. Sample of first list:",  a_new[0:20])
    print ("3. Generated number of sublists/Testcase is: ", len(ouput_list))
    return ouput_list


# erstelle test csv file mit mini data listen:
def writeMYfile(filename, data):
    with open (filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter =',')
        writer.writerows(data)
    print ("\n-> Done with writing data in", filename)


if __name__ == "__main__":
    logging.basicConfig(filename='logFILE-GenerateSearchLists.log', encoding='utf-8', level=logging.DEBUG)
    logging.info("\n -> Recursion allowed in this program: %r" % sys.getrecursionlimit())

    sys.setrecursionlimit(3000)
    print("\n -> Recursion allowed in this program:", sys.getrecursionlimit())
    #print( make_oneCluster_right(a))
    #print(make_oneCluster_middle(b, 2))
    #print(make_oneCluster_right(a))
  
    
    # schreibe test1 csv mit datalisten:
    dataForCSV = makeBigLists(data_list)
    writeMYfile("searchLists.csv", dataForCSV) 
