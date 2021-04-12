import cv2 as cv
import numpy as np
import imutils
import pytesseract as tess



img = cv.imread('images/golf2.jpg')
img = cv.resize(img, (500,300) )

cv.imshow('Full Original',img)


blnkSc = None

gscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
gscale = cv.bilateralFilter(gscale, 13, 15, 15) 

cv.imshow('BNW Original',gscale)

ivice = cv.Canny(gscale, 30, 200) 

cts = cv.findContours(ivice.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cts = imutils.grab_contours(cts)
cts = sorted(cts, key = cv.contourArea, reverse = True)[:10]

for x in cts:
    kriva = cv.arcLength(x, True)
    poligon = cv.approxPolyDP(x, 0.020 * kriva, True)

    if len(poligon) == 4:
        blnkSc = poligon
        break

cv.drawContours(img, [blnkSc], -1, (0, 0, 255), 3)

mask = np.zeros(gscale.shape,np.uint8)
kopija = cv.drawContours(mask,[blnkSc],0,255,-1,)
kopija = cv.bitwise_and(img,img,mask=mask)

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
tablica = gscale[topx:bottomx+1, topy:bottomy+1]

img = cv.resize(img,(500,300))
tablica = cv.resize(tablica,(400,200))
cv.imshow('Tablica',tablica)
cv.imshow('Full Original detektovana',img)

cv.waitKey(0)