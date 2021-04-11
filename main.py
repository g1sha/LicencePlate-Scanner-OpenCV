import cv2 as cv
import numpy as np
import imutils
import pytesseract as tess

def ucitajSliku(img_path):
    img = cv.imread(img_path)
    gscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Grayscale ubacene slike 
    cv.imshow("se1", gscale)

    gscale = cv.bilateralFilter(gscale, 13, 30, 30) #Blurovanje nepotrebnih dijelova na slici
    edge = cv.Canny(gscale, 30, 300) # Otkrivanje ivica
    cv.imshow("se2", edge)
    cv.imshow("se", gscale)

ucitajSliku("images/images.jpg") ## Prva slika
#ucitajSliku("images/tabla.jpg") ## Druga slika 

cv.waitKey(0)