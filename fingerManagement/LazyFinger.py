# Lazy finger merkt sich immer das zuletzt gesuchte element und verwendet dieses Element als Startnode in der suchfunktion

# meine Datenstruckturen
from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import *


import csv
import logging


class Finger():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = None
        
class LazyFinger():
    def __init__ (self):
        self.lazyFinger = Finger(None)
        # param to messure performance
        self.usedNodesInSearch = 0

    # set the first finger to the root (why not)      
    def setfirst_LazyFinger(self, tree):
        newLazyFinger = tree.getRoot()
        self.lazyFinger = newLazyFinger

        assert type(self.lazyFinger.data) or self.lazyFinger is not None, " \n %r is not a Finger, something went wrhong while setting up first Lazy Finger:" % (self.lazyFinger.data)
        #print(" Error, something went wrong, while setting the first finger")
        return self.lazyFinger
    
    # update the finger after search
    def lazyFinger_search(self, tree, keyInInt):
        global resultList
        resultList = []
        assert type(self.lazyFinger) or self.lazyFinger.data or keyInInt is not None, " \n %r is not a Finger, in this Tree only Lazy Finger as Finger accepted. \n Please modify your Lazyfinger" % (self.lazyFinger)
        self.usedNodesInSearch += 1
            
        #print("0) lazyFinger_search - searches for %r:"  % self.lazyFinger.data, keyInInt)
            
        if keyInInt == self.lazyFinger.data:
            searchResult = self.lazyFinger
            resultList.append(searchResult.data)
            #print("1) lazyFinger_search FOUND =", searchResult.data)
            return searchResult

        if self.lazyFinger.data != None:
            searchResult = None
            searchResult = tree.twoDirectSearch_Node(self.lazyFinger, keyInInt)
            resultList.append(searchResult.data)
            #print("2) lazyFinger_search used twoDirectSearch_Node =", searchResult.data)

        if searchResult != None:
            self.lazyFinger = searchResult
            #print("3) Lazy Finger now set to:", self.lazyFinger.data)
            #print("3) AFT lazyFinger_search resultList =", resultList)

        if searchResult == None:
            resultList.append(searchResult)
            self.lazyFinger = tree.getRoot()
            #print("4) !BAD CASE: lazyFinger set to  = ", self.lazyFinger.data)
            #print("4) !BAD CASE: searchResult = ", searchResult)

        #print("5) lazyFinger_search END resultList =", resultList)
        #print("5) lazyFinger_search END searchResult =", searchResult.data)

        return searchResult
    
    def findMultipleElem_with_LazyFinger(self, tree, list):
        foundList = []
        while list != []:
            x = list.pop()
            self.lazyFinger_search(tree, x)
            #print ("\n lazyfinger now:",  self.lazyFinger.data, "\n")

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    logging.basicConfig(filename='logFILE.log', encoding='utf-8', level=logging.DEBUG)
    
    #skl = SkipList()
    inputList1 = [1,2,3,4,5,6,7,8]
    searchlist = [1,1]
    print ("insert list in bst:", inputList1)
    print ("search list for Lazy finger:", searchlist)
       
    len_s = len(searchlist)
    len_i = len(inputList1) 
    
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList1)
    
    
    lf = LazyFinger()
    lf.LazyFinger = lf.setfirst_LazyFinger(bst)
    print("\n setfirst_LazyFinger - lazyFinger was set to:", lf.lazyFinger.data)
    
    print ("so many LazyFinger.usedNodesInSearch in BST:", lf.usedNodesInSearch)
    print ("so many BST.usedNodesInSearch:", bst.usedNodesInSearch)
    print ("TOTAL Used Nodes in search:", bst.usedNodesInSearch + lf.usedNodesInSearch)
    
    # Aktion  
    lf.findMultipleElem_with_LazyFinger(bst, searchlist)
    
    print ("so many LazyFinger.usedNodesInSearch in BST:", lf.usedNodesInSearch)
    print ("so many BST.usedNodesInSearch:", bst.usedNodesInSearch)
    print ("TOTAL Used Nodes in search:", bst.usedNodesInSearch + lf.usedNodesInSearch)
   
    
    # compare without
    print("--- without lazy finger ---")

    print ("len_s", len_s)
    print("mathematical search would be", (math.log2(len_i))*(len_s))
    
    #bst.printTree()
    #bst.printTree()
    #skl.printSkipList()
    
    
    
    
    
    