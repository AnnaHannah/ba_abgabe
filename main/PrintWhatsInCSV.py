# dieses Python file hat keinen tiefen sinn, als dass es mir übung gegeben hat, wie man csv reader und writer verwenden kann
# dieses Konzept ist bestimmt auch an anderen Stellen nützlich

from numpy.core.defchararray import isdigit, isdecimal, isnumeric
from decimal import Decimal  
import csv
import os
import sys
import re
from _csv import QUOTE_NONNUMERIC
from numpy.f2py.auxfuncs import ischaracter
from ntpath import split
from numpy.distutils.tests.test_npy_pkg_config import simple
from time import *
import time

data_list = [[11,22,33,44,55], [5,6,7,8,9,0], [0,0,0,0,0,0,0]]

# erstelle test csv file mit mini data listen:
def writeMYfile(filename):
    with open (filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter =',')
        writer.writerows(data_list)


# Ziel der funktion, file öffnen, alle Listen auslesen, alle stringsauslesen und in INT convertieren, 
# Liste von Listen zurückgeben

def readMYfile(filename):
    with open( filename) as csv_file:
        reader=csv.reader (csv_file, delimiter=',', skipinitialspace=True)
        
        output_list =[]
        line_count = 0
        
        for line in reader:
            new_list = []
            new_list.append(line)
            # entfernen von extra klammern
            simple_list = new_list.pop()
            # Alle string in liste zu INTEGER
            for i in range(0, len(simple_list)):
                simple_list[i]= int(simple_list[i])
            output_list.append(simple_list)
            
            line_count +=1
        print ("output_list after reading file (integer)", output_list)
        return output_list


def readWritePerformaveClock(): 
    start = time.process_time_ns()
    for i in range(0,100):
        i=i*i
        print (i)
    sleep = 10 
    stop = time.process_time_ns()
    delta_time=0.0
    delta_time = start - stop
    print (" start- end time:", delta_time)
    
    
      
if __name__ == "__main__":
    # writeMYfile("test1.csv") 
    #lines=readMYfile("test1.csv") 
    readWritePerformaveClock() 
    