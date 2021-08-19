import sys
from _overlapped import NULL
from idlelib.idle_test.test_editor import insert
# Implementing Red-Black Tree in Python
# Importing the threading module
from time import sleep
from tkinter.tix import INTEGER
from idlelib.idle_test.test_configdialog import root
from fingerManagement.BinarySplayTree import * 

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
            print("case missed in downSearchTree", node.data)
    
    def downSearchTree_Node(self, node, key):
        # Search downwards the tree
        # returns Nodes not keys
        
        if node == self.TNULL or type(node) == Node(None) or node == None or key ==0:
            return None
        
        self.usedNodesInSearch += 1
        
        if key == node.data:
            return node     
           
        if key < node.data:
            return self.downSearchTree_Node(node.left, key)
        
        if key > node.data:
            return self.downSearchTree_Node(node.right, key)
        else:
            print("case missed in downSearchTree_Node", node.data)
    
    def twoDirectSearch(self, node, key):
        # Search the tree upwards an downwords   
        # retruns Keys not Nodes  
        self.usedNodesInSearch += 1
        
        if node == self.TNULL:
            return None
        if node.data != None:    
            #print (" Node in twoDirectSearch is now: ", node.data)
            if key == node.data:
                return node.data
                  
            if key < node.data and node.parent == None:
                return self.downSearchTree(node.left, key) 
            
            if key > node.data and node.parent == None:
                return self.downSearchTree(node.right, key)
            
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
        
        if type(node) == Node(None) or node == None or node.data == None:
            return None
        
        self.usedNodesInSearch += 1 
        
        if key == node.data:
            return node
              
        if key < node.data and node.parent == None:
            return self.downSearchTree_Node(node.left, key) 
        
        if key > node.data and node.parent == None:
            return self.downSearchTree_Node(node.right, key)
        
        if key < node.data and node.parent != None:
            x = self.downSearchTree_Node(node.left, key) 
            if x != None:
                return x
            else:
                return self.twoDirectSearch_Node(node.parent, key)
               
        if key > node.data and node.parent != None:
            x = self.downSearchTree_Node(node.right, key) 
            if x != None:
                return x
            else:
                return self.twoDirectSearch_Node(node.parent, key) 
        else:
            print("case missed in downSearchTree_Node", node.data)

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
        return self.downSearchTree(self.root, k)


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
            
            #fix manipulations: 
        
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
            x = list.pop()
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
    # print("1. Recursion allowed in this program:", sys.getrecursionlimit())
    inputList = list(range(0,10))
    inputList1 = inputList.copy()
    search_list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    search_list1 = search_list.copy()
    
    # set up tree
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)
    bst.printTree()
    print("so many rotations were made:", bst.counterRotations)
    print("1) Rootsearch BST: bst.usedNodesInSearch ",bst.usedNodesInSearch)
    #start
    print("Rootsearch BST: optimal nodes ", math.log(bst.counterNodes, 2)*len(search_list))
    bst.findMultipleElem(search_list)
    print("2) Rootsearch BST: bst.usedNodesInSearch ",bst.usedNodesInSearch)
    
    
    # finish
    bst.deleteFullTree()
    
    print("\n --- now with splayspeedup ---\n ")
    
    
    splay = BinarySplayTree()
    splay.insertMultipleElem(inputList1) 
    
    splay.findMultipleElem_with_SplayTree(bst, search_list1)
    print("1) bst.usedNodesInSearch ", bst.usedNodesInSearch)
    print("2) splay.usedNodesInSearch", splay.usedNodesInSearch)
    print ("\n => total numbers of nodes used with splay tree:",  bst.usedNodesInSearch + splay.usedNodesInSearch)
    bst.printTree()

    
