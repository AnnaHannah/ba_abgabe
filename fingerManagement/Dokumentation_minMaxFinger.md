## Das ist eine Zusammenfassung von Funktionen welche in dem MinMaxFinger verwendet werden:  

Das Ziel dieser Classe ist es 2 statische Finger zu haben, wo 
- der MiniFinger auf dem kleinsten Node in der Datenstrucktur sitzt und 
- der MaxiFinger auf dem größten Node sitzt.

Folgende Funktionen sind verfügbar:

#### setMaxiFingerFrom (self, tree)
wird benutzt um des Maximum herrauszufinden un den Maxi finger global zu setzen.

#### setMiniFingerFrom(self, tree)
Ananlog wird hier das Minimum gesucht und auf den MiniFinger gesetzt.

#### fingerSearch(self, tree, keyInInt):
Diese Suche hat den Vorteil, dass sie an einer beliegigen Stelle in der Datenstrucktur anfangen kann zu suchen. 
Man muss hier bedenken, diese Funktion interessiert die Laufzeit nicht, sie geht falls der Node nicht gefunden wird, zur Wurzel zurück und macht dort die Wurzelsuche. Daher wird in dieser Fingersuche sich vorher überlegt ob der Wert mit dem Maximalen oder Mininmalen Finger gestartet werden soll. Das wiederum schafft eine bessere Laufzeit.

#### Beispiel Main:

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    bst = RedBlackTree()
    inputList1 = [1,2,3,4]
    bst.insertMultipleElem(inputList1)
    mmf=MinMaxFinger()
    mmf.maxiFinger = mmf.setMaxiFingerFrom(bst)
    mmf.miniFinger = mmf.setMiniFingerFrom(bst)    
    mmf.fingerSearch(bst, 1)
    bst.printTree()