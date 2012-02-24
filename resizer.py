import Image
import os,sys
import ImageFilter

outputHeight = 500

nazwaPliku = raw_input("podaj nazwe plik\n")
obrazek = Image.open(nazwaPliku)
inputHeight = obrazek.size[1]
inputWidth = obrazek.size[0]
outputWidth = int(inputWidth * outputHeight / inputHeight)

obrazekModified = obrazek.resize((outputWidth, outputHeight),Image.BICUBIC)

nazwaPlikuZmienionego = raw_input("\npodaj nazwe pliku wyjsciowego\n")
obrazekModified.save(nazwaPlikuZmienionego, "JPEG")

"""
Mamy dany rozmiar wejsciowy (wysokosc i szerokos)
chcemy to przerobic na wysokosc = 500 i szerokosc = X
i zalezy nam zeby proporcje zostaly zachowane
Jak bedziemy wyliczac szerokosc nowego pluiku
"""
"""
2048 - 980 2048*x = 500*980
500 - X

4096*x = 1024 * 500


640x480
666  x500

640*500/480
x = 666px
 """