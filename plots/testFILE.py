import numpy as np
import matplotlib.pyplot as plt
import csv
from numpy.core.arrayprint import IntegerFormat
from fileinput import filename
import time 
from datetime import timedelta
import datetime
from numpy.core.defchararray import isdigit, isdecimal, isnumeric
from decimal import Decimal  
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from _socket import close
from _operator import concat
from matplotlib.pyplot import title
from unicodedata import numeric
from numpy import double

# my files BAUSTELLE
import GenerateInputList
import GenerateSearchList
import sys 



def map_lists(in_listOfLists, se_listOfLists, func):
    result = []
 
    while len(in_listOfLists) > 0 and len(se_listOfLists) > 0:
        x = in_listOfLists.pop()
        y = se_listOfLists.pop()
        
        z = func(x, y)
        
        result.append(z)
    return result

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    # print("1. Recursion allowed in this program:", sys.getrecursionlimit())
    
    x_list = [[2],[1,2,3,5,5],[],]
    y_list = [[12],[1,1,1,1],[1,2,3,4,4],[3]]
    (map_lists (x_list,y_list, print))