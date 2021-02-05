# -*- coding: utf-8 -*-
"""
Get the threshold of precipitation in the record

Yang
"""

import numpy as np
import pandas as pd
import sys
import glob

dir="./output1/output2/output3/"
files=glob.glob(dir+"newpr*.txt")

print(files)


array = []
for i in range(len(files)):
    print(files[i])
    a = pd.read_csv(files[i],header=None,sep="\s+")
    b = np.array(a)
    print(b.shape)
    lat = b[:,1]
    lon = b[:,2]
    
    index = np.where((lat>=27)&(lat<=33.5)&(lon>=110)&(lon<=122.5))
    
    
    lat1 = lat[index[0]]
    lon1 = lon[index[0]]
    
    data = b[index[0],3:]
    
    data1 = np.where(data==3270.0,np.nan,data)
    data2 = np.nanmean(data1,axis=0)
    
    for j in range(len(data2)):
        array.append(data2[j])
   

print("***********")
print(len(index[0]))
print("&&&&&&&&&&&&")
array1 = np.array(array)
array2 = np.array(sorted(array1,reverse=True))


indexth90 = int(np.ceil(len(array2)*0.1))
indexth95 = int(np.ceil(len(array2)*0.05))
indexth99 = int(np.ceil(len(array2)*0.01))
# print(indexth90)
# print(indexth95)
# print(indexth99)

Th90 = array2[indexth90]
Th95 = array2[indexth95]
Th99 = array2[indexth99]

print("%.1f" %Th90)
print("%.1f" %Th95)
print("%.1f" %Th99)




