#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:50:48 2019

@author: nathanperney
"""

import numpy as np

#Schéma du graphe web
graphe = np.array([[0,1,1,0],[0,0,1,0],[1,0,0,0],[0,0,1,0]])

#Initialisation du pageranking
pagerank = [1,1,1,1]

#Mémoire tampon
pagerank_tampon = pagerank     
    


def fonction_pagerank(pagerank,damping,iteration):
    
    #Tableau final
    pagerank_final = [["numéro de la page","pageranking"]]
    
    for k in range (0,iteration-1):
        pagerank_tampon[0] = (1-damping) 
        for i in range(0,4):
            if graphe[i][0]==1 :
                pagerank_tampon[0] += damping*(pagerank[i]/np.sum(graphe,axis=1)[i])
        
        pagerank_tampon[1] = (1-damping) 
        for i in range(0,4):
            if graphe[i][1]==1 :
                pagerank_tampon[1] += damping*(pagerank[i]/np.sum(graphe,axis=1)[i])
        
        pagerank_tampon[2] = (1-damping) 
        for i in range(0,4):
            if graphe[i][2]==1 :
                pagerank_tampon[2] += damping*(pagerank[i]/np.sum(graphe,axis=1)[i])
        
        pagerank_tampon[3] = (1-damping)
        for i in range(0,4):
            if graphe[i][3]==1 :
                pagerank_tampon[3] += damping*(pagerank[i]/np.sum(graphe,axis=1)[i])
       
        pagerank = pagerank_tampon
        
    for k in range (0,4):
        pagerank_final.append([k+1,pagerank[k]])
        
    return (pagerank_final)
    
print(fonction_pagerank(pagerank, 0.85, 20))


    
