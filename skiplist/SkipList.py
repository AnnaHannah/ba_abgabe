import sys
from _overlapped import NULL
from skiplist.LinkedList import LinkedList
# Implementing Skiplist in Python
from random import randint, seed
from time import sleep
from tkinter.tix import INTEGER
from operator import contains
from numpy.core.defchararray import isdigit, isdecimal
#from red_black_tree.RedBlackTree import inputList1


class SkipNode():
    def __init__(self, height = 0, data = None):
        self.height = 0
        self.data = data
        self.next = [None]*height

class SkipList():

    def __init__(self):
        self.head = SkipNode()
        self.len = 0
        # max hight of a specitifc Node - it is always smaller then Skiplist hight
        self.maxHeight = 0 

    def __len__(self):
        return self.len

    def findElem(self, data):
        # update = self.updateList(data)
        if data == None:
            return (print( "Error you need to put an dataent in FindElem()"))
        if data != None:
            for i in (range(0, len(self.head.next), 1)):
                x = self.head
                while x.next[i] != None: 
                    x = x.next[i] 
                    if x.data == data: 
                        return x.data
            return None    
    
    def findNodeByElem(self, data, node):
        # this function is analog to Search for data, but instead is doing search for Node with dedicadet data 
        # this has Formating reasons
        # this function searches if a node with this data exists
        update = self.updateList(data, node)
        if data == None:
            print("\n C2) findfindNodeByElemElem was given None", data)
            return None
        else:
            if len(update) > len(self) and data != None:
                candidate = update[0].next[0]
                if candidate != None and candidate.data == data:
                    print("C2) findNodeByElem found this candidate:", candidate.data)
                    return candidate

    def contains(self, data):
        return (self.findElem(data) != None)

    def randomHeight(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def updateList(self, data, node):
        #print(" B) in function updateList() - jumpNextLine - this is number of clean lines:", [None]*self.maxHeight)
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            # Jede Ebene durchgehen
            while x.next[i] != None and x.next[i].data < data:
                # alle elemente in der ebene durch gehen und beim richtigen Stoppen:
                x = x.next[i]
            update[i] = x
            #print("B) in function updateList() - jumpNextLine - this was updated:", data)
        return update
        
    def insertElem(self, data):        
        if self.findElem(data) == None:
            node = SkipNode(self.randomHeight(), data)
            self.maxHeight = max(self.maxHeight, len(node.next))
            
            while len(self.head.next) < len(node.next):
                self.head.next.append(None)
    
            update = self.updateList(data, node)            
            if self.findNodeByElem(data, update) == None:
                for i in range(0, len(node.next)):
                    node.next[i] = update[i].next[i]
                    update[i].next[i] = node
                self.len += 1
            else: return ''  
   
    def insertMultipleElem(self, list):
        # Listeneinträge Pop-> einzeln einfügen in Skipliste    
        while list.__len__() > 0:
            x = list.pop()
            self.insertElem(x)  
            
    def findMultipleElem(self, list):   
        foundList = []
        while list.__len__() > 0:
            x = list.pop()
            self.findElem(x)
            # if self.findElem(x) != None:
                # foundList.append(self.findElem(x))
        # return foundList

    def delete(self, data):
        x = self.findElfindNodeByElem
        if x != None:
            for i in reversed(range(len(x.next))):
                #print("\n delete was operating on:", x.data)
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maxHeight -= 1
            self.len -= 1            
        
    def counterNodes(self):
        counter = 0
        for i in reversed(range(0, len(self.head.next), 1)):
            # Jede Ebene hat einen Kopf, der alleine ist schon 1 Wert
            x = self.head
            counter = counter + 1 
            while x.next[i] != None:  
                # jedes Element wird gezählt
                if x.data != None:
                    counter = counter + 1
                x = x.next[i] 
        return counter            
                
    def printSkipList(self):
        # indent = ""
        # Alle schichten der Skiplist durchgehen und immer 1 abziehen       
        for i in reversed(range(0, len(self.head.next), 1)):
            print ("\n------------------------------- Ebene Nummer", i)
            x = self.head
            while x.next[i] != None:  
                if x.data != None:
                    sys.stdout.write(str(x.data) + " ")
                x = x.next[i]
            if x.next[i] == None:
                    sys.stdout.write(str(x.data) + " ")

        # ohne das return erscheint ein None
        return ''
    
    
    def maximumInSkiplist(self):
        # idee: in jeder gereihten liste ist das maximum ganz hinten 
        # also gehe ich gleich auf die letze Liste (unten) und das letzte element
        if self.head != None:
            for i in (range(0, len(self.head.next), 1)):
                # unterste Zeile             
                x = self.head
                while x.next[i] != None:  
                    # jedes Element durch
                    x = x.next[i]
                    if x.next[i] == None:
                        return x
        return (self.head)
            
    def minimumInSkiplist(self):
        if self.head != None:   
        # idee: in jeder gereihten liste istr das minimum ganz vorne 
        # also gehe ich gleich auf die letze Liste (unten) und das erste element
            for i in reversed(range(0, len(self.head.next), 1)):
                x = self.head.next[0]
                return x
        return (self.head)
        
    #def listSearch(self, nodesList, searchNode):
    
            
    #def listSearchLinear(self, searchNode):
    #    return self.listSearch(self.head.next[o], searchNode)
           
if __name__ == "__main__":
    sys.setrecursionlimit(200)
    skl = SkipList()
    #inputList = list(range(1,1000))
    inputList1=[1,2,3,4,5,6,7,8 ]
    skl.insertMultipleElem(inputList1)
    print("\n - > number of nodes in SkipList:", skl.counterNodes())
    skl.printSkipList()
    # print ("\n \n skl.head ist:", skl.head.next[1].data)
    # print ("\n Here skl.maximumInSkiplist() = ", skl.maximumInSkiplist())
    print("\n skl.minimumInSkiplist() is now:", skl.minimumInSkiplist().data)
    print("\n skl.maximumInSkiplist() is now:", skl.maximumInSkiplist().data)
    
    print("\n liear Search war looking for:", skl.head.next[2].data)
    #skl.listSearchLinear(skl.head.next[2].data)
    
    