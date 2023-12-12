from graphics import *
from filedialog import *
import time
import sys
from sys import platform
import swapFaceImplementation as SFI

def main():
#   If you can find a way to import Pillow from macOS, please uncomment
#   the code down below.
    if (platform == "win32"):
        from PILWindows import Image
##      CURRENTLY UNAVAILABLE; PLEASE RUN ON WINDOWS SYSTEMS.
##    elif (platform == "darwin"):
##        from PILmacOS import Image
    else:
        print("DO NOT CONTINUE; IT IS TOO DANGEROUS HERE.")
        sys.exit(1)

    #These will change to true if both the images are accepted.
    proceed1 = False
    proceed2 = False

    #Creates a new interface Window with three boxes;
    #each box generates a prompt (will explain if you scroll down).
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
        #Gets the mouse coordinates when clicked in the window; Translates that to
        #the x-coordinate and y-coordinate for ease of access.
        point = interfaceWindow.getMouse()
        pointX = point.getX()
        pointY = point.getY()

        #Checks if the click is within the width range of the boxes;
        #two of thm are the same.
        if ((pointX<=900) & (pointX>=100)):
            if ((pointY<=200) & (pointY>=100)):
                #If there is already an image, undraw the reference to prepare for another reference;
                #then, ask for the file name, proceed to generate some text with the file path, and display
                #that file path.
                if (len(imageBackground)!=0):
                    imageBackgroundText.undraw()
                imageBackground = askopenfilename()
                imageBackgroundText = Text(Point(500,220), imageBackground)
                imageBackgroundText.draw(interfaceWindow)

            #This code does the same thing, but for the second image.
            elif ((pointY<=350) & (pointY>=250)):
                if (len(imageFace)!=0):
                    imageFaceText.undraw()
                imageFace = askopenfilename()
                imageFaceText = Text(Point(500,370), imageFace)
                imageFaceText.draw(interfaceWindow)

            #This is just to ensure a default case passes.
            else: time.sleep(0)

        #This one is a doozy; the reason the both of us used Python 3.11 is to use match-case;
        #the code basically checks if the images are in supported formats. If they are, then it'll
        #display the format types; otherwise, it will display an error message, and keep running through the loop
        #until the supported image types are selected. Currently, JPG, JPEG, and PNG images are supported.
        #Feel free to add in any supported formats; video was too much for us unfortunately.
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

    #Once the loop has successfully been exited, close the interface window.
    interfaceWindow.close()
#####################################################################

    #This calls in another method to basically swap the faces;
    #The print statement is due to the face that we basically stole that portion of code.
    swappedImage = SFI.swapFaces(imageFace, imageBackground)
    swappedImage.show()
    print("I'M NOT GIVING CREDIT TO SOMEONE THAT ALMOST MADE US PAY FOR THE SOURCE CODE; THAT IS DOWNRIGHT DESPICABLE.")
    
######################################################################

main()
