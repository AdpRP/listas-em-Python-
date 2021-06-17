# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:56:07 2021

@author: ap
"""
def al():
    
    lista=[]
    colunas0=2
    alunosinseridos=4
    c,d,n,no,si=0
    for i in range(colunas0): #colunas 
        nome=[]
        numero=[]
        nota=[]
    
    for j in range(alunosinseridos): #insercao dos valores nas listas nome numero e nota
        c+=1
        numero.append(c)
        nome.append(input('Digite seu nome: '))
        nota.append(input('Digite a nota: '))
    
    lista.append(numero)
    lista.append(nome)
    lista.append(nota)
    
    print('\n lista completa')
    print('\n',lista,'\n')
    
    for i in range(2):
        while d!=alunosinseridos:
            print('Sigu',numero[d],'Nome',nome[d],'Nota: ',nota[d])
            print("""""")
            d=d+1
        break
        #print('Nome',nome[d],'Nota: ',nota[d])
    for i in range(2):
        while n!=alunosinseridos:
            print('\n Nome',nome[n])
            print("""""")
            n=n+1
    for i in range(2):
        while no!=alunosinseridos:
            print('\n Nota: ',nota[no])
            print("""""")
            no=no+1
    for i in range(2):
        while si!=alunosinseridos:
            print('\n Numero sigu ',numero[si])
            print("""""")
            si=si+1
