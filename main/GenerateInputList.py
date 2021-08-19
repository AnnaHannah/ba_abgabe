import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from _socket import close
from _operator import concat
import logging

# Beispiel test fälle mit Listen
# bitte nicht 0 verwenden, das hat komische effekte im Code
data_list = []
#x = [1]
a = list(range(1,25))
b = list(range(1,50))
c = list(range(1,75))
d = list(range(1,100))
e = list(range(1,125))
f = list(range(1,150))
g = list(range(1,175))
h = list(range(1,200))

k = list(range(1,225))
l = list(range(1,250))
m = list(range(1,275))
n = list(range(1,300))
o = list(range(1,325))
p = list(range(1,350))
q = list(range(1,375))
r = list(range(1,400))


# a = list(range(1,2500))
# b = list(range(1,5000))
# c = list(range(1,7500))
# d = list(range(1,10000))
# e = list(range(1,12500))
# f = list(range(1,15000))
# g = list(range(1,17500))
# h = list(range(1,20000))
#
# k = list(range(1,22500))
# l = list(range(1,25000))
# m = list(range(1,27500))
# n = list(range(1,30000))
# o = list(range(1,32500))
# p = list(range(1,35000))
# q = list(range(1,37500))
# r = list(range(1,40000))


def makeBigLists(listOfList):
    print("\n1. Generating with makeBigLists - method is starting")
    ouput_list=[]
    print("2. ... ")
    for i in range(0, len(listOfList)):
        single_list=[]
       
        single_list.append(listOfList[i])
        for j in range(0, len(single_list)):
           
            # make some sublist List funktion here                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            ouput_list.append(single_list[j])
   
# Beispiel um alle Listen anzuhängen  
    #ouput_list.append(x)
    ouput_list.append(a) 
    ouput_list.append(b) 
    ouput_list.append(c) 
    ouput_list.append(d)   
    ouput_list.append(e) 
    ouput_list.append(f) 
    ouput_list.append(g)
    ouput_list.append(h)

    ouput_list.append(k)
    ouput_list.append(l)
    ouput_list.append(m)
    ouput_list.append(n)
    ouput_list.append(o)
    ouput_list.append(p)
    ouput_list.append(q)
    ouput_list.append(r)

    print ("3. Generated number of sublists/Testcase is: ", len(ouput_list))        
    return ouput_list

# erstelle test csv file mit mini data listen:
def writeMYfile(filename, data):
    with open (filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter =',')
        writer.writerows(data)      
    print ("\n-> Done with writing data in", filename)
    

if __name__ == "__main__":
    logging.basicConfig(filename='logFILE-GenerateInputLists.log', encoding='utf-8', level=logging.DEBUG)
    dataForCSV = makeBigLists(data_list)
    # schreibe test1 csv mit datalisten:
    writeMYfile("inputLists.csv", dataForCSV) 
