# LicencePlate-Scanner-OpenCV
## Simple Car Licence Plate Scanner

# Requirements

```
    pip install --upgrade pip
    pip install opencv-contrib-python
    pip install caer
    pip install pytesseract
    pip install imutils
```

Ako koristite VS Code dodajte ovu liniju
```
    "python.linting.pylintArgs": ["--generate-members"]
```
u (Ctrl+Shift+P) -> Preferences: Open Settings (JSON), kao što je prikazano ispod:
```
    {
        "workbench.colorTheme": "Default Light+",
        "workbench.editorAssociations": [
            {
                "viewType": "jupyter.notebook.ipynb",
                "filenamePattern": "*.ipynb"
            }
        ],
        "python.linting.pylintArgs": ["--generate-members"]
    }
```

Testiranja detekcije na slikama sa interneta:

Ovdje vidimo da se tablica ne prepoznaje, već neki drugi rectangle:
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_3.png?raw=true)

Šta možemo uraditi da se ispravi detekcija? Prva stvar koja mi je pala na pamet je uzimanje manjeg polja na kojem će se provjera tj. detekcija vršiti, tako sam u Paintu smanjio polje pretrage na istoj slici i rezultati su se poboljšali:
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_8.png?raw=true)

Također ista stvar se desila na još primjera:
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_6.png?raw=true)
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_7.png?raw=true)

A neke su iz prvog pokušaja detektovane jer polje pretrage nema puno kontura:
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_1.png?raw=true)
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_4.png?raw=true)
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_5.png?raw=true)

** Dodan algoritam koji odabranu sliku siječe u kvadrante i olakšava detekciju registarske oznake**

![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_10.png?raw=true)
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_9.png?raw=true)

Također dodao sam i sječenje slike u dva dijela po pola slike!

## Finalni proizvod izgleda otprilike ovako:
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_11.png?raw=true)
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_12.png?raw=true)
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_13.png?raw=true)
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_14.png?raw=true)
![alt text](https://github.com/g1sha/LicencePlate-Scanner-OpenCV/blob/main/screenshots/Screenshot_15.png?raw=true)
