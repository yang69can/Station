# -*- coding: utf-8 -*-
"""

This is the first script to deal with the stations data.
This code is used for getting the common stations of all rainfall months
and get the new month rainfall distributions for all months 
meanwhile, made other large values into 3270. 

Yang

"""

import numpy as np
import pandas as pd
import glob
import sys


dir = "./"

files = glob.glob("*.TXT")
#print(files)


ss = pd.read_csv(files[0],sep='\s+',header=None)
standss = ss.iloc[:,0]

#np.set_printoptions(threshold=None)

for i in np.arange(len(files)):
    year = files[i][31:35]
    mo   = files[i][35:37]
    a = pd.read_csv(files[i],sep='\s+',header=None)
    b = np.array(a)
    lat = b[:,1]
    lat = lat*0.01
    lon = b[:,2]
    lon = lon*0.01
    stand = b[:,0]
    
    if(mo=='06'):
        lat1 = np.reshape(lat,(int(len(lat)/30),30))
        lon1 = np.reshape(lon,(int(len(lon)/30),30))
        stand1 = np.reshape(stand,(int(len(stand)/30),30))
    if mo=='07' or mo=='08':
        lat1 = np.reshape(lat,(int(len(lat)/31),31))
        lon1 = np.reshape(lon,(int(len(lon)/31),31))
        stand1 = np.reshape(stand,(int(len(stand)/31),31))
        
        
    standss = np.intersect1d(standss,stand1[:,0])
    print(len(standss))
    

del lat,lon,lat1,lon1,year,mo,stand,stand1,a,b
#sys.exit()
for j in np.arange(len(files)):
    print(j)
    year = files[j][31:35]
    mo   = files[j][35:37]
    aa = pd.read_csv(files[j],sep='\s+',header=None)
    bb = np.array(aa)
    lat = bb[:,1]
    lat = lat*0.01
    lon = bb[:,2]
    lon = lon*0.01
    stand = bb[:,0]
    
    data = bb[:,9]
    data = data*0.1
    data = np.where(data>500,3270,data)
    
    
    if(mo=='06'):
        lat1 = np.reshape(lat,(int(len(lat)/30),30))
        lon1 = np.reshape(lon,(int(len(lon)/30),30))
        stand1 = np.reshape(stand,(int(len(stand)/30),30))
        data1 = np.reshape(data,(int(len(data)/30),30))
    if mo=='07' or mo=='08':
        lat1 = np.reshape(lat,(int(len(lat)/31),31))
        lon1 = np.reshape(lon,(int(len(lon)/31),31))
        stand1 = np.reshape(stand,(int(len(stand)/31),31))
        data1 = np.reshape(data,(int(len(data)/31),31))
        
    index = np.in1d(stand1[:,0],standss) 
    
    locate = np.where(index==1)[0]    
    stand2 = stand1[:,0][locate]
    
    
    lat2 = lat1[:,0][locate]
    lon2 = lon1[:,0][locate]
    
    lat2 = np.round(np.floor(lat2)+((lat2-np.floor(lat2))*100/60.0),2)
    lon2 = np.round(np.floor(lon2)+((lon2-np.floor(lon2))*100/60.0),2)
    
    data2 = data1[locate]
    
    
   
    if(mo=='06'):
        dt = np.zeros((len(locate),33))
    if(mo=='07' or mo=='08'):
        dt = np.zeros((len(locate),34))
        
        
    dt[:,0]=stand2
    dt[:,1]=lat2
    dt[:,2]=lon2
    dt[:,3:]=data2
    
   
    np.savetxt("./output1/pr"+str(year)+str(mo)+".txt",dt,fmt='%-10.6s')
    
