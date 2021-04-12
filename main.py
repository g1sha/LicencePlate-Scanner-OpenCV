import cv2 as cv
import numpy as np
import imutils
import pytesseract as tess


def detektujTablicu(img):
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

def cropCetvrtina(img):
    cropCV_1 = img[0:(img.shape[0]//2), 0:(img.shape[1]//2)]
    cropCV_2 = img[(img.shape[0]//2):(img.shape[0]), (img.shape[1]//2):(img.shape[1])]
    cropCV_3 = img[(img.shape[0]//2):(img.shape[0]), 0:(img.shape[1]//2)]
    cropCV_4 = img[0:(img.shape[0]//2), (img.shape[1]//2):(img.shape[1])]

    cv.rectangle(img,((img.shape[1]//2),0), ((img.shape[1]), img.shape[0]//2), (0,255,0),thickness=2)
    cv.putText(img, "Polje za crop 1/4 slike", ((img.shape[1]//2)-110, (img.shape[0]//2)-10), cv.FONT_HERSHEY_PLAIN, 0.5, (0,255,0), 1)
    cv.imshow("crop1", cropCV_1)
    cv.imshow("crop2", cropCV_2)
    cv.imshow("crop3", cropCV_3)
    cv.imshow("crop4", cropCV_4)
    #detektujTablicu(cropCV_4)

img = cv.imread('images/pd.jpg') ## UCITAVANJE SLIKE !
## SPLIT SLIKU U DIJELOVE
cropCetvrtina(img)


detektujTablicu(img)
cv.waitKey(0)