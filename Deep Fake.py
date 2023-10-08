from graphics import *
from filedialog import *
import time

def main():
    proceed = False
    
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

    imageBackground = ""
    imageFace = ""
    while (proceed == False):
        point = interfaceWindow.getMouse()
        pointX = point.getX()
        pointY = point.getY()
        print(point)

        if ((pointX<900) & (pointX>100)):
            if ((pointY<200) & (pointY>100)):
                if (len(imageBackground)!=0):
                    imageBackgroundText.undraw()
                imageBackground = askopenfilename()
                imageBackgroundText = Text(Point(500,220), imageBackground)
                imageBackgroundText.draw(interfaceWindow)

            elif ((pointY<350) & (pointY>250)):
                if (len(imageFace)!=0):
                    imageFaceText.undraw()
                imageFace = askopenfilename()
                imageFaceText = Text(Point(500,370), imageFace)
                imageFaceText.draw(interfaceWindow)

            else: time.sleep(1)

        if (((pointX<700) & (pointX>300))& ((pointY<450) & (pointY>400))):
            if ((len(imageBackground)!=0) & (len(imageFace)!=0)):
                if (imageBackground.endswith("JPG") & imageFace.endswith("JPG")):
                    proceed = True
                else:
                    ErrorMessage = "Files other than JPG are not supported in this iteration."
                    ErrorMessageText = Text(Point(500, 470), ErrorMessage)
                    ErrorMessageText.draw(interfaceWindow)
                    time.sleep(5)
                    ErrorMessageText.undraw()
                
            else:
                ErrorMessage = "Please choose two files."
                ErrorMessageText = Text(Point(500, 470), ErrorMessage)
                ErrorMessageText.draw(interfaceWindow)
                time.sleep(5)
                ErrorMessageText.undraw()

    interfaceWindow.close()
    


main()
