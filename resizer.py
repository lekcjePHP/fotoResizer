import Image
import os,sys
import ImageFilter

nazwaPliku = raw_input("podaj nazwe plik\n")
obrazek = Image.open(nazwaPliku)

obrazekModified = obrazek.resize((500,500),Image.BICUBIC)

nazwaPlikuZmienionego = raw_input("\npodaj nazwe pliku wyjsciowego\n")
obrazekModified.save(nazwaPlikuZmienionego, "JPEG")
