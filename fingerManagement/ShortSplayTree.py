# Splay tree implementation in python
# Author: AlgorithmTutor
# Tutorial URL: http://algorithmtutor.com/Data-Structures/Tree/Splay-Trees/
# https://codecitrus.com/runden-in-python/

# Finger Management system, für optimierte suchen

from red_black_tree.RedBlackTree import *
from skiplist.SkipList import * 
import csv
import math
import logging



class Node:
    def  __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        

class ShortSplayTree:
    def __init__(self):
        self.root = None
        
        # param to messure performance
        self.counterNodes = 0
        self.usedNodesInSearch = 0
        self.counterRotations = 0
        
        
    def deleteFullTree(self):
        # all Nodes in tree
        self.data = None
        self.parent = None
        self.left = None
        self.right = None
          
        # tree Parameters
        self.data = None
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
        self.counterNodes = 0
        self.usedNodesInSearch = 0

    def recrusive_print(self, currPtr, indent, last):
        # print the tree structure on the screen
        if currPtr != None:
            sys.stdout.write(indent)
            if last == True:
                  sys.stdout.write("R----")
                  indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print (currPtr.data)

            self.recrusive_print(currPtr.left, indent, False )
            self.recrusive_print(currPtr.right, indent, True)
    
    def binary_search_NO_WORKING_VERSION(self, startNode, key):
        
        #print ("start this binary_search parameter:", type(startNode), type(key))
        if (type(startNode) == None) or (startNode == None):
            print("FAIL: BinarySplayTree Startnode got lost -> self.root recovery", type(startNode))
            return self.root
        else:
            self.usedNodesInSearch += 1
            if key == startNode.data:
                #print ("-- binary_search found key in splay:", key, startNode.data)
                return startNode
            
            if key < startNode.data:
                if startNode.left != None:
                    return self.binary_search(startNode.left, key)
                else: 
                    # print ("SplayTree Binary searchresult nearby:", startNode.data)
                    return startNode
            if key >= startNode.data:
                if startNode.right != None:
                    return self.binary_search(startNode.right, key)
                else: 
                    #print ("SplayTree Binarysearch result nearby:", startNode.data)
                    return startNode
            else:
                return self.root

    
        
    
    
    def binary_search(self, startNode, key):
        
        if type(startNode) == None or (startNode == None):
            print("ERROR: binary_search type of StartNod is invalid - break", type(startNode))
        
        # abbruch der Suche wenn ergebnis gefunden:
        global firstRes
        firstRes = None
        global leafRes
        leafRes = None
        
        #print ("\n B) START this binary_search parameter:", (startNode.data, key))
        #print ("-- START usedNodesInSearch :", self.usedNodesInSearch, "\n")
        if key == startNode.data:
            #self.usedNodesInSearch += 1
            firstRes = startNode
            #print ("B) return END1: binary_search - FOUND key: ", key, firstRes.data)
            #print ("-- END1 usedNodesInSearch :", self.usedNodesInSearch, "\n")
            return firstRes
        
        self.usedNodesInSearch += 1
               
        if key != startNode.data and firstRes == None:
                            
            if (startNode.left != None) and (startNode.right == None):
                #print ("binary_search GO LEFT:", (startNode.data, key))
                #print ("-- GO LEFT: self.usedNodesInSearch :", self.usedNodesInSearch)
                self.binary_search(startNode.left, key)
                #print ("-- GO LEFT: self.usedNodesInSearch :", self.usedNodesInSearch)
                
            if (startNode.left == None) and (startNode.right != None):
                #print ("binary_search GO RIGHT:", (startNode.data, key))
                #print ("-- GO RIGHT self.usedNodesInSearch :", self.usedNodesInSearch)
                self.binary_search(startNode.right, key)    
                #print ("-- GO RIGHT self.usedNodesInSearch :", self.usedNodesInSearch)
                                
            if (startNode.left != None) and (startNode.right != None):
                #print ("binary_search GO Left+RIGHT:", (startNode.data, key))
                #print ("-- GO Left+RIGHT self.usedNodesInSearch :", self.usedNodesInSearch)
                x = self.binary_search(startNode.left, key)
                if x == None and (firstRes) == None:
                    y = self.binary_search(startNode.right, key)  
                #print ("-- GO Left+RIGHT self.usedNodesInSearch :", self.usedNodesInSearch)
            
            if (startNode.left == None) and (startNode.right == None):
                # leaf situation AND no result found -> set new leaf as result
                
                #print ("B) binary_search SET LEAF:", startNode.data, key)
                #print ("-- SET LEAF usedNodesInSearch :", self.usedNodesInSearch)
                leafRes = startNode
                
                #print ("-- SET LEAF usedNodesInSearch :", self.usedNodesInSearch)
              
        if firstRes != None:
            #print ("B) return END3: binary_search - FOUND key: ", (firstRes.data, key))
            #print ("-- END3 usedNodesInSearch :", self.usedNodesInSearch, "\n")
            return firstRes
        #else: return leafRes
            
       
            
        
    def deleteElem(self, startNode, key):
        x = None
        t = None 
        s = None
        while startNode != None:
            if startNode.data == key:
                x = startNode
            if startNode.data <= key:
                startNode = startNode.right
            else:
                startNode = startNode.left
        self.counterNodes -= 1
        if x == None:
            print ("Couldn't find key in the tree")
            return
        
        # split operation
        self.moveToTop(x)
        if x.right != None:
            t = x.right
            t.parent = None
        else:
            t = None

        s = x
        s.right = None
        x = None

        # join operation
        if s.left != None:
            s.left.parent = None

        self.root = self.joinToOneTree(s.left, t)
        s = None

    # rotate left at node x
    def left_rotate(self, x):
        
        self.counterRotations += 1
        
        y = x.right
        x.right = y.left
        if y.left != None:
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

    # rotate right at node x
    def right_rotate(self, x):
        
        self.counterRotations += 1
        
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        
        y.parent = x.parent;
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y

    # Splaying operation. It moves x to the root of the tree
    def moveToTop(self, x):
        assert (type(x)) is not None, " \n %r is not a Node for moveToTop/splay in Splaytree" % (self.root)
        
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    # zig rotation
                    self.right_rotate(x.parent)
                else:
                    # zag rotation
                    self.left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zig rotation
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag rotation
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag rotation
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)
            else:
                # zag-zig rotation
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)

    # joins two trees s and t
    def joinToOneTree(self, s, t):
        if s == None:
            return t

        if t == None:
            return s

        x = self.maximumNode(s)
        self.moveToTop(x)
        x.right = t
        t.parent = x
        return x

    # find the successor of a given node
    def successor(self, x):
        # if the right subtree is not null,
        # the successor is the leftmost node in the
        # right subtree
        if x.right != None:
            return self.minimum(x.right)

        # else it is the lowest ancestor of x whose
        # left child is also an ancestor of x.
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    # find the predecessor of a given node
    def predecessor(self, x):
        # if the left subtree is not null,
        # the predecessor is the rightmost node in the 
        # left subtree
        if x.left != None:
            return self.maximum(x.left)

        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y

    def __pre_order_helper(self, node):
        if node != None:
            sys.stdout.write(node.data + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != None:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != None:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            std.out.write(node.data + " ")

    # Pre-Order traversal
    # Node->Left Subtree->Right Subtree
    def preorder(self):
        self.__pre_order_helper(self.root)

    # In-Order traversal
    # Left Subtree -> Node -> Right Subtree
    def inorder(self):
        self.__in_order_helper(self.root)

    # Post-Order traversal
    # Left Subtree -> Right Subtree -> Node
    def postorder(self):
        self.__post_order_helper(self.root)


    # search the tree for the key k
    # and return the corresponding node
    def searchSplayTree(self, k):
        assert (type(self.root.data) or type(self) or type(k)) is not None, " \n %r is not a Root in Splaytree" % (self.root)
        
        if type(self.root)!= None and type(self) != None and type(self.root.data)!= None:
            #print ("A) searchSplayTree gives (%r) as startpoint for binary_search for:" % self.root.data, k)
            x = None
            x = self.binary_search(self.root, k)
           
            if x != None:
                #print ("A) searchSplayTree -> binary_search returns:", x.data, k)
                self.moveToTop(x)
            #else:
                #print ("A) searchSplayTree -> binary_search returns %r for:" % type(x),  k)
           
            return x
        else:
            print("NO Root in Splaytree!")
            
    def minimumNode(self, node):
        while node.left != None:
            node = node.left
        return node

    def maximumNode(self, node):
        while node.right != None:
            node = node.right
        return node

    # insert the key to the tree in its appropriate position
    def insert(self, key):
        node =  Node(key)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        self.counterNodes += 1       
             
        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        # splay the node
        self.moveToTop(node)
        
    def insertMultipleElem(self, list):
        while list != []:
            x = list.pop()
            self.insert(x)
            
    def deleteNode(self, data):
        # delete the node from the tree
        self.deleteElem(self.root, data)

    def printSplaytree(self):
        self.recrusive_print(self.root, "", True)

    def findMultipleElem_with_SplayTree (self, tree, searchlist):
        global resultList 
        resultList =[]
        while (len(searchlist) > 0):
            key = searchlist.pop()
            splay_result = self.searchSplayTree(key)
            #if splay_result == None:
                #print ("\n C) findMultipleElem_with_SplayTree: start twoDirectSearch_Node in BST with Splaynode:", splay_result)
            #print ("\n C) findMultipleElem_with_SplayTree: start twoDirectSearch_Node in BST with Splaynode:", splay_result.data)
            x = tree.twoDirectSearch_Node(splay_result, key)
            #if x != None:
               # print ("\n C) with splay twoDirectSearch_Node in BST has found:", x.data)
            #else: #print ("\n C) twoDirectSearch_Node in BST has found:", type(x))
            
            if x != None:
                #print("1) result twoDirectSearch_Node in BST:", (x.data))    
                resultList.append(x.data) 
            else:
                #print("2) result twoDirectSearch_Node in BST: ", (x))
                resultList.append(x)
        return resultList
    
    def findMultipleElem_with_SplayTree_WORKING (self, tree, searchlist, resultList):
        while (len(searchlist) > 0):
            key = searchlist.pop()
            splay_result = self.searchSplayTree(key)
            
            #print ("\nStart twoDirectSearch_Node in BST with Splaynode:", splay_result.data)
            x = tree.twoDirectSearch_Node(splay_result, key)
            #print ("twoDirectSearch_Node in BST is searching for key:", key) 
            
            if x != None:
                #print("1) result twoDirectSearch_Node in BST:", (x.data))    
                resultList.append(x.data) 
            else:
                #print("2) result twoDirectSearch_Node in BST: ", (x))
                resultList.append(x)
        return resultList



if __name__ == '__main__':
    
    sys.setrecursionlimit(20000)
    logging.basicConfig(filename='logFILE.log', encoding='utf-8', level=logging.DEBUG)
    
    
    list1 = list(range(1,10))
    list2 = list1.copy()
    search_list = [5,9,5,9,5,9,5,9,5]
    print ("list1:", list1)
    print ("list2:", list2)
    print ("search_list:", search_list)
    
    bst = RedBlackTree()
    splay = ShortSplayTree()
    splay.insertMultipleElem(list1) 
    
    bst.insertMultipleElem(list2)
    
    print("\n-- now searching -- ")
    
    splay.findMultipleElem_with_SplayTree(bst, search_list)
    
    print("1) bst.usedNodesInSearch: ", bst.usedNodesInSearch)
    print("2) splay.usedNodesInSearch: ", splay.usedNodesInSearch)
    print ("\n => total numbers of nodes used with splay tree:",  bst.usedNodesInSearch + splay.usedNodesInSearch)
    print("----------------------------------------------")
    bst.printTree()
    print("----------------------------------------------")
    splay.printSplaytree()
    
    