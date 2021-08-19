# this class is the MinMax Finger tree
# this version of finger trees accepts input datastructure, then sets ist minimal and maximal pointers(Fingers) and then starts 
# a search from the given Pointer, 

# Funktioniert nur für rot schwarz bäume

from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 
from numpy import log
from main.GenerateSearchList import *
import logging


class Finger():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = None
        
class MinMaxFinger():
    def __init__ (self):
        self.maxiFinger = Finger(None)
        self.miniFinger = Finger(None)
        
        
        # param to messure performance
        self.usedNodesInSearch=0
    
    def setMaxiFingerFrom(self, tree):  
        if type(tree)== RedBlackTree:    
            newMaxFinger = tree.maximumInTree()
            self.maxiFinger = newMaxFinger
            #print("MaxiFinger was set from " + str(type(tree)) + " to", newMaxFinger.data)
            return newMaxFinger
        if type(tree) == SkipList:
            newMaxFinger = tree.maximumInSkiplist()
            self.maxiFinger = newMaxFinger
            #print("MaxiFinger was set from " + str(type(tree)) + " to", newMaxFinger.data)
            return newMaxFinger
    
    def setMiniFingerFrom(self, tree):  
        if type(tree)== RedBlackTree:        
            newMinFinger = tree.minimumInTree()              
            self.miniFinger = newMinFinger
            #print("MiniFinger was set from " + str(type(tree)) + " to", newMinFinger.data)
            return newMinFinger
        if type(tree)== SkipList: 
            newMinFinger = tree.minimumInSkiplist()
            self.miniFinger = newMinFinger
            #print("MiniFinger was set from " + str(type(tree)) + " to", newMinFinger.data)
            return newMinFinger
    
    def fingerSearch(self, tree, keyInInt):
        searchResult = None
        if type(tree)== RedBlackTree: 
            assert type(self.maxiFinger.data) is not None, " \n %r is not a Finger, in this Tree only Maxi Finger as Finger accepted. \n Please modify your Finger" % (self.maxiFinger.data)
            assert type(self.miniFinger.data) is not None, " \n %r is not a Finger, in this Tree only Mini Finger as Finger accepted. \n Please modify your Finger" % (self.miniFinger.data)
            assert type(keyInInt) is not None, " \n %r is not a keyInInt, in this Tree only keyInInt as Integer accepted. \n Please modify your keyInInt" % (type(keyInInt))
            
            self.usedNodesInSearch += 1
            
            if self.maxiFinger.data - keyInInt <= keyInInt - self.miniFinger.data:
                searchResult = tree.twoDirectSearch_Node(self.maxiFinger, keyInInt)
                #if( type(searchResult) != None or type(searchResult.data) != None):
                    #print ("1a) fingerSearch maxifinger case:", type(searchResult)) 
                    #print ("2a) twoDirectSearch_Node used maxiFinger %r for:"  % self.maxiFinger.data, keyInInt, searchResult.data)
                #else: 
                    #print ("fingerSearch has not found:", type(searchResult))  
               # print (self.usedNodesInSearch)
                #print (bst.usedNodesInSearch)    
            if self.maxiFinger.data - keyInInt > keyInInt - self.miniFinger.data:
                searchResult = tree.twoDirectSearch_Node(self.miniFinger, keyInInt)
                #if type(searchResult) != None or type(searchResult.data != None):
                    #print ("1b) fingerSearch minifinger case:", type(searchResult)) 
                    #print ("2b) twoDirectSearch_Node used miniFinger %r for:" % self.miniFinger.data, keyInInt, searchResult.data)
                #else: 
                    #print ("fingerSearch has not found:", type(searchResult))
                #print (self.usedNodesInSearch) 
                #print (bst.usedNodesInSearch) 
            #if keyInInt == searchResult.data:
                #print ("fingerSearch done")
            #else:
                #print ("fingerSearch case missed")
            #return searchResult
    # skiplist ansatz    
        # #if type(tree)== SkipList: 
            # if self.maxiFinger.data - keyInInt < keyInInt - self.miniFinger.data:
                # searchResult = (tree.twoDirectSearch(self.maxiFinger, keyInInt)) 
                # # print ("- fingerSearch used maxiFinger for:", searchResult)      
            # if self.maxiFinger.data - keyInInt > keyInInt - self.miniFinger.data:
                # searchResult = (tree.twoDirectSearch(self.miniFinger, keyInInt))
                # #print ("- fingerSearch used miniFinger for:", searchResult)
                # #print ("\nfingerSearch has found:", searchResult)
            
    def findMultipleElem_with_MinMaxFinger (self, tree, list):
        foundList = []
        while list != []:
            x = list.pop()
            self.fingerSearch(tree, x)   
        
if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    logging.basicConfig(filename='logFILE.log', encoding='utf-8', level=logging.DEBUG)

    bst = RedBlackTree()
    #skl = SkipList()
    inputList1 = list(range(1,75))
    searchlist = make_zickzack(list(range(1,12)))
    
    len_s = len(searchlist)
    len_i = len(inputList1)

    bst.insertMultipleElem(inputList1)
    #skl.insertMultipleElem(inputList1)
    
    mmf = MinMaxFinger()
    mmf.maxiFinger = mmf.setMaxiFingerFrom(bst)
    print ("maxiFinger = ", mmf.maxiFinger.data)
    mmf.miniFinger = mmf.setMiniFingerFrom(bst)
    print ("miniFinger = ", mmf.miniFinger.data)
    
    #mmf.maxiFinger = mmf.setMaxiFingerFrom(skl)
    #mmf.miniFinger = mmf.setMiniFingerFrom(skl)
    
    print ("Used Nodes in mmf search:", mmf.usedNodesInSearch)
    print ("Used Nodes in bst search:", bst.usedNodesInSearch)
    #print("\nErgebniss von Fingersearch ist, fingersearch entscheidet selbst ob es von minimum oder Maximum sucht:", mmf.fingerSearch(bst, 3))
    print("\nmmf.findMultipleElem_with_MinMaxFinger(bst, searchlist)")
    mmf.findMultipleElem_with_MinMaxFinger(bst, searchlist)
    print ("Used Nodes in mmf search:", mmf.usedNodesInSearch)
    print ("Used Nodes in bst search:", bst.usedNodesInSearch)
    print ("TOTAL Used Nodes in search:", bst.usedNodesInSearch + mmf.usedNodesInSearch)
    
    print ("len_s", len_s)
    print("mathematical search would be", (math.log2(len_i))*(len_s))
    
    bst.printTree()
    #bst.printTree()
    #skl.printSkipList()
    
    