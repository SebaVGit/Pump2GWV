# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:35:46 2020

@author: SVazquez
"""
#------------------Imports
import os
import pandas as pd
from tqdm import tqdm

#----------time-------------------
import time
t = time.time()

#--------------Presentación-------------------------------
presentacion='Developed by Sebastián V. G.\nPumping2GWV Script v1'
print(presentacion)

#-------------directory------------------
Ruta = os.getcwd() + '\\'
#nombre_archivo=input('Nombre del archivo excel: ')
nombre_archivo='CaudalToGWV'
directory =  Ruta + nombre_archivo + '.xlsx'

#--------------Nombre archivo de guardado------------
#archivo_guardado=input('Nombre del archivo de guardado: ')
archivo_guardado='PumpOut_2GWV'
#-----------Read_Excel---------------------
pump=pd.read_excel(directory,'Caudal',names=[0,1,2]) #los números representan las columnas de la hoja excel
aux=pd.read_excel(directory,'Info_Pozos',names=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]) #los números representan las columnas de la hoja excel

#------------------Generate_Dictionary-------------------------------
dic={}
for i in pump[0].unique():
    dic[i] = [(pump[2][j], round(pump[1][j],3)) for j in pump[pump[0]==i].index]
#dic=dict(sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))) 
for well in dic:
    dic[well]=sorted(dic[well]) # Para ordenar la data en caso de que este desordenada

#---------------------Create_New_Dataframe----------------------
df=pd.DataFrame(columns=['Pozo', 'Este', 'Norte', 'Layer_Top','Layer_Bot', 'NumTrans','Rw', 'LossType','PumpLoc','Zpump','Skin','Kskin',
                         'Qlimit','PumpLevel','Reach'])

#----------------------Read Wells and check data----------------
indice1=0 #sera el que vea el i como número para recorrer el arcivho auxiliar
indice2=1 #sera el variable para ir pegando los datos
acum=0  #acumulación de indice
'''
Nota del archivo de caudales
Se ocupa el incide j para recorrer cada uno de los periodos de stress.
Ahora bien, se utiliza el "num_aux" para recorrer los datos de caudales
presentes en cada pozo, dado que a veces existen vacios y lo más importante
es que no siempre se ajusta la dimensión de los periodos de stress con
la dimensión de los datos de caudal.
'''

for i in tqdm(aux[0]): #locate all wells
    lst=[] #list auxiliar para saber si encuentra o no el periodo de stress
    num_aux=0 #será el índice de los datos presentes en cada pozo
    num=aux[5][indice1] #numero de datos, en este caso NumTrans
    df.loc[acum,'Pozo']=i
    df.loc[acum,'Este']=aux[1][indice1]
    df.loc[acum,'Norte']=aux[2][indice1]
    df.loc[acum,'Layer_Top']=aux[3][indice1]
    df.loc[acum,'Layer_Bot']=aux[4][indice1]
    df.loc[acum,'NumTrans']=aux[5][indice1]
    df.loc[acum,'Rw']=aux[6][indice1]
    df.loc[acum,'LossType']=aux[7][indice1]
    df.loc[acum,'PumpLoc']=aux[8][indice1]
    df.loc[acum,'Zpump']=aux[9][indice1]
    df.loc[acum,'Skin']=round(aux[10][indice1],3)
    df.loc[acum,'Kskin']=round(aux[11][indice1],3)
    df.loc[acum,'Qlimit']=aux[12][indice1]
    df.loc[acum,'PumpLevel']=aux[13][indice1]
    df.loc[acum,'Reach']=aux[14][indice1]
    for n in range(0,len(dic[i])):
        lst.append(dic[i][n][0])
    for j in range(0,num):
        df.loc[indice2,'Pozo']=j+1
        df.loc[indice2,'Este']=j+1
        if j+1 not in lst:
            df.loc[indice2,'Norte']=0
            df.loc[indice2,'Layer_Top']=0
        else:
            try:
                df.loc[indice2,'Norte']=round(dic[i][num_aux][1],3)
                df.loc[indice2,'Layer_Top']=0
                num_aux+=1
            except IndexError:
                pass
        indice2+=1
    indice1+=1
    acum=indice2+1
    indice2=acum+1
#---------------save csv-------------------------------
#df.to_csv(archivo_guardado+'.csv',sep='\t',index=False)
df.to_csv(archivo_guardado+'.csv',index=False) #aquí se guardará como csv

#-----------elapsed time---------------------------------------------
print('Tiempo de corrida: '+str((time.time()-t)//60)+' minutos y '+('%.1f' %((time.time()-t)-60*((time.time()-t)//60)))+' segundos.')