#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 07:42:11 2022

@author: edgartarraga
"""

import cv2
import numpy as np
import os

Clasifica_Cara = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
Clasifica_Ojos = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye_tree_eyeglasses.xml')
captura = cv2.VideoCapture(0)

while (captura.isOpened()):
    ret,Imagen = captura.read()
    Filas,Columnas,Canales=Imagen.shape
    Min_SizeFila=round(0.2*Filas)
    Min_SizeCol=round(0.2*Columnas)
    Max_SizeFila=round(0.8*Filas)
    Max_SizeCol=round(0.8*Columnas)
    if ret == True: ## Si hay imagen si  continua
        imag_gray = cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)
        Detecta_cara = Clasifica_Cara .detectMultiScale(imag_gray, 1.2, 5)
        ## Se obtenie los limites de la cara
        cordx=Detecta_cara[0,0] # corrdenadas de columnas
        cordy=Detecta_cara[0,1]
        ancho_cara=Detecta_cara[0,2]
        largo_cara=Detecta_cara[0,3]
        y_ojos=round(cordy+0.1*largo_cara)
        sector_ojos=round(0.6*largo_cara)
        Cuadro_cara=Imagen[cordy:cordy+sector_ojos,cordx:cordx+ancho_cara] 
        Cara_Gray=cv2.cvtColor(Cuadro_cara, cv2.COLOR_BGR2GRAY)
        Ojos = Clasifica_Ojos.detectMultiScale(Cara_Gray)
        for (ex,ey,ew,eh) in Ojos:
            cv2.rectangle(Cuadro_cara,(ex,ey),(ex+ew,ey+eh),(0,200,0),2)
        cv2.imshow('Cuadro CARA', Cuadro_cara)
        if cv2.waitKey(1) & 0xFF == ord('q'): ###Si tecla ccionada es q quit termina
            cv2.destroyAllWindows()
            cv2.waitKey(1) # Espera cierre de pantallaq
            break
captura.release()                