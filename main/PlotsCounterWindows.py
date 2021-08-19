import numpy as np
import matplotlib.pyplot as plt
import csv
from numpy.core.arrayprint import IntegerFormat
from fileinput import filename
import time 
from datetime import timedelta
import datetime
from numpy.core.defchararray import isdigit, isdecimal, isnumeric
from decimal import Decimal  
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from _socket import close
from _operator import concat
from matplotlib.pyplot import title
from unicodedata import numeric
from numpy import double
import logging
import copy
import sys


# try to find Modules RedBlackTree and Skiplist 
from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 
from fingerManagement.MinMaxFinger import *
from fingerManagement.LazyFinger import *
from fingerManagement.BinarySplayTree import *

# Ziel der funktion, file öffnen, alle Listen auslesen, alle stringsauslesen und in INT convertieren, 
# Liste von Listen zurückgeben
def readMYfile(filename):
    with open( filename) as csv_file:
        reader=csv.reader (csv_file, delimiter=',', skipinitialspace=True)
        
        output_list =[]
        line_count = 0
        
        for line in reader:
            new_list = []
            new_list.append(line)
            # entfernen von extra klammern
            simple_list = new_list.pop()
            # Alle string in liste zu INTEGER
            for i in range(0, len(simple_list)):
                simple_list[i]= int(simple_list[i])
            output_list.append(simple_list)
            
            line_count +=1
        #print("\n -> Done reading File: ", filename)
        return output_list


def map_lists(in_listOfLists, se_listOfLists, func):
    result = []
    while len(in_listOfLists) > 0 and len(se_listOfLists) > 0:
        # always use first element
        x = in_listOfLists.pop(0)
        y = se_listOfLists.pop(0)
        
        z = func(x, y)
        result.append(z)
    return result

def subListLengh(listOfLists):
    lenSublist_Output = [] 
    for list in listOfLists:
        lenSublist_Output.append(len(list))
    #print ("the lenght of every SubList in ListOfLists is", lenSublist_Output)
    return lenSublist_Output 

def messureTime_INSERT_RedBlackTree (inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    #start timer
    # start_time = time.monotonic()
    bst = RedBlackTree()
    start = time.perf_counter_ns()
    # init für Blackred tree
    
    bst.insertMultipleElem(inputList)
    
    # End Timer 
    end  = time.perf_counter_ns()
    delta_time = 0
    delta_time = (int(end-start)/(100000))
    return int(delta_time)

def messureTime_INSERT_SkipList(inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    #start timer
    delta_time = 0
    skl = SkipList()
    #start_time = time.monotonic()
    start = time.perf_counter_ns()
    # init für Skiplist tree
   
    skl.insertMultipleElem(inputList)
    
    # End Timer
    end = time.perf_counter_ns()
    delta_time = (int(end-start)//(100000))
    return (int(delta_time))

def messureNodes_SEARCH_RedBlackTree(inputList, searchlist):
    # formale sache
    if type(inputList) != list:
        inputList = inputList.tolist()
    if type(searchlist) != list:
        searchlist = searchlist.tolist()    
   
   # init für Tree und Finger
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)
    
    # Messen
    x = bst.usedNodesInSearch

    # Aktion
    bst.findMultipleElem(searchlist)
    x = bst.usedNodesInSearch

    return int(x)

def messureNodes_MinMaxFingerSEARCH_RedBlackTree(inputList, searchlist):
    # formale sache
    if type(inputList) != list:
        inputList = inputList.tolist()
    if type(searchlist) != list:
        searchlist = searchlist.tolist()  
    
    # init für Tree und Finger
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)
    mmf = MinMaxFinger()
    mmf.maxiFinger = mmf.setMaxiFingerFrom(bst)
    mmf.miniFinger = mmf.setMiniFingerFrom(bst)
    # Aktion  
    mmf.findMultipleElem_with_MinMaxFinger(bst, searchlist)

    # Messen
    x = (bst.usedNodesInSearch + mmf.usedNodesInSearch)
    return int(x)

def messureNodes_LAZYFingerSEARCH_RedBlackTree(inputList, searchlist):
    # formale sache
    if type(inputList) != list:
        inputList = inputList.tolist()
    if type(searchlist) != list:
        searchlist = searchlist.tolist()  
    
   # init für Tree und Finger
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)
    lf = LazyFinger()
    lf.LazyFinger = lf.setfirst_LazyFinger(bst)
    
    # Aktion  
    lf.findMultipleElem_with_LazyFinger(bst, searchlist)
    
    # Messen
    x = (bst.usedNodesInSearch + lf.usedNodesInSearch)
    return (x)

