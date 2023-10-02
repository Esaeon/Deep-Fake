from PIL import Image

def main():
    imageFile = input("Please paste the image path location: ")
    imageOriginal = Image.open(imageFile)
    imageOriginal.show()

    imageFile2 = input("Please paste the image path location: ")
    imageOriginal2 = Image.open(imageFile2)
    imageOriginal2.show()


main()
