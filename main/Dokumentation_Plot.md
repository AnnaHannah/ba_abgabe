## Das ist eine Zusammenfassung von Funktionen welche Plots verwendet werden  

Die PLots gibts in zwei Ausführungen: für Windows und für Linux.

Folgendes Verfahren ist zu empfehlen

1. GenerateInputLists.py in der Console ausführen
2. GenerateSearchList.py in der Console ausführen
3. PlotsWindos.py ODER PlotsLinux.py in der Console ausführen

Auswirkungen dieser Abfolge:
1. es werden die Such und Input listen in die Datenstrukturen erstellt (hier im plots Ordner abgelegt)
2. für die Plots werden die Datenstrukturen mit den csv dateien aufgefüllt und vermessen, halt um die Plots erstellen zu können


#### 


## --- weniger wichtige Funktionen ---


## --- Beispielcode für main ---
```
if __name__ == "__main__":
    #Je nach dem wie stark die Rechenleistung ist, bitte begrenzen:
    sys.setrecursionlimit(20000)
    #Performance INSERT
    in_listOfLists = readMYfile('inputLists.csv')
    insert_TimeRBT = timePerformanceINSERTRedBlackTree(in_listOfLists)
    in_listOfLists = readMYfile('inputLists.csv')
    insert_TimeSKL = timePerformanceINSERTSkipList(in_listOfLists)
    #Performance ROOTSEARCH
    input_listOfLists = readMYfile('inputLists.csv')
    search_listOfLists = readMYfile('searchLists.csv') 
    search_TimeRBT = timePerformanceSEARCHRedBlackTree(input_listOfLists, search_listOfLists)
    input_listOfLists = readMYfile('inputLists.csv')
    search_listOfLists = readMYfile('searchLists.csv')
    search_TimeSKL = timePerformanceSEARCHSkipList(input_listOfLists, search_listOfLists)
    #Performance FINGER SEARCH
    input_listOfLists = readMYfile('inputLists.csv')
    search_listOfLists = readMYfile('searchLists.csv')
    search_MinMaxFinger_TimeRBT = timePerformanceMinMaxFingerSEARCHRedBlackTree(input_listOfLists, search_listOfLists)
    input_listOfLists = readMYfile('inputLists.csv')
    search_listOfLists = readMYfile('searchLists.csv')
    search_LazyFinger_TimeRBT = timePerformanceLAZYFingerSEARCHRedBlackTree(input_listOfLists, search_listOfLists)
    input_listOfLists = readMYfile('inputLists.csv')
    search_listOfLists = readMYfile('searchLists.csv')
    search_SplayFinger_TimeRBT = timePerformanceSPLAYFingerSEARCHRedBlackTree(input_listOfLists, search_listOfLists)
    # logischer weise hat diese Kennzahl das gleiche format wie List_performanceTime, gut für plot...
    # Anzahl der Input werte auslesen pro Liste
    listOfLists = readMYfile('inputLists.csv')
    numberOfInputValuesRBT = subListLengh(listOfLists)
    listOfLists = readMYfile('inputLists.csv')
    numberOfInputValuesSKL = subListLengh(listOfLists)
    # Actual plot
    # https://www.grund-wissen.de/informatik/python/scipy/matplotlib.html
    fig, ((plt1, plt2), (plt3, plt4)) = plt.subplots(2, 2)
    fig.suptitle('Laufzeiten Rotschwarz Baum und Skiplist')# Plot 1
    plt1.plot (numberOfInputValuesRBT, insert_TimeRBT, 'ro', linestyle='--', label=r'insert time in RedBlackTree')
    plt1.plot (numberOfInputValuesSKL, insert_TimeSKL, 'mo', linestyle='--', label=r'insert time in SkipList')
    plt1.set_ylabel('Time in nano sec 10^(-6)')
    plt1.set_xlabel('Number of values per list from CSV')
    # Plot 2
    plt2.plot (numberOfInputValuesRBT, search_TimeRBT, 'bo', linestyle='--', label=r'Rootsearch time in RedBlackTree ') 
    plt2.plot (numberOfInputValuesSKL, search_MinMaxFinger_TimeRBT, 'go', linestyle='--', label=r'MinMax-Finger-Search time in RedBlackTree') 
    plt2.plot (numberOfInputValuesRBT, search_LazyFinger_TimeRBT, 'ko', linestyle='--', label=r'Lazy-Finger-Search time in RedBlackTree') 
    plt2.plot (numberOfInputValuesRBT, search_SplayFinger_TimeRBT, 'ro', linestyle='--', label=r'SplayTree-Finger-Search time in RedBlackTree')
    plt2.set_ylabel('Time in nano sec')
    plt2.set_xlabel('Number of Values from CSV')
    # Plot 3
    plt3.plot (numberOfInputValuesSKL, search_TimeSKL, 'ko', linestyle='--', label=r'Rootsearch time in SkipList ') 
    plt3.set_ylabel('Time in nano sec')
    plt3.set_xlabel('Number of Values from CSV')
    # Plot 4
    plt4.plot (numberOfInputValuesRBT, search_TimeRBT, 'bo', linestyle='--', label=r'Rootsearch time in RedBlackTree ') 
    plt4.plot (numberOfInputValuesRBT, search_SplayFinger_TimeRBT, 'ro', linestyle='--', label=r'SplayTree-Finger-Search time in RedBlackTree') 
    plt4.set_ylabel('Time in nano sec')
    plt4.set_xlabel('Number of Values from CSV')
    #Legende einblenden:
    plt1.legend(loc='upper left', frameon=True)
    plt2.legend(loc='upper right', frameon=True)
    plt3.legend(loc='upper left', frameon=True)
    plt4.legend(loc='upper right', frameon=True)
    print ("Plot is on Display")
    plt.show()
```    


