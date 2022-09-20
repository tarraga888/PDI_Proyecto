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
        Detecta_cara = Clasifica_Cara .detectMultiScale(imag_gray, 1.3, 5)
        ## Se obtenie los limites de la cara
        cordx=Detecta_cara[0,0]
        cordy=Detecta_cara[0,1]
        largo=Detecta_cara[0,2]
        ancho=Detecta_cara[0,3]
        Cuadro_cara=Imagen[cordy:cordy+ancho,cordx:cordx+largo] 
        cv2.imshow('Cuadro CARA', Cuadro_cara)
        if cv2.waitKey(1) & 0xFF == ord('q'): ###Si tecla ccionada es q quit termina
            cv2.destroyAllWindows()
            cv2.waitKey(1) # Espera cierre de pantalla
            break
captura.release()                