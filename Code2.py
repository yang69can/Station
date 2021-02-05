# -*- coding: utf-8 -*-
"""
This is the second script to further select the station that:  
1) remove the station if the data is the missing value in the whole month
2) remove the station if the record of missing value value more than 10%

Yang
"""

import numpy as np
import pandas as pd
import glob
import sys


dir1 = "./output1/"
dir2 = "./output1/output2/"
dir3 = "./output1/output2/output3/"

files = glob.glob(dir1+"pr*.txt")



#intentify the missing value in the whole month
index = []
for i in range(len(files)):
    print(files[i])
    a = pd.read_csv(files[i],header=None,sep='\s+')
    b = np.array(a)
    
       
    stand = b[:,0]
    lat = b[:,1]
    lon = b[:,2]
    data = b[:,3:]

    
    for j in range(data.shape[0]):
        if(sum(data[j,:])==0):
            continue
        if(sum(data[j,:])/len(data[j,:])==3270):
           print("***************")
           index.append(j) 

del i,a,b,lat,lon,data

print(index)
for i in range(len(files)):
    print(files[i])
    year = files[i][12:16]
    mo   = files[i][16:18]
    a = pd.read_csv(files[i],header=None,sep='\s+')
    b = np.array(a)
    
    newdata = np.delete(b,index,axis=0)
    np.savetxt(dir2+"pr"+str(year)+str(mo)+".txt",newdata,fmt='%-10.6s')
    


#intentify the missing value more than 10% in all months
del i,year,mo,a,b,newdata,index



file1s = glob.glob(dir2+"pr*.txt")

a1 = pd.read_csv(file1s[0],header=None,sep='\s+')
b1 = np.array(a1)
data1 = b1[:,3:]
for i in range(len(file1s)):
    if(i+1==len(file1s)):
        continue
    
    a = pd.read_csv(file1s[i+1],header=None,sep='\s+')
    b = np.array(a)

    data = b[:,3:]
    data1 = np.column_stack((data1,data))
    
    
    print(data1.shape)

number=np.sum(data1==3270.0,axis=1)
ncol = data1.shape[1]

PrecentMiss = number/ncol*100
index = np.where(PrecentMiss >= 15.0)[0]
print(index)

del i,a,b,data,data1,number,ncol
#find the location where the missing value over the 15% during the whole period


for i in range(len(file1s)):
    name = file1s[i][18:31]
    a = pd.read_csv(file1s[i],header=None,sep='\s+')
    b = np.array(a)
    
    newdata = np.delete(b,index,axis=0)
    np.savetxt(dir3+"new"+name,newdata,fmt='%-10.6s')


        
    