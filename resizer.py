import Image
import os,sys
import ImageFilter
import Tkinter, tkFileDialog

def scaleForTheGallery(imagePath, outputHeight):
	rawImage = Image.open(imagePath)
	inputHeight = rawImage.size[1]
	inputWidth = rawImage.size[0]
	outputWidth = int(inputWidth * outputHeight/inputHeight)
	outputImage = rawImage.resize((outputWidth, outputHeight),Image.BICUBIC)
	outputImagePath = "res"+imagePath
	outputImage.save(outputImagePath, "JPEG")

root = Tkinter.Tk()

dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
filesList = os.listdir(dirname)

for fileName in filesList:
	imagePath = dirname+"/"+fileName
	scaleForTheGallery(imagePath, 500)