def messureNodes_SPLAYFingerSEARCH_RedBlackTree(inputList, searchlist):
        # formale sache
    if type(inputList) != list:
        inputList = inputList.tolist()
    if type(searchlist) != list:
        searchlist = searchlist.tolist() 
    
    # init für Tree und Finger
    inputSplay = copy.deepcopy(inputList)
    print(len(inputSplay))

    splay = BinarySplayTree()
    splay.insertMultipleElem(inputSplay) 

    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)

    # Aktion
    splay.findMultipleElem_with_SplayTree(bst, searchlist)
    
    # Messen
    x = (bst.usedNodesInSearch + splay.usedNodesInSearch)
    print ("messureNodes_SPLAYFingerSEARCH_RedBlackTree: usedNodesInSearch (bst+splay)", x)
    return (x)


def timePerformanceINSERTRedBlackTree(listOfLists):
    perf_OutputList = []   
    for list in listOfLists:
        timeRBT = messureTime_INSERT_RedBlackTree(list)
        perf_OutputList.append(timeRBT)

    print ("timePerformanceINSERTRedBlackTree will return:", perf_OutputList)
    return perf_OutputList

# def timePerformanceINSERTSkipList(listOfLists):
    # perf_OutputList = []   
    # for list in listOfLists:
        # timeSKL = messureTime_INSERT_SkipList(list)
        # perf_OutputList.append(timeSKL)
    # print ("timePerformanceINSERTSkipList has messured time pro list iteration, and will return:", perf_OutputList)
    # return perf_OutputList

def PerformanceSEARCHRedBlackTree(input_listOfLists, search_listOfLists):
    res = map_lists(input_listOfLists, search_listOfLists, messureNodes_SEARCH_RedBlackTree)
    out = []
    se = readMYfile('searchLists.csv')
    # print(se)
    while len(res) > 0 and len(se) > 0:
        a = res.pop(0)
        b = (se.pop(0))
        if type(b) == list:
            b = len(b)
        if b != 0:
            x = a / b
        else:
            x = 0
        #print(a, b, x)
        out.append(x)

    print ("PerformanceSEARCHRedBlackTree will return:", out)
    return out

# def timePerformanceSEARCHSkipList(input_listOfLists, search_listOfLists):
    # res = map_lists(input_listOfLists, search_listOfLists, messureTime_SEARCH_Skiplist)
    # reverse list, because of pop() use (witch starts from opposite end)
    # res.reverse()
    # print ("timePerformanceSEARCHRedBlackTree has messured time pro list iteration, and will return:", res)
    # return res    

def PerformanceMinMaxFingerSEARCHRedBlackTree (input_listOfLists, search_listOfLists):
    res = map_lists(input_listOfLists, search_listOfLists, messureNodes_MinMaxFingerSEARCH_RedBlackTree)
    out = []
    se = readMYfile('searchLists.csv')
    # print(se)
    while len(res) > 0 and len(se) > 0:
        a = res.pop(0)
        b = (se.pop(0))
        if type(b) == list:
            b = len(b)
        if b != 0:
            x = a / b
        else:
            x = 0
        #print(a, b, x)
        out.append(x)

    print("PerformanceMinMaxFingerSEARCHRedBlackTree will return:", out)
    return out


def PerformanceLAZYFingerSEARCHRedBlackTree(input_listOfLists, search_listOfLists):
    res = map_lists(input_listOfLists, search_listOfLists, messureNodes_LAZYFingerSEARCH_RedBlackTree)
    out = []
    se = readMYfile('searchLists.csv')
    # print(se)
    while len(res) > 0 and len(se) > 0:
        a = res.pop(0)
        b = (se.pop(0))
        if type(b) == list:
            b = len(b)
        if b != 0:
            x = a / b
        else:
            x = 0
        #(a, b, x)
        out.append(x)

    print("PerformanceLAZYFingerSEARCHRedBlackTree will return:", out)
    return out

def PerformanceSPLAYFingerSEARCHRedBlackTree(input_listOfLists, search_listOfLists):
    #print ("PerformanceSPLAYFingerSEARCHRedBlackTree started with:", len(input_listOfLists), len(search_listOfLists))
    res = map_lists(input_listOfLists, search_listOfLists, messureNodes_SPLAYFingerSEARCH_RedBlackTree)
    out = []
    se = readMYfile('searchLists.csv')
    # print(se)
    while len(res) > 0 and len(se) > 0:
        a = res.pop(0)
        b = se.pop(0)
        if type(b) == list:
            b = len(b)
        if b != 0:
            x = a / b
        else:
            x = 0
        #print(a, b, x)
        out.append(x)

    print("PerformanceSPLAYFingerSEARCHRedBlackTree will return:", out)
    return out



