# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:24:35 2018

@author: Giovanni
"""

edad = int(input("¿Cuántos años tiene? "))
if edad < 0:
    print("No se puede tener una edad negativa")
elif edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad") 