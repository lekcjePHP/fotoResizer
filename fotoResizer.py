import Image
import os

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton#uzywamy singletona aby nie towrzyc 2och obiektow tej samej klasy tu:fotoResize
class fotoResizer():
	def changeName(filePath):
		lastDot = filePath.rfind(".")#znalezienie ostatniej kropki
		filePath=filePath[:lastDot]#usuniecie wszystkiego za ta kropka i tej kropki tez
		filePath=filePath+"-resized.JPEG"#dodanie strina resizeJPEG
		return filePath

	def scale(imagePath, outputHeight):
		rawImage = Image.open(imagePath)
		inputHeight = rawImage.size[1]
		inputWidth = rawImage.size[0]
		outputWidth = int(inputWidth * outputHeight/inputHeight)
		outputImage = rawImage.resize((outputWidth, outputHeight),Image.BICUBIC)
		outputImagePath = self.changeName(imagePath)
		outputImage.save(outputImagePath, "JPEG")

	def scaleWholeCatalogue(dirname,height):
		filesList = os.listdir(dirname)
		for fileName in filesList:
			imagePath = dirname+"/"+fileName	
			self.scale(imagePath, height)

