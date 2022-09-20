#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 07:42:11 2022

@author: edgartarraga
"""

import cv2
import numpy as np

captura = cv2.VideoCapture(0)

while (captura.isOpened()):
    ret,Imagen = captura.read()

    if ret == True: ## Si hay imagen si  continua
        cv2.imshow('Cuadro Completo',Imagen)
        if cv2.waitKey(1) & 0xFF == ord('q'): ###Si tecla ccionada es q quit termina
            cv2.destroyAllWindows()
            cv2.waitKey(1) # Espera cierre de pantalla
            break
captura.release()                