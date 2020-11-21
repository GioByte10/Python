#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:46:56 2018

@author: diegoesquivel
"""

nombre = input("Cual es tu nombre? ")

edad = input("Cual es tu edad? ")

agua_necesaria = input("Normlamente cuanta agua consumes en un dia? ")

if agua_necesaria == "1":
    respuesta_litros= input("Consumes " + agua_necesaria + " litro al dia? ")
else:
    respuesta_litros= input("Consumes " + agua_necesaria + " litros al dia? ")

if respuesta_litros == "si" or "SI" or "Si"  "sI":
    print("Gracias.")
else:
    agua_necesaria = input("Normlamente cuanta agua consumes en un dia? ")
    
disponible = input("Cuanta agua tienes disponible en el momento ? (tu respuesta estara en litros) ")
respues_dias = input("Supongamos que estas en un naufragio, cuantos dias estaras en el naufragio? ")

print("normalmente lo minimo que un ser humano necesita de agua para vivir es 0.8 lts ")

cantidad_necesaria = float(respues_dias) * float(0.8)

dias_vividos = float(respues_dias) * float(disponible) / float(cantidad_necesaria)

if float(dias_vividos) > float(respues_dias):
    dias = float(dias_vividos) - float(respues_dias)
    print("Enhora buena, " + str(nombre) + " sobreviviste los " + str(respues_dias)+ " dias, en incluso te sobraron " + str(dias) + " dias ")
elif float(dias_vividos) == float(respues_dias):
    print("Tienes el agua exacta")
elif float(dias_vividos) < float(respues_dias):
    dias = float(respues_dias) - float(dias_vividos)
    print("Siento decirte, " + str(nombre) + " pero solo viviras " + str(dias_vividos)+ " dias.")
    print("te faltaron " + str(dias) + " dias.")