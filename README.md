Das ist der praktische Teil von meiner Bachelorarbeit. 

---

Um meinen Code auszuführen, empfehle ich die Vorgehensweise:
1.	Bitte den Ordner /main öffnen.
2.	Diese 2 files auszuführen: GenerateInputLists.py und GenerateSearchLists.py
3.	Nun haben die Fingersuchen zwei .csv files für die Initialisierung
4.	Dann im selben Ordner PlotsCounterWindows.py auszuführen, dieses Skript verwendet die verschiedenen Arten der Fingersuche.
5.	Jetzt erscheint ein Plot im neuen Fenster

Diese Plots sind auch die gleichen verwendeten Plots in der Bachelorarbeit und in der schriftlichen Ausarbeitung disskutiert.

---
## Abstract
In dieser Bachelorarbeit geht es um externe Pointer, auch Finger genannt, und wie man den Suchprozess in Datenstrukturen durch sie beschleunigen kann. Die Laufzeiten der Such-Funktion können durch zusätzliche Finger in einer Datenstruktur z.B. bei Bäumen von O(log n) auf O(log d) [1] reduziert werden. Diese Art der Suche heißt Distanzsuche, da der Suchauftrag mit einer gewissen Distanz zur Wurzel startet. 
Das Ziel dieser Arbeit ist eine Simulation der Fingersuche zu implementieren, in der sich drei Fingersuchen in Abhängigkeit von fünf Suchaufträgen im Vergleich zum Benchmark der Wurzelsuche messen lassen. 
Es wird außerdem eine theoretische Betrachtung geboten, wie die Anzahl der Finger bei der Fingersuche begrenzt werden kann. Es wird ein „gekürzter“ Splay-Tree als möglicher Algorithmus aus dem Model geschlussfolgert, welcher die Informationen aus den vergangenen Suchen besonders gut nutzen kann.

Genauere Details sind hier in der schriftlichen Bachelorarbeit zu finden.

## Abstract - English
This bachelor thesis is about external pointers, also called fingers, and how to use them to speed up the search process in data structures. The runtime of the search function can be reduced from O (log n) to O (log d) [1] using extra fingers in a data structure, e.g. in trees. This type of search is called a distance search, as the search task starts a certain distance from the root.
The aim of this work is to implement a simulation of the finger search, where 3 finger searches are performed based on 5 search requests which will be compared to the benchmark root search. 
A section is dedicated to theoretical considerations of how the number of fingers used for a search can be limited. A “shortened” Splay-Tree is concluded from the model as a possible algorithm, which is able to use the information from previous searches in a very effective way.

More details can be found here in the written bachelor thesis.

---
Für mich:
#### Probleme, die behoben werden können:

- Skiplist two direkt search implementieren
- Red Fingersearch
- Splaytree kürzen (ShortSplayTree.py)

#### Refractoring:
- wie UML Diagram -> Abstrakte Klassen: Fingermanagement und Finger 
