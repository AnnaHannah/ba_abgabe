# (29.11.2020) inspiriert von https://qvault.io/python/red-black-tree-python/
# modified by me

from RedBlackTree import RedBlackTree
import unittest
from random import seed, randint
from timeit import Timer
from _overlapped import NULL
from cmath import log

class RedBlackTreeTest(unittest.TestCase):

    def setUp(self):
        seed(0)
        self.rb = RedBlackTree()

# Test insert(elem) - funktioniert einwandfrei!
 
    def testInsertionInEmptyTree(self):
         # clean test tree needed
        self.rb.deleteFullTree()
        # start test
        self.rb.insert(1)
        self.assertTrue(self.rb.searchTree(1))
        self.assertFalse(self.rb.searchTree(2))
 
    def testInsersionAtTheBeginningOfTheTree(self):
        # clean test tree needed
        self.rb.deleteFullTree()
        # start test
        self.rb.insert(2)
        self.rb.insert(1)
        self.assertTrue(self.rb.searchTree(1))
        self.assertTrue(self.rb.searchTree(2))
         
    def testInsersionAtTheEndOfTheTree(self):
        # clean test tree needed
        self.rb.deleteFullTree()
        # start test
        self.rb.insert(1)
        self.rb.insert(2)
        self.assertTrue(self.rb.searchTree(1))
        self.assertTrue(self.rb.searchTree(2))
 
    def testInsertionOfTheSameElement(self):
        # clean test tree needed
        self.rb.deleteFullTree()
        # start test
        self.rb.insert(1)
        self.rb.insert(1)
        self.assertTrue(self.rb.searchTree(1))
        self.assertEqual(2, self.rb.nodes_in_tree())
         

# Test remove(elem)

    def testRemovalFromASingleElementTree(self):
        # clean test tree needed
        self.rb.deleteFullTree()
        
        # start test
        self.rb.insert(1)
        self.assertEqual(self.rb.deleteNode(1), None)
        self.rb.deleteNode(1)
        self.assertFalse(self.rb.deleteNode(1))

    def testRemovalFromAnElementNotInTheTree(self):
        # clean test tree needed
        self.rb.deleteFullTree()
        
        # start test
        self.rb.deleteNode(1)
        self.rb.insert(1)
        self.assertEqual(self.rb.deleteNode(1), None)
        self.rb.deleteNode(2)
        self.assertEqual(self.rb.deleteNode(1), None)

# Test find(elem) - funktioniert einwandfrei
 
    def testFindingOfASingleElementTree(self):
        # clean test tree needed
        self.rb.deleteFullTree()
        # start test
        
        self.rb.insert(1)
        node = self.rb.searchTree(1)
        self.assertEqual(1, node.data)
 
    def testFindingOfTheMiddleElementTree(self):
        # clean test tree needed
        self.rb.deleteFullTree()
        # start test
        self.rb.insert(1)
        self.rb.insert(2)
        self.rb.insert(3)
        node = self.rb.searchTree(2)
        self.assertEqual(2, node.data)
 
    def testFindingAnElementNotInTheTree(self):
        self.assertEqual(None, self.rb.searchTree(1))
        
        
    def testRightColor(self):
        # clean test tree needed
        self.rb.deleteFullTree() 
        #start test
        self.rb.insertMultipleElem([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        self.assertEqual(self.rb.root.color, 0)
        self.assertNotEqual(self.rb.root.color, 1)
        # smallest element and next to it
        self.assertEqual(self.rb.searchTree(1).color, 1)
        self.assertNotEqual(self.rb.searchTree(2).color, 1)
 
 
if __name__ == '__main__':
    unittest.main()
