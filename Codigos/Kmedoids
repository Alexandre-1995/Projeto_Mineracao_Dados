# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 14:56:27 2021

@author: alexa
"""
import numpy as np


class Kmedoids(object):

    def __init__(self, dists, N):
        self.dists=dists
        self.N=N
        self.k=[0]*self.N
        self.grupos=[[]]*self.N
        
    def iniciaKs(self,ki):
        
   #     self.k[0]=random.randrange(1,(len(self.dists)),-1)
        self.k[0]=ki
        i=1
        while i <= (self.N-1):
            
            soma=[0]*len(self.dists)
            
            for j in range(i):                
                for m in range(len(self.dists)):
                    soma[m]=soma[m]+self.dists[m][self.k[j]]
            
            self.k[i]=soma.index(max(soma))
            
            i=i+1       
        return self.k
        
    def __AtribuiObjetos(self):        
        
        atribuicao=[]
        for i in range(len(self.dists)):        
            menor=[]
            for j in self.k:
                menor.append(self.dists[i][j])
            
            atribuicao.append(self.dists[i].index(min(menor)))
        
        
        for j in range(self.N):
            grupo=[]
            for i in range(len(atribuicao)):

                if atribuicao[i]==self.k[j]:
                    grupo.append(i)
                    
            self.grupos[j]=grupo
                    
        
    def __EncontraMedoide(self):
        
        for i in range(len(self.grupos)):
            soma=[0]*len(self.grupos[i])
            m=0
            for j in self.grupos[i]:
                for n in self.grupos[i]:
                    soma[m]=soma[m]+self.dists[j][n]
                m=m+1
                    
            self.k[i]=self.grupos[i][soma.index(min(soma))]
                    
            
    def EliminaKs(self):
        
        newk=[]
        lenkant=len(self.k)
        lenk=0
        
        while lenkant > lenk :
            
            lenkant=len(self.k)
            
            for i in range(len(self.k)):
            
                if not self.k:
                    break
            
                else:
                    newk.append(self.k.pop())
                    B=len(self.k)
                
                for j in range(B):                
                
                    if newk[i]==self.k[j] :                    
                        self.k.remove(self.k[j])
                        self.grupos.remove(self.grupos[j])  
                        break      
                    
            lenk=len(self.k)
            
        for x in range(len(newk)):        
            self.k.append(newk.pop()) 
        
        return self.grupos, self.k
        
    def EfetuaIteracoes(self, maxiter):
        kant=[]
        kant.append(self.k)
        kant=np.array(kant)
        limiar=np.array([1, 1])
        
        for i in range(maxiter):
            kseg=[]
            self.__AtribuiObjetos()
            self.__EncontraMedoide()
            
            kseg.append(self.k)
            kseg=np.array(kseg)
            
            dif=abs(kant-kseg)
            
            kant=kseg
            
            if dif.all() <= limiar.all():
                break

        return self.grupos, self.k
                  
    def EncontraSilhueta(self):
        
#        a=[0]*len(self.dists)
        a=[]
        b=[]
        
        for i in range(len(self.grupos)):
            a.append([])
            b.append([])
            for j in range(len(self.grupos[i])):
                bdist=[]
                
                a[i].append(self.dists[self.grupos[i][j]][self.k[i]])
                

                for n in self.k:
                    if n!=self.k[i]:
                        bdist.append(self.dists[self.k[i]][n])
                        
                        minbk=self.dists[self.k[i]].index(min(bdist))
                        
                b[i].append(self.dists[self.grupos[i][j]][minbk])
                
        s=[0]*len(self.dists)
        for i in range(len(self.grupos)):
            
            if len(self.grupos[i])==1:
                s[self.grupos[i][0]]=0
            else:
                for j in range(len(self.grupos[i])):       
                    
                    num=b[i][j]-a[i][j]
                    den=max(b[i][j], a[i][j])
                    
                    s[self.grupos[i][j]]=num/den
            
        NUM=0
        for i in range(len(s)):
            NUM=NUM+s[i]
        
        SWC=NUM/len(s)
            
        return SWC
                
        
    