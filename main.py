import cv2 as cv
import numpy as np
import imutils
import pytesseract as tess
import re
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detektujTablicu(img):
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

    if blnkSc is None:
        detected = 0
        cropCetvrtina(img)
        print ("Nije detektovana tablica")
        return
    else:
        detected = 1
    if detected == 1:
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
    
    text = tess.image_to_string(tablica, config='--psm 11')
    # if (len(text.strip())<7):
    #     print("Nije detektovana tablica")
    #     return
    txt = re.sub('[\W_]+', '', text)
    print("Detektovana tablica je : ",txt[:7])
    print(len(txt[:7]))

    #cv.rectangle(img,((img.shape[1]//2),0), ((img.shape[1]), img.shape[0]//2), (0,0,255),thickness=2)
    cv.putText(img, txt[:7], (10,30), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv.putText(img, "Broj tablica koji je prepoznat", (10,45), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
    cv.putText(tablica, txt[:7]+" Broj tablice koji je prepoznat !", (10,30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv.imshow('Tablica',tablica)
    cv.imshow('Full Original detektovana',img)

def cropCetvrtina(img):
    cropCV_1 = img[0:(img.shape[0]//2), 0:(img.shape[1]//2)]
    cropCV_2 = img[(img.shape[0]//2):(img.shape[0]), (img.shape[1]//2):(img.shape[1])]
    cropCV_3 = img[(img.shape[0]//2):(img.shape[0]), 0:(img.shape[1]//2)]
    cropCV_4 = img[0:(img.shape[0]//2), (img.shape[1]//2):(img.shape[1])]
    cropCV_5 = img[0:(img.shape[0]), (img.shape[1]//2):(img.shape[1])]
    cropCV_6 = img[0:(img.shape[0]), 0:(img.shape[1]//2)]

    cv.rectangle(img,((img.shape[1]//2),0), ((img.shape[1]), img.shape[0]), (0,255,0),thickness=2)
    #cv.putText(img, "Polje za crop 1/4 slike", ((img.shape[1]//2)-110, (img.shape[0]//2)-10), cv.FONT_HERSHEY_PLAIN, 0.5, (0,255,0), 1)
    cv.imshow("crop1", cropCV_1)
    cv.imshow("crop2", cropCV_2)
    cv.imshow("crop3", cropCV_3)
    cv.imshow("crop4", cropCV_4)
    cv.imshow("crop5", cropCV_5)
    cv.imshow("crop6", cropCV_6)
    detektujTablicu(cropCV_1)
    detektujTablicu(cropCV_2)
    detektujTablicu(cropCV_4)
    detektujTablicu(cropCV_3)
    detektujTablicu(cropCV_5)
    detektujTablicu(cropCV_6)


img = cv.imread('images/tabla.jpg') ## UCITAVANJE SLIKE !
img = cv.resize(img, (600,300))
detektujTablicu(img)

## SPLIT SLIKU U DIJELOVE
#cropCetvrtina(img)


#detektujTablicu(img)
cv.waitKey(0)