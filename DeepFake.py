from graphics import *
from filedialog import *
import time
import sys
from sys import platform
import swapFaceImplementation as SFI

def main():
    if (platform == "win32"):
        from PILWindows import Image
##                                  CURRENTLY UNAVAILABLE; PLEASE RUN ON WINDOWS SYSTEMS.
##    elif (platform == "darwin"):
##        from PILmacOS import Image
    else:
        print("DO NOT CONTINUE; IT IS TOO DANGEROUS HERE.")
        sys.exit(1)
    
    proceed1 = False
    proceed2 = False
    
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
    while (proceed1 == False & proceed2 == False):
        point = interfaceWindow.getMouse()
        pointX = point.getX()
        pointY = point.getY()

        if ((pointX<=900) & (pointX>=100)):
            if ((pointY<=200) & (pointY>=100)):
                if (len(imageBackground)!=0):
                    imageBackgroundText.undraw()
                imageBackground = askopenfilename()
                imageBackgroundText = Text(Point(500,220), imageBackground)
                imageBackgroundText.draw(interfaceWindow)

            elif ((pointY<=350) & (pointY>=250)):
                if (len(imageFace)!=0):
                    imageFaceText.undraw()
                imageFace = askopenfilename()
                imageFaceText = Text(Point(500,370), imageFace)
                imageFaceText.draw(interfaceWindow)

            else: time.sleep(0)

        if (((pointX<=700) & (pointX>=300))& ((pointY<=450) & (pointY>=400))):
            if ((len(imageBackground)!=0) & (len(imageFace)!=0)):
                AcceptedMessage = ""
                match ((imageBackground[(imageBackground.find(".")+1):]).upper()):
                    case "JPG":
                        AcceptedMessage += "JPG and "
                        proceed1 = True
                    case "JPEG":
                        AcceptedMessage += "JPEG and "
                        proceed1 = True
                    case "PNG":
                        AcceptedMessage += "PNG and "
                        proceed1 = True
                    case "TIFF":
                        ErrorMessage = "Currently an unknown image type; will possibly implement in the future."
                        ErrorMessageText = Text(Point(500, 470), ErrorMessage)
                        ErrorMessageText.draw(interfaceWindow)
                        time.sleep(3)
                        ErrorMessageText.undraw()
                        continue
                    case "PDF":
                        ErrorMessage = "PDFs could work, but you need to download the images;the program cannot currently download PDFs from the web."
                        ErrorMessageText = Text(Point(500, 470), ErrorMessage)
                        ErrorMessageText.draw(interfaceWindow)
                        time.sleep(3)
                        ErrorMessageText.undraw()
                        continue
                    case _:
                        ErrorMessage = "This is an unsupported file type."
                        ErrorMessageText = Text(Point(500, 470), ErrorMessage)
                        ErrorMessageText.draw(interfaceWindow)
                        time.sleep(3)
                        ErrorMessageText.undraw()
                        continue

                match ((imageFace[(imageFace.find(".")+1):]).upper()):
                    case "JPG":
                        AcceptedMessage += "JPG files selected."
                        proceed2 = True
                        AcceptedMessageText = Text(Point(500, 470), AcceptedMessage)
                        AcceptedMessageText.draw(interfaceWindow)
                        time.sleep(1)
                        AcceptedMessageText.undraw()
                    case "JPEG":
                        AcceptedMessage += "JPEG files selected."
                        proceed2 = True
                        AcceptedMessageText = Text(Point(500, 470), AcceptedMessage)
                        AcceptedMessageText.draw(interfaceWindow)
                        time.sleep(1)
                        AcceptedMessageText.undraw()
                    case "PNG":
                        AcceptedMessage += "PNG files selected."
                        proceed2 = True
                        AcceptedMessageText = Text(Point(500, 470), AcceptedMessage)
                        AcceptedMessageText.draw(interfaceWindow)
                        time.sleep(1)
                        AcceptedMessageText.undraw()
                    case "TIFF":
                        ErrorMessage = "Currently an unknown image type; will possibly implement in the future."
                        ErrorMessageText = Text(Point(500, 470), ErrorMessage)
                        ErrorMessageText.draw(interfaceWindow)
                        time.sleep(3)
                        ErrorMessageText.undraw()
                        continue
                    case "PDF":
                        ErrorMessage = "PDFs could work, but you need to download the images;the program cannot currently download PDFs from the web."
                        ErrorMessageText = Text(Point(500, 470), ErrorMessage)
                        ErrorMessageText.draw(interfaceWindow)
                        time.sleep(3)
                        ErrorMessageText.undraw()
                        continue
                    case _:
                        ErrorMessage = "This is an unsupported file type."
                        ErrorMessageText = Text(Point(500, 470), ErrorMessage)
                        ErrorMessageText.draw(interfaceWindow)
                        time.sleep(3)
                        ErrorMessageText.undraw()
                        continue
                
            else:
                ErrorMessage = "Please choose two files."
                ErrorMessageText = Text(Point(500, 470), ErrorMessage)
                ErrorMessageText.draw(interfaceWindow)
                time.sleep(5)
                ErrorMessageText.undraw()

    interfaceWindow.close()
#####################################################################
    imageWindow = GraphWin("Deep Fake v0.1.1 Sprint Demo", 700, 700)

    proceedText = Text(Point(350, 200), "Click here if this image is acceptable.")
    proceedRectangle = Rectangle(Point(100, 100), Point(600, 300))
    noProceedText = Text(Point(350,500), "Click here if either image is not acceptable;\nyou will need to run the program again.")
    noProceedRectangle = Rectangle(Point(100, 400), Point(600, 600))
    
    proceedText.draw(imageWindow)
    proceedRectangle.draw(imageWindow)
    noProceedText.draw(imageWindow)
    noProceedRectangle.draw(imageWindow)
    i = 0

    imageAlreadyOpen = False
    while (True):
        if (i == 0):
            imageToDraw = imageBackground
        elif (i == 1):
            imageToDraw = imageFace
        else:
            break
        if (imageAlreadyOpen == False):
            imageOpened = Image.open(imageToDraw)
            imageOpened.show()
            imageAlreadyOpen = True
        
        point = imageWindow.getMouse()
        pointX = point.getX()
        pointY = point.getY()

        print(point)
        if ((pointX<=600) & (pointX>=100)):
            if ((pointY<=300) & (pointY>=100)):
                imageOpened.close()
                i = i + 1
                imageAlreadyOpen = False
                continue
            elif ((pointY<=600) & (pointY>=400)):
                print("Either one of the images or both of the images were not accepted after being shown.\nTerminating program to not transmit the data over.")
                sys.exit(1)
            else:
                time.sleep(0)

    imageWindow.close()        
                
######################################################################
    print("Untested lmao")
    swappedImage = SFI.swapFaces(imageFace, imageBackground)
    
    
    
######################################################################

main()
