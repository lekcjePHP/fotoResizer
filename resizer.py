import Image
import os,sys
import ImageFilter
import Tkinter, tkFileDialog

def changeName(filePath):#filePath dostajemy z outputImagePath
	lastDot = filePath.rfind(".")#znalezienie ostatniej kropki
	filePath=filePath[:lastDot]#usuniecie wszystkiego za ta kropka i tej kropki tez
	filePath=filePath+"-resized.JPEG"#dodanie 
	return filePath

def scaleForTheGallery(imagePath, outputHeight):
	rawImage = Image.open(imagePath)
	inputHeight = rawImage.size[1]
	inputWidth = rawImage.size[0]
	outputWidth = int(inputWidth * outputHeight/inputHeight)
	outputImage = rawImage.resize((outputWidth, outputHeight),Image.BICUBIC)
	outputImagePath = changeName(imagePath)
	outputImage.save(outputImagePath, "JPEG")

root = Tkinter.Tk()

dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
filesList = os.listdir(dirname)

for fileName in filesList:
	imagePath = dirname+"/"+fileName
	scaleForTheGallery(imagePath, 3000)

