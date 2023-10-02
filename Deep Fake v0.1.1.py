from PIL import Image
from graphics import *

def main():
    interfaceWindow = GraphWin("Deep Fake v0.1.1", 1000, 500)
    imageChooser1 = Rectangle(Point(100, 100), Point(900, 200))
    imageChooser1.draw(interfaceWindow)

    imageText1 = Text(Point(500, 150), "Choose The Image To Be The Background")
    imageText1.draw(interfaceWindow)

    imageChooser2 = Rectangle(Point(100, 250), Point(900, 350))
    imageChooser2.draw(interfaceWindow)

    imageText2 = Text(Point(500, 300), "Choose The Image Representing the Face Itself")
    imageText2.draw(interfaceWindow)

    proceedRec = Rectangle(Point(300, 400), Point(700, 450))
    proceedRec.draw(interfaceWindow)
    proceedText = Text(Point(500, 425), "Proceed")
    proceedText.draw(interfaceWindow)
    
##    imageFile = input("Please paste the image path location: ")
##    imageOriginal = Image.open(imageFile)
##
##    imageFile2 = input("Please paste the image path location: ")
##    imageOriginal2 = Image.open(imageFile2)
    


main()
