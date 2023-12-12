#This part of the program requires OpenCV, Numpy,
#and dLib in order to run; import all of that. We also need to translate
#the image back into Pillow so that it can be displayed.
import cv2 as OpenCV
import numpy as Numpy
import dlib
import time
import sys
from sys import platform
if (platform == "win32"):
    from PILWindows import Image
##                                  CURRENTLY UNAVAILABLE; PLEASE RUN ON WINDOWS SYSTEMS.
##    elif (platform == "darwin"):
##        from PILmacOS import Image
else:
    print("DO NOT CONTINUE; IT IS TOO DANGEROUS HERE.")
    sys.exit(1)


#Not exactly sure what this does in terms of the big picture; don't touch. I REPEAT: DO. NOT. TOUCH.
def extract_index_nparray(nparray):
    index = None
    for num in nparray[0]:
        index = num
        break
    return index

def swapFaces(imageFace, imageBackground):
    #Grabs both of the faces from the previous program, and
    #creates gray images along with a mask.
    img = OpenCV.imread(imageFace)
    img_gray = OpenCV.cvtColor(img, OpenCV.COLOR_BGR2GRAY)
    mask = Numpy.zeros_like(img_gray)
    img2 = OpenCV.imread(imageBackground)
    img2_gray = OpenCV.cvtColor(img2, OpenCV.COLOR_BGR2GRAY)


    #This portion is the part where we get the face shape.
    #It's not the most robust, but it works.
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    height, width, channels = img2.shape
    img2_new_face = Numpy.zeros((height, width, channels), Numpy.uint8)




    # THIS IS ALL FOR ONE FACE.
    faces = detector(img_gray)
    for face in faces:
        #Sets down the points for the face to help with
        #transforming the face.
        landmarks = predictor(img_gray, face)
        landmarks_points = []
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            landmarks_points.append((x, y))


        #Grab the points from the landmarks set on top of the face,
        #and create...something; we don't recommend touching this bit either.
        points = Numpy.array(landmarks_points, Numpy.int32)
        convexhull = OpenCV.convexHull(points)
        OpenCV.polylines(img, [convexhull], True, (255, 0, 0), 3)
        OpenCV.fillConvexPoly(mask, convexhull, 255)

        face_image_1 = OpenCV.bitwise_and(img, img, mask=mask)

        # The Delaunay Triangulation is needed to help create triangles
        # to map out the facial features.
        rect = OpenCV.boundingRect(convexhull)
        subdiv = OpenCV.Subdiv2D(rect)
        subdiv.insert(landmarks_points)
        triangles = subdiv.getTriangleList()
        triangles = Numpy.array(triangles, dtype=Numpy.int32)

        #This part makes the triangles for the first face.
        indexes_triangles = []
        for t in triangles:
            pt1 = (t[0], t[1])
            pt2 = (t[2], t[3])
            pt3 = (t[4], t[5])


            index_pt1 = Numpy.where((points == pt1).all(axis=1))
            index_pt1 = extract_index_nparray(index_pt1)

            index_pt2 = Numpy.where((points == pt2).all(axis=1))
            index_pt2 = extract_index_nparray(index_pt2)

            index_pt3 = Numpy.where((points == pt3).all(axis=1))
            index_pt3 = extract_index_nparray(index_pt3)

            if index_pt1 is not None and index_pt2 is not None and index_pt3 is not None:
                triangle = [index_pt1, index_pt2, index_pt3]
                indexes_triangles.append(triangle)



    # This is for the second face.
    faces2 = detector(img2_gray)
    for face in faces2:
        landmarks = predictor(img2_gray, face)
        landmarks_points2 = []
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            landmarks_points2.append((x, y))


        points2 = Numpy.array(landmarks_points2, Numpy.int32)
        convexhull2 = OpenCV.convexHull(points2)

    lines_space_mask = Numpy.zeros_like(img_gray)
    lines_space_new_face = Numpy.zeros_like(img2)
    
    # Triangulation of both faces
    for triangle_index in indexes_triangles:
        # Triangulation of the first face (whatever this means)
        tr1_pt1 = landmarks_points[triangle_index[0]]
        tr1_pt2 = landmarks_points[triangle_index[1]]
        tr1_pt3 = landmarks_points[triangle_index[2]]
        triangle1 = Numpy.array([tr1_pt1, tr1_pt2, tr1_pt3], Numpy.int32)


        rect1 = OpenCV.boundingRect(triangle1)
        (x, y, w, h) = rect1
        cropped_triangle = img[y: y + h, x: x + w]
        cropped_tr1_mask = Numpy.zeros((h, w), Numpy.uint8)


        points = Numpy.array([[tr1_pt1[0] - x, tr1_pt1[1] - y],
                           [tr1_pt2[0] - x, tr1_pt2[1] - y],
                           [tr1_pt3[0] - x, tr1_pt3[1] - y]], Numpy.int32)

        OpenCV.fillConvexPoly(cropped_tr1_mask, points, 255)

        # Lines space
        OpenCV.line(lines_space_mask, tr1_pt1, tr1_pt2, 255)
        OpenCV.line(lines_space_mask, tr1_pt2, tr1_pt3, 255)
        OpenCV.line(lines_space_mask, tr1_pt1, tr1_pt3, 255)
        lines_space = OpenCV.bitwise_and(img, img, mask=lines_space_mask)

        # Triangulation of second face (no clue what this means either)
        tr2_pt1 = landmarks_points2[triangle_index[0]]
        tr2_pt2 = landmarks_points2[triangle_index[1]]
        tr2_pt3 = landmarks_points2[triangle_index[2]]
        triangle2 = Numpy.array([tr2_pt1, tr2_pt2, tr2_pt3], Numpy.int32)


        rect2 = OpenCV.boundingRect(triangle2)
        (x, y, w, h) = rect2

        cropped_tr2_mask = Numpy.zeros((h, w), Numpy.uint8)

        points2 = Numpy.array([[tr2_pt1[0] - x, tr2_pt1[1] - y],
                            [tr2_pt2[0] - x, tr2_pt2[1] - y],
                            [tr2_pt3[0] - x, tr2_pt3[1] - y]], Numpy.int32)

        OpenCV.fillConvexPoly(cropped_tr2_mask, points2, 255)

        # Warp triangles
        points = Numpy.float32(points)
        points2 = Numpy.float32(points2)
        M = OpenCV.getAffineTransform(points, points2)
        warped_triangle = OpenCV.warpAffine(cropped_triangle, M, (w, h))
        warped_triangle = OpenCV.bitwise_and(warped_triangle, warped_triangle, mask=cropped_tr2_mask)

        # This portion of code below reconstructs the face to replace onto the destination face
        img2_new_face_rect_area = img2_new_face[y: y + h, x: x + w]
        img2_new_face_rect_area_gray = OpenCV.cvtColor(img2_new_face_rect_area, OpenCV.COLOR_BGR2GRAY)
        _, mask_triangles_designed = OpenCV.threshold(img2_new_face_rect_area_gray, 1, 255, OpenCV.THRESH_BINARY_INV)
        warped_triangle = OpenCV.bitwise_and(warped_triangle, warped_triangle, mask=mask_triangles_designed)

        img2_new_face_rect_area = OpenCV.add(img2_new_face_rect_area, warped_triangle)
        img2_new_face[y: y + h, x: x + w] = img2_new_face_rect_area



    # Once this section has run, all the code has been executed.
    img2_face_mask = Numpy.zeros_like(img2_gray)
    img2_head_mask = OpenCV.fillConvexPoly(img2_face_mask, convexhull2, 255)
    img2_face_mask = OpenCV.bitwise_not(img2_head_mask)


    img2_head_noface = OpenCV.bitwise_and(img2, img2, mask=img2_face_mask)
    result = OpenCV.add(img2_head_noface, img2_new_face)

    (x, y, w, h) = OpenCV.boundingRect(convexhull2)
    center_face2 = (int((x + x + w) / 2), int((y + y + h) / 2))

    #This section is actually ours.
    #Convert into Pillow image, and send back to the original caller.
    seamlesscloneImage = OpenCV.seamlessClone(result, img2, img2_head_mask, center_face2, OpenCV.NORMAL_CLONE)
    conversionPart1 = OpenCV.cvtColor(seamlesscloneImage, OpenCV.COLOR_BGR2RGB)
    conversionPart2 = Image.fromarray(conversionPart1)
    return conversionPart2
