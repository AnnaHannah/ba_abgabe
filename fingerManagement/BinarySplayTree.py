# Splay tree implementation in python
# Author: AlgorithmTutor
# Tutorial URL: http://algorithmtutor.com/Data-Structures/Tree/Splay-Trees/
# https://codecitrus.com/runden-in-python/

# Finger Management system, für optimierte suchen

from red_black_tree.RedBlackTree import *
from skiplist.SkipList import *
# from main.PlotsCounterWindows import *

import csv
import math
import logging
import copy
import random

class Node: #i should rename it to Finger!!
    def  __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        # routen markierung / aka suche war schon hier
        self.marked = 0
        

class BinarySplayTree:
    def __init__(self):
        self.root = None
        self.oneParamCache = None
        
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
        self.usedNodesInSearch += 1
        #print ("start this binary_search parameter:", type(startNode), type(key))
        if (type(startNode) == None) or (startNode == None):
            print("FAIL: BinarySplayTree Startnode got lost -> self.root recovery", type(startNode))
            return self.root
        elif(startNode != None):
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


    def mark_all_nodes_1 (self, startNode):
        if startNode != None:
            if startNode.left != None:
                startNode.left.marked = 1
                self.mark_all_nodes_1(startNode.left)
            if startNode.right != None:
                startNode.right.marked = 1
                self.mark_all_nodes_1(startNode.right)
            logging.info("mark_all_nodes_1 done for: {0}".format(startNode.data))

    def mark_all_nodes_0 (self, startNode):
        if startNode != None:
            if startNode.left != None:
                startNode.left.marked = 0
                self.mark_all_nodes_0(startNode.left)
            if startNode.right != None:
                startNode.right.marked = 0
                self.mark_all_nodes_0(startNode.right)

        logging.info("mark_all_nodes_0 done for: {0}".format(startNode.data))

    def binary_search(self, startNode, key):
        marked_route = []

        if type(startNode) == None or (startNode == None):
            print(TypeError)
            logging.info("TypeError: {0}".format(startNode))
            return None
        
        self.usedNodesInSearch += 1
        logging.info("binary_search parameter Startnode (data, key, marked): ({0}, {1}, {2}) ". format(startNode.data, key, startNode.marked))

        if key == startNode.data:
            startNode.marked = 1
            self.mark_all_nodes_1 (self.root)
            logging.info("!!! self.mark_all_nodes_1 !!!")
            logging.info("DONE - data: ({0})".format(startNode.data))
            self.oneParamCache = startNode
            return startNode

        if startNode.marked != 1:
            if startNode.left != None and startNode.left.marked != 1 and startNode.marked != 1:
                logging.info("1-GO LEFT {0}" .format(startNode.data))
                self.binary_search(startNode.left, key)
                startNode.marked = 1


            if startNode.right != None and startNode.right.marked != 1 and startNode.marked != 1:
                logging.info("1-GO RIGHT {0}".format(startNode.data))
                self.binary_search(startNode.right, key)
                startNode.marked = 1

            if startNode.marked == 1 and self.oneParamCache != None:
                logging.info("1-exit subsearch {0}".format(startNode.data))
                return (self.oneParamCache)
        else:
            logging.info("2-exit subsearch {0}".format(startNode.data))
            return (self.oneParamCache)

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
            print ("Couldn't find key to delete in the tree")
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
        # self.printSplaytree()


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
        assert (type(self.root.data) and type(self)) is not None, " \n %r is not a Root in Splaytree" % (self.root)
        if type(self.root)!= None and type(self) != None and type(self.root.data)!= None:
                x = self.binary_search(self.root, k)
                if x != None:
                    self.moveToTop(x)
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
        #self.moveToTop(node)
        
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
            key = searchlist.pop(0)
            logging.info("\nStart searchSplayTree for {0}".format(key))
            # clean splaytree from markes
            logging.info("\nStart Clean Splaytree, mark_all_nodes_0")
            self.mark_all_nodes_0(self.root)
            logging.info("\nStart splay_result for {0}".format(key))
            splay_result = self.searchSplayTree(key)
            if splay_result != None:
                logging.info("\nStart twoDirectSearch_Node in BST with Splaynode {0}".format(splay_result.data))

            if splay_result == key:
                resultList.append(splay_result.data)
                break
            else:
                x = tree.twoDirectSearch_Node(splay_result, key)
                logging.info("\ntwoDirectSearch_Node in BST is searching for key {0}".format(key))
            
                if x != None:
                    logging.info("1) result twoDirectSearch_Node in BST:{0}".format(x.data))
                    resultList.append(x.data)
                else:
                    logging.info("2) result twoDirectSearch_Node in BST:{0}".format(x))
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
    sys.setrecursionlimit(10000)
    logging.basicConfig(filename='logFILE-BinarySplayTree.log', encoding='utf-8', level=logging.DEBUG)

    def make_total_random(list):
        # Achtung, es macht nur Sinn nach Elementen zusuchen die auch da sind! => maximum der gegeben Listen ist größtest Elemeent
        res = []
        max = int(list[-1])
        for i in list:
            y = random.randrange(1, max)
            res.append(y)
        return res

    list1 = list(range(1,25))
    list2 = list(range(1,25))

    searchlist = [22,23,21,20,22,21,20,21,21,21,20,21,23,23,22,21,20,23,22,22,22,23,21,22]
    len_s = len(searchlist)
    resultList = []
    
    bst = RedBlackTree()            
    splay = BinarySplayTree()
    print("list1:", list1)
    bst.insertMultipleElem(list1)

    print("list2:", list2)
    splay.insertMultipleElem(list2)
    splay.printSplaytree()

    print("-----------------------------")
    print ("\nsearchlist = ", searchlist)

    print("Pre search: number of splay tree used Nodes in search:", splay.usedNodesInSearch)
    print("Pre search: number of used RedBlacktree  Nodes in search:", bst.usedNodesInSearch)
    print ("- > so many elements should be found", len(searchlist))

    splay.findMultipleElem_with_SplayTree(bst, searchlist)
    splay.printSplaytree()
    print("RESULT- LIST", resultList)
    print("SEARCH- LIST", searchlist)

    print("-----------------------------")
    print("Post Search: number of used Splaytree  Nodes in search:", splay.usedNodesInSearch)
    print("Post Search: number of used RedBlacktree  Nodes in search:", bst.usedNodesInSearch)
    
    print ("Post Search: totalnumber of used Nodes in all BST+SplayTree:",splay.usedNodesInSearch + bst.usedNodesInSearch)
    
    print ("optimal BST search numers would be:", int((math.log(bst.counterNodes, 2))*len_s))

    