import cv2 as OpenCV
import numpy as Numpy

def swapFaces(imageFace, imageBackground):
    #Code by Utsav Raj:
    #https://medium.com/@ccpvyn/creating-a-face-swapping-tool-with-opencv-and-python-4d64fc332de3
    face = OpenCV.imread(imageFace)
    background = OpenCV.imread(imageBackground)

    faceButGray = OpenCV.cvtColor(face, OpenCV.COLOR_BGR2GRAY)
    backgroundButGray = OpenCV.cvtColor(background, OpenCV.COLOR_BGR2GRAY)

    faceRecognition = OpenCV.CascadeClassifier(OpenCV.data.haarcascades + "haarcascade_frontalface_default.xml")
    faceDetected = faceRecognition.detectMultiScale(faceButGray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    backgroundDetected = faceRecognition.detectMultiScale(backgroundButGray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faceDetected) == 0 or len(backgroundDetected) == 0:
        print("No faces detected in one or both images.")
        return None

    face_x, face_y, faceWidth, faceHeight = faceDetected[0]
    background_x, background_y, backgroundWidth, backgroundHeight = backgroundDetected[0]

    faceRegionsOfInterest = face[face_y:face_y + faceHeight, face_x:face_x + faceWidth]
    backgroundRegionsOfInterest = background[background_y:background_y + backgroundHeight, background_x:background_x + backgroundWidth]

    model_path = "path/to/opencv_face_detector_uint8.pb"
    config_path = "path/to/opencv_face_detector.pbtxt"
    net = OpenCV.dnn.readNetFromTensorflow(model_path, config_path)
    blob = OpenCV.dnn.blobFromImage(backgroundRegionsOfInterest, 1.0, (300, 300), [104, 117, 123], False)
    net.setInput(blob)
    landmarks = net.forward()

    backgroundGuides = []
    for i in range(68):
        x = int(landmarks[0, 0, i, 0] * backgroundWidth) + background_x
        y = int(landmarks[0, 0, i, 1] * backgroundHeight) + background_y
        backgroundGuides.append((x, y))

    convexHullPoints = OpenCV.convexHull(np.array(backgroundGuides), returnPoints=True)
    convexHullMask = np.zeros(face.shape[:2], dtype=np.uint8)
    OpenCV.fillPoly(mask, [np.array(backgroundGuides)], 255)

    transformation_matrix, _ = OpenCV.estimateAffinePartial2D(np.array(backgroundGuides), np.array(faceDetected)[:,:2])
    warpedFace = OpenCV.warpAffine(faceRegionsOfInterest, transformation_matrix, (backgroundWidth, backgroundHeight))

    backgroundFaceMasked = OpenCV.bitwise_and(backgroundRegionsOfInterest, backgroundRegionsOfInterest, mask=mask)
    swappedFace = OpenCV.add(backgroundFaceMasked, warpedFace)

    background[background_y:background_y + backgroundHeight, background_x:background_x + backgroundWidth] = swappedFace
    return background
