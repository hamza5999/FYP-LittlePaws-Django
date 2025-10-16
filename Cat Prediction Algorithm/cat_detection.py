import cv2
import numpy
import os
import time
face = cv2.CascadeClassifier("cat_features.xml")  # for detecting face

image = cv2.imread("dog.jpg")
mage = cv2.resize(image, (300, 200))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert into gray so color not effect accuracy

# parameters(img,scale_factor[reduce image size],min_neighbour)
faces = face.detectMultiScale(gray, 1.1, 1)  # for  faces
x_axis = 0
y_axis = 0
cat = False
for (x, y, w, h) in faces:
    cat = True
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 205), 3)
    x_axis = x + int(w/2)
    x_axis = x_axis - 10
    y_axis = y + int(h/2)
    y_axis = y_axis - 10


if cat:
    hue = [0,0,0]
    print(list)
    print("Cat Detected")
    image = cv2.rectangle(image, (x_axis, y_axis), (x_axis + 20, y_axis + 20), (127, 0, 205), 1)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cv2.imshow("Cat Detected", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    x_axis = x_axis + 10
    y_axis = y_axis
    xlimit = x_axis+20
    ylimit = y_axis+20
    for x in range(x_axis,xlimit):
        for y in range(y_axis,ylimit):
            pixel = hsv[x,y]
            H = pixel[0]
            S = pixel[1]
            V = int(pixel[2]/255) * 100
            if H<20:
                hue[1] = hue[1] + 1
            elif H>15 and V>60:
                hue[2] = hue[2] + 1
            elif S<2:
                hue[0] = hue[0] + 1
            else:
                hue[2] = hue[2] + 1
    print(hue)
    if hue[0]>hue[1] and hue[0]>hue[2]:
        color = "Black"
    elif hue[1]>hue[0] and hue[1]>hue[2]:
        color = "Brown"
    else:
        color = "White"
    print(color)
    time.sleep(5)
    dirPath = ""+color
    files = os.listdir(dirPath)
    for file in files:
        imagePath = os.path.join(dirPath, file)
        image = cv2.imread(imagePath, 1)
        image = cv2.resize(image, (600, 500))
        cv2.imshow("Images", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

else:
    print("Its not a Cat")