# (30.11.2020, 16:00 Uhr) kopiert aus: https://github.com/kunigami/blog-examples/tree/master/skip-list 

from SkipList import SkipList
from LinkedList import LinkedList
import unittest
from random import seed, randint
from timeit import Timer

class SkipListTest(unittest.TestCase):

    def setUp(self):
        seed(0)
        self.sl = SkipList()

    # Test insert(elem)
 
    def testInsertionInEmptyList(self):
        self.sl.insertElem(1)
        self.assertTrue(self.sl.contains(1))
        self.assertFalse(self.sl.contains(2))

    def testInsersionAtTheBeginningOfTheList(self):
        self.sl.insertElem(2)
        self.sl.insertElem(1)
        self.assertTrue(self.sl.contains(1))
        self.assertTrue(self.sl.contains(2))
        
    def testInsersionAtTheEndOfTheList(self):
        self.sl.insertElem(1)
        self.sl.insertElem(2)
        self.assertTrue(self.sl.contains(1))
        self.assertTrue(self.sl.contains(2))

    def testInsertionOfTheSameElement(self):
        self.sl.insertElem(1)
        self.sl.insertElem(1)
        self.assertTrue(self.sl.contains(1))
        self.assertEqual(1, len(self.sl))

    # Test delete Node 

    def testRemovalFromASingleElementList(self):
        self.sl.insertElem(1)
        self.assertTrue(self.sl.contains(1))
        self.sl.delete(1)
        self.assertFalse(self.sl.contains(1))

    def testRemovalFromAnElementNotInTheList(self):
        self.sl.delete(1)
        self.sl.insertElem(1)
        self.assertTrue(self.sl.contains(1))
        self.sl.delete(2)
        self.assertTrue(self.sl.contains(1))

    # Test find(elem)

    def testFindingOfASingleElementList(self):
        self.sl.insertElem(1)
        node = self.sl.find(1)
        self.assertEqual(1, node.elem)

    def testFindingOfTheMiddleElementList(self):
        self.sl.insertElem(1)
        self.sl.insertElem(2)
        self.sl.insertElem(3)
        node = self.sl.find(2)
        self.assertEqual(2, node.elem)

    def testFindingAnElementNotInTheList(self):
        self.assertEqual(None, self.sl.find(1))
 
if __name__ == '__main__':
    unittest.main()
    