# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:04:49 2021

@author: alexa
"""

import pandas as pd
import os
from sequencealignment import SequenceAlignment
from Kmedoids import Kmedoids
from matplotlib import pyplot as plt

caminho=r"C:\Users\alexa\OneDrive\Área de Trabalho\Disciplinas mestrado\02 - Mineração de dados\projeto\atual_total\\"

print(caminho)

file=0
arquivo=caminho + r'\\' + str(file)  + '.csv'
listas=[]

while(os.path.exists(arquivo)):    
    
    data = pd.read_csv (arquivo)
    df = pd.DataFrame(data, columns= ['Event','Element Id'])
    dt = df.rename(columns={'Element Id': 'Element'}, inplace=False)
#    print(dt)
    lista=[]
    
    for i in range(len(df)):
        lista.append(df.Event[i]+ " "+ dt.Element[i])
    listas.append(lista)

    file=file+1
    arquivo=caminho + r'\\' + str(file)  + '.csv' 
 #   print(lista)
matriz_dist=[]
for i in range(len(listas)): 
    vetor_dist=[]
    for j in range(len(listas)):
        sqalign = SequenceAlignment(listas[i], listas[j])
   #     min_edit, steps = sqalign.alignment()
        min_edit = sqalign.alignment()
        vetor_dist.append(min_edit)
    matriz_dist.append(vetor_dist) 
    print(vetor_dist)
    
I=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
SWCk=[]
SWC=[]
kiniciais=[]
kinicial=[]
melhorgrupo=[]
melhork=[]
ki=16

for i in I:
    for kin in range(ki):
    
        teste=Kmedoids(matriz_dist, i)
        k=teste.iniciaKs(kin)
        kiniciais.append(k)
        grupos, k = teste.EfetuaIteracoes(5)
        grupos, k = teste.EliminaKs()
        melhorgrupo.append(grupos)
        melhork.append(k)
        swc = teste.EncontraSilhueta()
        SWCk.append(swc)
                   
        
    indicek=SWCk.index(max(SWCk))
    print(melhorgrupo[indicek])
    print(melhork[indicek])
    print(SWCk[indicek])
    kinicial.append(kiniciais[indicek])
    SWC.append(SWCk[indicek])
    kiniciais=[]
    SWCk=[]
    melhorgrupo=[]
    melhork=[]

print(kinicial)
plt.plot( I, SWC, label='linear')
plt.xlabel('Nº de grupos')
plt.ylabel('Largura de silhueta')
plt.show()

        
        