if __name__ == "__main__":
    
    # Je nach dem wie stark die Rechenleistung ist, bitte begrenzen:
    sys.setrecursionlimit(50000)
    logging.basicConfig(filename='logFILE-PlotsCounterWindows.log', encoding='utf-8', level=logging.DEBUG)
    
    #Performance INSERT
    # in_listOfLists = readMYfile('inputLists.csv')
    # insert_TimeRBT = timePerformanceINSERTRedBlackTree(in_listOfLists)
    
    # in_listOfLists = readMYfile('inputLists.csv')
    # insert_TimeSKL = timePerformanceINSERTSkipList(in_listOfLists)
    
    #Performance ROOTSEARCH
    input_listOfLists = readMYfile('inputLists.csv')
    search_listOfLists = readMYfile('searchLists.csv') 
    search_TimeRBT = PerformanceSEARCHRedBlackTree(input_listOfLists, search_listOfLists)

    # input_listOfLists = readMYfile('inputLists.csv')
    # search_listOfLists = readMYfile('searchLists.csv')
    # search_TimeSKL = timePerformanceSEARCHSkipList(input_listOfLists, search_listOfLists)
    
    #Performance FINGER SEARCH
    input_listOfLists = readMYfile('inputLists.csv')
    search_listOfLists = readMYfile('searchLists.csv')
    search_MinMaxFinger_TimeRBT = PerformanceMinMaxFingerSEARCHRedBlackTree(input_listOfLists, search_listOfLists)
    
    input_listOfLists = readMYfile('inputLists.csv')
    search_listOfLists = readMYfile('searchLists.csv')
    search_LazyFinger_TimeRBT = PerformanceLAZYFingerSEARCHRedBlackTree(input_listOfLists, search_listOfLists)
    
    input_listOfLists = readMYfile('inputLists.csv')
    search_listOfLists = readMYfile('searchLists.csv')
    search_SplayFinger_TimeRBT = PerformanceSPLAYFingerSEARCHRedBlackTree(input_listOfLists, search_listOfLists)
    
    
    # logischer weise hat diese Kennzahl das gleiche format wie List_performanceTime, gut für plot...
    # Anzahl der Search Werte auslesen pro Liste < Anzahl der Input werte
    listOfLists = readMYfile('inputLists.csv')
    numberOfInputValuesRBT = subListLengh(listOfLists)
    
    listOfLists = readMYfile('inputLists.csv')
    numberOfInputValuesSKL = subListLengh(listOfLists)

    
# ------------------------------
# Plot Idea: list lenght and time in Datastructure, global Time
    
    # Actual plot
    # https://www.grund-wissen.de/informatik/python/scipy/matplotlib.html
   
    fig, ((plt1, plt2), (plt3, plt4)) = plt.subplots(2, 2)
    fig.suptitle('Laufzeiten Rotschwarz Baum und Skiplist')
    
    # Plot 1
    #plt1.plot (numberOfInputValuesRBT, insert_TimeRBT, 'ro', linestyle='--', label=r'insert time in RedBlackTree')
    #plt1.plot (numberOfInputValuesSKL, insert_TimeSKL, 'mo', linestyle='--', label=r'insert time in SkipList')
    
    #plt1.set_ylabel('Time in nano sec 10^(-6)')
    #plt1.set_xlabel('Number of values per list from CSV')
    
    # Plot 2
    plt2.plot (numberOfInputValuesRBT, search_TimeRBT, 'bo', linestyle='--', label=r'Rootsearch in Tree ') 
    plt2.plot (numberOfInputValuesRBT, search_MinMaxFinger_TimeRBT, 'go', linestyle='--', label=r'MinMax-Finger-Search in Tree') 
    plt2.plot (numberOfInputValuesRBT, search_LazyFinger_TimeRBT, 'ko', linestyle='--', label=r'Lazy-Finger-Search in Tree') 
    plt2.plot (numberOfInputValuesRBT, search_SplayFinger_TimeRBT, 'ro', linestyle='--', label=r'SplayTree-Finger-Search  in Tree')
    
    plt2.set_ylabel('Number of touched Nodes per Search')
    plt2.set_xlabel('Number of Nodes in Datastructure')
    
    # Plot 3
    # plt3.plot (numberOfInputValuesSKL, search_TimeSKL, 'ko', linestyle='--', label=r'Rootsearch time in SkipList ') 
    # plt3.set_ylabel('Total number of touched Nodes')
    # plt3.set_xlabel('Number of Values from CSV')
    
    # Plot 4
    plt4.plot (numberOfInputValuesRBT, search_TimeRBT, 'bo', linestyle='--', label='Rootsearch in RedBlackTree ') 
    plt4.plot (numberOfInputValuesRBT, search_SplayFinger_TimeRBT, 'ro', linestyle='--', label='SplayTree-Finger-Search in RedBlackTree') 
    
    plt4.set_ylabel('Total number of touched Nodes per Search')
    plt4.set_xlabel('Number of Nodes in Datastructure')
   
    
    # Legende einblenden:
    #plt1.legend(loc='upper left', frameon=True)
    plt2.legend(loc='center right', frameon=True)
    #plt3.legend(loc='upper left', frameon=True)
    plt4.legend(loc='center right', frameon=True)
   
    print ("Plot is on Display")
    plt.show()
    

