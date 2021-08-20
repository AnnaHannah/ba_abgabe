import sys
from _overlapped import NULL
from idlelib.idle_test.test_editor import insert
# Implementing Red-Black Tree in Python
# Importing the threading module
from time import sleep
from tkinter.tix import INTEGER
from idlelib.idle_test.test_configdialog import root
from fingerManagement.BinarySplayTree import * 
from fingerManagement.ShortSplayTree import *
from fingerManagement.LazyFinger import *
import logging

import matplotlib.pyplot as plt


# global Variable
mRcounter = 0
mBcounter = 0


# Node creation
class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = None

    @property
    def x_y_wurzel(self):
        abstand_x = 0
        abstand_y = 0
        current = self
        while current.parent:
            abstand_y += 1
            if current == current.parent.left:
                abstand_x -= 1*abstand_y
            elif current == current.parent.right:
                abstand_x += 1*abstand_y
            else:
                raise Error("hilfe hilfe(panik panik); Node hat mehr als 2 Kinder u./o. ist nicht richtig verlinkt")
            current = current.parent


        return (abstand_x, abstand_y)



class RedBlackTree():

    def __init__(self):
        self.TNULL = Node(None)
        self.TNULL.color = 1
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.hight = 0
        
        # param to messure performance
        self.counterNodes = 0
        self.usedNodesInSearch = 0
        self.counterRotations = 0

    @property
    def all_nodes(self):
        output = []
        to_be_processed = [self.root]
        while to_be_processed:
            current = to_be_processed.pop()
            output.append(current)
            if current.left and current.left != self.TNULL:
                to_be_processed.append(current.left)
            if current.right and current.right != self.TNULL:
                to_be_processed.append(current.right)
        return output


    
    def deleteFullTree (self):
        # all Nodes in tree
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        
        # tree Parameters
        self.data = None
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
        self.counterNodes = 0
        self.usedNodesInSearch = 0
        
    # Preorder
    def preOrderHelper(self, node):
        if node != self.TNULL:
            sys.stdout.write(str(node.data) + " ")
            self.preOrderHelper(node.left)
            self.preOrderHelper(node.right)

    # Inorder
    def inOrderHelper(self, node):
        if node != self.TNULL:
            self.inOrderHelper(node.left)
            sys.stdout.write(str(node.data) + " ")
            self.inOrderHelper(node.right)

    # Postorder
    def postOrderHelper(self, node):
        if node != self.TNULL:
            self.postOrderHelper(node.left)
            self.postOrderHelper(node.right)
            sys.stdout.write(str(node.data) + " ")

    
    def downSearchTree(self, node, key):
        # Search the tree
        # retruns Keys not Nodes
        #print (" Node in downSearchTree is now: ", node.data)
        # now checking the good Cases:

        logging.error("\n downSearchTree (NOT NODE) START (%r," % node.data + " %r )" % key + " firstRes: %r \n " % firstRes)

        if node == self.TNULL or type(node) == Node(None) or node == None or key ==0:
            return None
        
        self.usedNodesInSearch += 1
        if key == node.data:
            #print ("Gesucht nach %r und im Tree gefunden." % node.data)
            return node.data
        if key < node.data:
            #print("downSearchTree %r used, for" % node.data, key)
            return self.downSearchTree(node.left, key)
        if key > node.data:
            return self.downSearchTree(node.right, key)
        else:
            logging.error("\n downSearchTree (NOT NODE) CASE MISSED (%r," % node.data + " %r )" % key + " firstRes: %r \n " % firstRes)
    
    def downSearchTree_Node(self, node, key):
        # Search downwards the tree
        # returns Nodes not keys
        self.usedNodesInSearch += 1

        global firstRes
        firstRes = None

        if node == self.TNULL or type(node) == Node(None) or node.data == None or key == 0:
            #print("downSearchTree_Node returns None because of node.data:", node.data)
            logging.error("downSearchTree_Node NONE with (%r," % node.data + " %r )" % key + " parent: %r" % node.parent)
            return None

        # now checking the good Cases:
        logging.info("\n downSearchTree_Node START (%r," % node.data + " %r-key)" % key + " firstRes: %r \n " % firstRes)

        if firstRes != None:
            logging.info("downSearchTree_Node firstRES FOUND2 (%r," % node.data + " %r )" % key + " firstRes: %r" % firstRes)
            return firstRes

        if key == node.data:
            firstRes = node
            logging.info(" \n downSearchTree_Node FOUND1 (%r," % node.data + " %r )" % key + " firstRes: %r" % firstRes.data)
            return firstRes        

        if key > node.data:
            logging.info("downSearchTree_Node GO RIGHT (%r," % node.data + " %r )" % key + " firstRes: %r" % firstRes)
            x = self.downSearchTree_Node(node.right, key)
            if x != None:
                logging.info("downSearchTree_Node GO RIGHT now return: %r" % x.data)
            else:
                logging.info("downSearchTree_Node GO LEFT now return: %r" % x)
            return x

        if key < node.data:
            logging.info("downSearchTree_Node GO LEFT (%r," % node.data + " %r )" % key + " firstRes: %r" % firstRes)
            x = self.downSearchTree_Node(node.left, key)
            if x != None:
                logging.info("downSearchTree_Node GO LEFT now return: %r" % x.data)
            else:
                logging.info("downSearchTree_Node GO LEFT now return: %r" % x)
            return x
        else:
            logging.info("downSearchTree_Node MISSED CASE with (%r," % node.data + " %r )" % key + " firstRes: %r" % firstRes)
    
    def twoDirectSearch(self, node, key):
        # Search the tree upwards an downwords   
        # retruns Keys not Nodes  
        
        if node == self.TNULL:
            return None
        
        self.usedNodesInSearch += 1
        
        if node.data != None:    
            #print (" Node in twoDirectSearch is now: ", node.data)
            if key == node.data:
                return node.data
            
            # root cases      
            if key < node.data and node.parent == None:
                return self.downSearchTree(node.left, key) 
            
            if key > node.data and node.parent == None:
                return self.downSearchTree(node.right, key)
            
            # basic cases
            if key < node.data and node.parent != None:
                x = self.downSearchTree(node.left, key) 
                if x != None:
                    #print ("downSearchTree started because, node.data is  bigger then key:", key, node.data)
                    return x
                else:
                    #print ("twoDirectSearch  started because, node.data is bigger then key:",key, node.data)
                    return self.twoDirectSearch(node.parent, key)
                
            if key > node.data and node.parent != None:
                x = self.downSearchTree(node.right, key) 
                if x != None:
                    #print ("downSearchTree  started because, node.data is smaller then key:", key, node.data)
                    return x
                else:
                    #print ("twoDirectSearch started because, node.data is smaller then key:", key, node.data)
                    return self.twoDirectSearch(node.parent, key) 
        else:
            return None

    def twoDirectSearch_Node(self, node, key):
        # Search the tree upwards an downwords  
        # returns Nodes not keys
        # if first res is found - > stop searching (specially needed for finger search)

        if type(node) == Node(None) or node == None or node.data == None or key <= 0:
            logging.error("twoDirectSearch_Node NONE with (%r," % node.data + " %r )" % key + " parent: %r" % node.parent)
            return None

        self.usedNodesInSearch += 1 #(down tree search hat schon +1 hier wäre es dopelt)

        # abbruch der Suche wenn ergebnis gefunden:
        global firstRes
        firstRes = None
        global leafRes
        leafRes = None

        logging.info("\n twoDirectSearch_Node START with (%r," % node.data + " %r )" % key + " firstRes: %r," % firstRes + " leafRes: %r \n" % leafRes )

        if key == node.data:
            firstRes = node
            logging.info(
                "twoDirectSearch_Node FOUND1 with (%r," % node.data + " %r )" % key + " firstRes: %r," % firstRes + " leafRes: %r  " % leafRes)
            return firstRes

        if firstRes != None:
            logging.info("twoDirectSearch_Node FOUND2 with (%r," % node.data + " %r )" % key + " firstRes: %r," % firstRes + " leafRes: %r" % leafRes)
            return firstRes

        # root cases
        if None == node.parent and key < node.data and node.left != None:
            logging.info("twoDirectSearch_Node GO LEFT with (%r," % node.data + " %r )" % key + "call downSearchTree_Node")
            return self.downSearchTree_Node(node.left, key)
        if None == node.parent and key > node.data and node.right != None:
            logging.info("twoDirectSearch_Node GO RIGHT with (%r," % node.data + " %r )" % key + "call downSearchTree_Node")
            return self.downSearchTree_Node(node.right, key)

        # node cases
        if key < node.data and node.left != None and node.parent != None and firstRes == None:
            # Eigentlich müsste man beides Paralell machen, aber ich gehen davonaus dass lokalitätsprinzip gilt => daher zuerst downsearch
            x = self.downSearchTree_Node(node.left, key)
            logging.info("1) twoDirectSearch_Node GO RIGHT with (%r," % node.data + " %r)" % key + "call downSearchTree_Node")
            #print ("1) twoDirectSearch_Node now x =", x)
            logging.info("1) twoDirectSearch_Node GO RIGHT now x = %r " %x)
            if x == None and firstRes == None:
                #go UP
                logging.info("1) twoDirectSearch_Node GO-UP with (%r," % node.data + " %r) " % key + "firstRes: %r " % firstRes + "leafRes: %r \n " % leafRes)
                y = self.twoDirectSearch_Node(node.parent, key)
                logging.info("1) twoDirectSearch_Node GO-UP now y = %r " %y.data)
                #print ("1) twoDirectSearch_Node now y =", y.data)
                if y != None:
                    firstRes = y
                    logging.info("1) twoDirectSearch_Node now y is firstRES = %r " % firstRes.data)
            else:
                firstRes = x
                logging.info("1) twoDirectSearch_Node now x is firstRES = %r " % firstRes.data)
                #print("twoDirectSearch_Node FOUND:", firstRes, key)

            logging.info("1) twoDirectSearch_Node RETURN firstRES = %r " %  firstRes.data)
            return firstRes

        if key > node.data and node.right != None and node.parent != None and firstRes == None:
            # Eigentlich müsste man beides Paralell machen, aber ich gehen davonaus dass lokalitätsprinzip gilt => daher zuerst downsearch
            logging.info("2) twoDirectSearch_Node GO RIGHT with (%r," % node.data + " %r)" % key + "call downSearchTree_Node")
            x = self.downSearchTree_Node(node.right, key)
            logging.info("2) twoDirectSearch_Node GO RIGHT now x = %r " % x)
            print ("2) twoDirectSearch_Node now x =", x)
            if x == None and firstRes == None:
                #self.usedNodesInSearch += 1
                logging.info("2) twoDirectSearch_Node GO-UP with (%r," % node.data + " %r) " % key + "firstRes: %r " % firstRes + "leafRes: %r \n " % leafRes)
                y = self.twoDirectSearch_Node(node.parent, key)
                logging.info("2) twoDirectSearch_Node GO-UP now y = %r " % y.data)
                print ("2) twoDirectSearch_Node now y =", y.data)
                if y != None:
                    firstRes = y
                    logging.info("2) twoDirectSearch_Node now y is firstRES = %r " % firstRes.data)
                    print ("twoDirectSearch_Node FOUND:", firstRes, key)
            else:
                firstRes = x
                logging.info("2) twoDirectSearch_Node now x is firstRES = %r " % firstRes.data)
                print("twoDirectSearch_Node FOUND:", firstRes, key)
            logging.info("2) twoDirectSearch_Node RETURN firstRES = %r " % firstRes.data)
            return firstRes

        else:
            logging.ERROR("CASE MISSED twoDirectSearch_Node node.data = %r, " % node.data + "firstRES = %r " % firstRes.data)
            print("case missed in twoDirectSearch_Node", node.data, firstRes)

    def fixDelete(self, x):
        # Balancing the tree after deletion
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.leftRotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.rightRotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rightRotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.leftRotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = 0

    def __rbTransplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
  
    def deleteNodeHelper(self, node, key):
        # Node deletion
        self.counterNodes -= 1
        if self.counterNodes < 0:
            self.counterNodes = 0
        if node == self.root:
            z = self.TNULL
            # node = self.TNULL
            return 
        
        while node != self.TNULL:
            if node.data == key:
                z = node
            if node.data <= key:
                node = node.right
            else:
                node = node.left
        if z == self.TNULL:
            print("Cannot find " + str(key) + " in the tree")
            return None
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rbTransplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rbTransplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rbTransplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rbTransplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.fixDelete(x)
    
    # Balance the tree after insertion
    def fixInsert(self, new_node):
        while new_node != self.root and new_node.parent.color == 1:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.color == 1:
                    u.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self.leftRotate(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle
                if u.color == 1:
                    u.color = 0
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self.rightRotate(new_node.parent.parent)
        self.root.color = 0

    
    def printHelper(self, node, indent, last):
        # Printing the tree
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last == True:
                sys.stdout.write("R----")
                indent += "|    "
            if last == False:
                sys.stdout.write("L----")
                indent += "    "

            if node.color == 1:
                s_color = "RED" 
            else: 
                s_color = "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.printHelper(node.left, indent, False)
            self.printHelper(node.right, indent, True)

    # Fix colors in Red Black tree
    def fixColorHelper(self, node): 
        
        def makeRed(node): 
            global mRcounter 
            mRcounter = mRcounter + 1
            # Abfangen von AttributeError: 'NoneType' object has no attribute 'color'
            # None.color exestiert nicht
            if node == None:
                return ''
            if node.color == 1:
                if node.left != None:
                    node.left.color = 0
                    makeBlack(node.left)
                if node.right != None:
                    node.right.color = 0
                    makeBlack(node.right)    
      
        def makeBlack(node):
            global mBcounter
            mBcounter = mBcounter + 1
            # Abfangen von AttributeError: 'NoneType' object has no attribute 'color'
            # None.color exestiert nicht
            if node == None:
                return ''     
            if node.color == 0:
                if node.left != None:
                    node.left.color = 1
                    makeRed(node.left)
                if node.right != None:
                    node.right.color = 1
                    makeRed(node.right)

        if node == None:
            return ''  
        
        makeBlack(node)  # falls Wurzel unbekannte Farbe hat
        makeRed(node)      
              
    def preorder(self):
        self.preOrderHelper(self.root)

    def inorder(self):
        self.inOrderHelper(self.root)

    def postorder(self):
        self.postOrderHelper(self.root)

    def rootSearchTree(self, k):
        self.twoDirectSearch_Node (self.root, k)
        #return self.downSearchTree(self.root, k)


    # rotations and balancing from here (19.07.2021 - 18:45 UHr): https://qvault.io/python/red-black-tree-python/
    def leftRotate(self, x):
        
        self.counterRotations += 1
        
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        
    def rightRotate(self, x):
        self.counterRotations += 1
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        
    def insert(self, key):
        assert type(key) is int, " \n %r is not an integer, in this Tree is only interger accepted. \n Please modify your Input. \n Insertionprozess stopped now" % key
        if self.contains(key) == False:
            # create new node:
            node = Node(key)
            node.parent = None
            node.data = key
            node.left = self.TNULL
            node.right = self.TNULL
            node.color = 1
            self.counterNodes = (self.counterNodes) + 1 
            # manage new Node:
            y = None
            x = self.root
    
            while x != self.TNULL:
                y = x
                if node.data < x.data:
                    x = x.left
                else:
                    x = x.right
    
            node.parent = y
            if y == None:
                self.root = node
            elif node.data < y.data:
                y.left = node
            else:
                y.right = node
            self.fixInsert(node)
            if node.parent == None:
                node.color = 0
                return
            if node.parent.parent == None:
                return
        
        self.usedNodesInSearch = 0
        self.hight = math.ceil(math.log2(self.counterNodes)) # ceil rundet auf
            
        
        
    def fixColor(self):
        self.fixColorHelper(self.root)
        
    def insertMultipleElem (self, list):
        while list != []:
            x = list.pop()
            self.insert(x)
            #self.fixInsert(x)
        self.fixColor()
        

    def findMultipleElem (self, list):
        foundList = []
        while list != []:
            x = list.pop(0)
            self.rootSearchTree(x)
            # if self.rootSearchTree(x) != None:
                # foundList.append(self.rootSearchTree(x))
        # return foundList

    def getRoot(self):
        return self.root

    def deleteNode(self, data):
        self.deleteNodeHelper(self.root, data)

    def printTree(self):
        self.printHelper(self.root, "", True)

    def nodesInTree(self):
        return self.counterNodes
    
    def contains(self, key):
        x= self.rootSearchTree(key)
        # contains macht eine versteckte Suche, das sollte nicht bei der normalen suche mit abgebildet werden
        if self.usedNodesInSearch >= 1:
            self.usedNodesInSearch -= 1
        return (x == key)
    
    
    def findMaximum(self, key): 
        # this maximum should NOT BE A LOGICAL MAXIMUM - this is the most right object
        currentMax = key
        if currentMax.data != None: 
            while (currentMax.right.data != None):
                currentMax = currentMax.right 
        print ("current maximum in Tree:", currentMax.data)
        return (currentMax)
           
    def findMinimum(self, key): 
         # this minimum should NOT BE A LOGICAL MAXIMUM - this is the most left object
        currentMini = key
        if currentMini.data != None: 
            while (currentMini.left.data != None):
                currentMini = currentMini.left
        print ("current minimum in Tree:", currentMini.data)
        return (currentMini)
    
    def findMaximum_WORKiNG(self, key): 
        # this maximum should NOT BE A LOGICAL MAXIMUM
        currentMax = key
        if currentMax.data != None: 
            while ((currentMax.right.data != None) and (currentMax.right.data > currentMax.data)):
                currentMax = currentMax.right
                print 
             #eigentlich unnötig
            while ((currentMax.left.data != None) and (currentMax.left.data > currentMax.data)):
                currentMax = currentMax.left
            
        print ("current maximum in Tree:", currentMax.data)
        return (currentMax)
           
    def findMinimum_WORKING(self, key): 
        currentMini = key
        if currentMini.data != None: 
            while ((currentMini.left.data != None) and (currentMini.left.data < currentMini.data)):
                currentMini = currentMini.left
            #eigentlich unnötig 
            while ((currentMini.right.data != None) and (currentMini.right.data < currentMini.data)):
                currentMini = currentMini.right
        print ("current minimum in Tree:", currentMini.data)
        return (currentMini)
        
    def maximumInTree(self): 
        maximum = self.findMaximum(self.root)
        #print("maximumInTree",maximum)
        return maximum 
    
    def minimumInTree(self):
        minimum = self.findMinimum(self.root)
        #print("minimumInTree",minimum)
        return minimum 
    
    

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    logging.basicConfig(filename='logFILE-RedBlackTree.log', encoding='utf-8', level=logging.DEBUG)
    logging.info("\n notice, before insertion the search proofs if there is a need for insertion - this search is also logged here \n ")

    # print("1. Recursion allowed in this program:", sys.getrecursionlimit())
    inputList = list(reversed(range(1,2500)))
    inputList1 = inputList.copy()
    inputList2 = inputList.copy()
    
    search_list = [3,9,3,9,3,9,3]
    search_list1= search_list.copy()
    print("inputlist is:", inputList)
    print("searchlist is:", search_list)
    
    # set up tree
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)

    all_nodes = bst.all_nodes
    fig, ax = plt.subplots(3, 1, figsize=(8, 10))

    # single point

    for node in all_nodes:
        x, y = node.x_y_wurzel
        ax[0].plot(x, y, '-ro', label='line & marker - no line because only 1 point')
    plt.show()

    assert 1 == 1
   

    bst.findMultipleElem(search_list)
    print("2) => total numbers of nodes used with bst: ", bst.usedNodesInSearch)
    print("\n1) Rootsearch BST: optimal nodes ", math.log(bst.counterNodes, 2)*len(search_list))
    
    #bst.printTree()
    # finish
    bst.deleteFullTree()
    
    print("\n --- now with splayspeedup ---\n ")
    
    print("inputlist is:", inputList1)
    print("inputlist is:", inputList2)
    print("searchlist is:", search_list1, "\n")
    
    # set up tree
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList1)

    lf = LazyFinger()
    lf.LazyFinger = lf.setfirst_LazyFinger(bst)
    lf.findMultipleElem_with_LazyFinger(bst, search_list1)

    #splay = ShortSplayTree()
    #splay.insertMultipleElem(inputList2)
    #splay.printSplaytree()
    #splay.findMultipleElem_with_SplayTree(bst, search_list1)
    
    print("1) bst.usedNodesInSearch (twoDirectSearch_Node)", bst.usedNodesInSearch)
    print("2) lf.usedNodesInSearch", lf.usedNodesInSearch)
    print ("\n => total numbers of nodes used with splay tree:",  bst.usedNodesInSearch + lf.usedNodesInSearch)
    bst.printTree()
    #splay.printSplaytree()

    
