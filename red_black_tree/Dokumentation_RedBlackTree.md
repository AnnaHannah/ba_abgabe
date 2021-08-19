## Das ist eine Zusammenfassung von Funktionen welche in dem Rot Schwarz Baum verwendet werden:  

Allgemein der RotSchwarzBaum besteht aus Nodes welcher in einer Binärbaum Strucktur zusammengestellt werden. Kleinere Werte der Nodes werden nach rechts und größere nach Links einsortiert.

Folgende Funktionen sind verfügbar:

#### bst = RedBlackTree()
init/Initiation von leerem rot-Schwarz Baum

#### inputList = [1, 2, 3, 4, 5, 6]
Empfohlen den Input als Liste zudefinieren, besonders für die folgende funktion: insertMultipleElem

#### bst.insertMultipleElem(inputList)
So kann man mehere Elementen aus der Liste in den RS-Baum einfügen, Achtung: Beschränkung wurde auferlegt, dass nur Integer als Input zugelassen sind. Farbe wird automatisch nach korrigiert.

#### deleteFullTree (bst) - 
löscht den gesammten Baum und löscht alle Nodes

#### bst.downSearchTree(key)
Sucht was für node data bei dem Key abgelegt wurde, dies Suchrichtung ist immer nach unten richtung leaf.

#### bst.rootSearchTree(key)
klassische Wurzelsuche nach element.

#### bst.twoDirectSearch(startNode, key)
Diese Suche startet an einem beliebigen Startnode, sucht immer nach unten und wenns den passnedenNode nichgt findet, dann geht Sie eine Ebene höher.

#### bst.deleteNode(1)
Löscht den Node mit dem Wert 1 aus BST

#### bst.maximumInTree()
Gibt das Größte Node zurück, was jemals abgelegt wurde. Nicht den wert des Nodes, das ist wichtig für Fingersuche ...

#### bst.minimumInTree()
Analog zu maximumInTree()


#### bst.printTree()
Nutzt vorallem die print Funktion um in der Konsole einen Baum zuprinten.




## --- weniger wichtige Funktionen ---

#### bst.nodesInTree()
Gibt die Anzahl der Nodes zurück, welche aktuell im Baum enthalten sind.

#### bst.preorder()
Gibt die eingetragenen Zahlen preoder gelesen heraus

#### bst.inorder()
Gibt die eingetragenen Zahlen inorder gelesen heraus

#### bst.postorder()
Gibt die eingetragenen Zahlen postorder gelesen heraus

#### bst.getRoot()
Gibt die aktuelle Wurzel des Baumes zurück

#### bst.leftRotate(x)
Linksrotation um die Node x im BST

#### bst.rightRotate(x)
Rechtsrotation um die Node x im BST

#### bst.insert(1)
die 1 als Integer wird in den BST reingetan

#### bst.fixColor()
Rot schwarz Baum wird Rotschwarz, doppelt kontrolliert

#### nodesInTree()
Gibt die Anzahl der Nodes zurück

#### bst.contains(key)
Beantwortet die Frage ob ein element in der Datenstrucktur hinterlegt ist oder nicht.

#### bst.findMaximum(key)
Sucht ein größereres Maximum als der übergebene key.

#### bst.findMinimum(key)
Analog zu findMaximum




## --- Beispielcode für main ---

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    # print("1. Recursion allowed in this program:", sys.getrecursionlimit())
    inputList1 = [4,5,6,7,8,9,1,1,2,3,1000000000]
    searchList = [1,2,3,4,5,6,7,1,2,1,1,1,1,1,1,1]
    bst = RedBlackTree()
    # print("2. Number of Nodes now is: ", bst.counterNodes)
    print("Input in den Tree:", inputList1)
    bst.insertMultipleElem(inputList1)
    startNode = bst.root.left
    print(" start Node for search in twoDirectSearch: ", startNode.data)
    print("\n gefunden mit twoDirectSearch: " , bst.twoDirectSearch(startNode, 2))
    print("\n gefunden mit RootSearchTree: " , bst.rootSearchTree(3))
    #bst.findMultipleElem(searchList)
    #print ("Ergebnis von Suche bst.findMultipleElem ("+ str(searchList) +") ist:", bst.findMultipleElem(searchList) )   
    # print ("das wird gesucht: bst.RootSearchTree(5)", bst.RootSearchTree(5))
    # print ("das wird gesucht: bst.contains(0)", bst.contains(0))
    # print("4. Number of Nodes now is: ", bst.counterNodes)
    # print ("5. Number of black and red color fixes: " + str(mBcounter) + " and " + str(mRcounter))        
    print("\n")
    bst.printTree()
    # bst.maximumInTree()
    # bst.minimumInTree()

