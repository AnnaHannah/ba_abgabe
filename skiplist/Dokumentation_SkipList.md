## Das ist eine Zusammenfassung von Funktionen welche in der Skiplist verwendet werden:  

Allgemein, die Skiplist besteht aus Nodes welche nach Zufall in eine Strucktur zusammengestellt werden. Skpilisten werden aus Linked Lists erstellt. Durch das zufällige Wesen der Skiplisten werden sie fast jedes Mal durch das erstellen mit den gleichen Werten unterscheidlich hoch un auch aufgebaut sein.

Folgende Funktionen sind verfügbar:

#### skl = SkipList()
init für Skiplisten.

#### inputList = [1, 2, 3, 4, 5, 6]
Empfohlen den Input als Liste zudefinieren, besonders für die folgende funktion: insertMultipleElem

#### skl.findElem(2)
Sucht und findet die Zahl 2 in der Skipliste. 

#### skl.findMultipleElem(2)
Diese Funktion nimmt eine Liste entgegen und gibt eine Liste zurück. die Inputliste  - da wird jedes element einzeln gesucht, falls es gefunden wird, wird es in die Outputliste getan.

#### skl.findNodeByElem (elem, node)
Subfunktion beim insert, dass mna nicht doppelt inserted.

#### skl.contains(2)
Boolean funktion ob eine Zahl enthalten ist oder nicht.

#### skl.randomHeight
Ist die Randomfunktion, die bestimmt ob eine neue Ebene eröffnet werden soll oder nicht. wird mit update funktionen verwendet.

#### skl.updateList (elem, node)
Diese funktion gibt einem Element den Platz in einer Ebene.

#### skl.insertElem(elem)
Fügt ein einzelnes Element in die Skipliste ein. Sie verlegt auch die richtigen Pointer.

#### skl.insertMultipleElem([1,2,3,4,5])
Diese funktion ist wie insertElem() nur nimmt sie Listen entgegen. Keine Rückgabe.

#### skl.delete(2)
Die Zahl 2 wird aus der Skipliste entfernt und die Skipliste neu aufgebaut.

#### skl.printList()
Stellt eine Consolendarstellung der Ebenen und Elemente da.

#### skl.__len__()
Gibt die länge der Untersten Liste-Ebene zurück.


## --- Beispielcode für main ---
```
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
```
