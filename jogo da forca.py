# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:01:14 2023

@author: balbi
"""
import random

def encontrarLetra(texto,letra):
    posicoes = []
    for pos, e in enumerate (texto):
        if e == letra:
            posicoes.append(pos)
    
    return posicoes
    
def Menu():
    print("------------------------------")
    print("    Bem vindo ao hang-man!")
    print("------------------------------")
    print("Escolha seu tema:")
    print("1- Animais")
    print("2- Frutas")
    opcao = int(input())
    return opcao

animais = ["tatu","cavalo","zebra","cachorro","gato","lagartixa","elefante","tucano","leao","penguim","lesma"]
frutas  = ["maca","pera","laranja","banana","melao","melancia","kiwi","jabuticaba","tomate","tangerina","pitaya","rambutam","jaca","lichia","carambola","kiwano","durian","frutilla branca"]

opcao = Menu()

if opcao==1:
    lista = animais.copy()

if opcao==2:
    lista = frutas.copy()

indice = random.randint(0, len(lista)-1)
palavra = lista[indice]

print("Certo, agora voce possui 6 tentavias para acertar a palavra:")
texto = []
for i in palavra:
    texto.append("*")
    
print(texto)

count = 0
while(count!=6):
    letra = input("letra:")
    if letra in palavra:
        qtd = palavra.count(letra)
        posicoes = encontrarLetra(palavra, letra)
        for i in posicoes:
            texto[i] = letra
    
    print(texto)
    
    if not letra in palavra:
        count+=1
    
    if not "*" in texto:
        print("Parabéns!!")
        break

if(count == 6):
    print("perdeu troxa KKKKK")
    