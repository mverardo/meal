import cv
import cv2
import common
import numpy as np

#http://opencv-srf.blogspot.com.br/2010/09/filtering-images.html

#CHECAR ISSO AQUI!!!
#http://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html#cv2.floodFill

seedPoints = []
colors = [[255,0,0], [0,255,0], [0,0,255], [255, 255, 100], [255, 100, 255], [100, 255, 255], [0, 255, 100]]

# def lateFlood(img, seed, color):
#   crop = common.cropImage(img, seed)
#   lowBounds, highBounds = common.findBounds(crop, common.findZscore())
#   print("lowBounds = " + str(lowBounds))
#   print("highBounds = " + str(highBounds))
#   #cv.FloodFill(img, seed, color, cv.RGB(*lowBounds), cv.RGB(*highBounds), 4 + cv.CV_FLOODFILL_FIXED_RANGE)
#   cv2.floodFill(img, seed, color, cv2.RGB(*lowBounds), cv2.RGB(*highBounds), 4)
#   return img

def flood(srcImg, seed, color):
  h, w = srcImg.shape[:2]
  mask = np.zeros((h+2, w+2), np.uint8)
  crop = common.cropImage(srcImg, seed)
  lowBounds, highBounds = common.findBounds(crop)
  connectivity = 8
  flags = connectivity
  flags |= cv2.FLOODFILL_FIXED_RANGE
  cv2.floodFill(srcImg, mask, seed, color, lowBounds, highBounds, flags)
  # cv2.imshow("mask", mask)
  return srcImg

def preprocessImage(img):
    #cv2.imshow('floodfill', img)
    #cv2.waitKey()
    img = cv2.medianBlur(img, 13)
    cv2.imshow('floodfill', img)
    cv2.waitKey()
    img = cv2.dilate(img, np.ones((9,9),'int'))
    cv2.imshow('floodfill', img)
    cv2.waitKey()
    return img

def captureMousePosition(event, x, y, flags, nemIdeia):
  if flags == cv2.EVENT_FLAG_SHIFTKEY and event == cv2.EVENT_LBUTTONDOWN:
    print(x, y)
    return
  if event == cv2.EVENT_LBUTTONDOWN:
      if(len(seedPoints) < len(colors)):
            seedPoints.append((x,y))
            print(str((x, y)))
            color = colors[len(seedPoints)-1]
            cv2.circle(imgComPontos, (x,y), 10, color, -1)
            cv2.imshow("floodfill", imgComPontos)


img = cv2.imread("imagens/prato4.jpg")
img = cv2.resize(img, (800,600))

img = preprocessImage(img)
imgComPontos = img.copy()

cv2.imshow("floodfill", img)
cv2.setMouseCallback('floodfill', captureMousePosition)
cv2.waitKey(0)

for seed, color in zip(seedPoints, colors):
  print("Preenchendo o ponto "+ str(seed) + " com a cor " + str(color))
  # img = lateFlood(img, seed, color)
  img = flood(img, seed, color)

cv2.imshow("floodfill", img)
cv2.waitKey(0)
