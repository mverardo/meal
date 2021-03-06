#coding: utf-8

import cv2
import common
import numpy as np

#http://opencv-srf.blogspot.com.br/2010/09/filtering-images.html

#CHECAR ISSO AQUI!!!
#http://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html#cv2.floodFill

seedPoints = []
colors = [[255,0,0], [0,255,0], [0,0,255], [255, 255, 100], [255, 100, 255], [100, 255, 255], [0, 255, 100]]

masks = []

# def lateFlood(img, seed, color):
#   crop = common.cropImage(img, seed)
#   lowBounds, highBounds = common.findBounds(crop, common.findZscore())
#   print("lowBounds = " + str(lowBounds))
#   print("highBounds = " + str(highBounds))
#   #cv.FloodFill(img, seed, color, cv.RGB(*lowBounds), cv.RGB(*highBounds), 4 + cv.CV_FLOODFILL_FIXED_RANGE)
#   cv2.floodFill(img, seed, color, cv2.RGB(*lowBounds), cv2.RGB(*highBounds), 4)
#   return img

def preprocessImage(img):
    #cv2.imshow('floodfill', img)
    #cv2.waitKey()
    img = cv2.medianBlur(img, 33)
    cv2.imshow('floodfill', img)
    cv2.waitKey()

    img = cv2.dilate(img, np.ones((51,51),'int'))
    cv2.imshow('floodfill', img)
    cv2.waitKey()
    img = cv2.erode(img, np.ones((51,51),'int'))
    cv2.imshow('floodfill', img)
    cv2.waitKey()

    img = cv2.medianBlur(img, 33)
    # cv2.imshow('floodfill', img)
    # cv2.waitKey()

    return img

def flood(srcImg, seed, color):
  h, w = srcImg.shape[:2]
  mask = np.zeros((h+2, w+2), np.uint8)
  crop = common.cropImage(srcImg, seed)
  lowBounds, highBounds = common.findBounds(crop)
  connectivity = 8
  flags = connectivity
  flags |= cv2.FLOODFILL_FIXED_RANGE
  flags |= cv2.FLOODFILL_MASK_ONLY
  cv2.floodFill(srcImg, mask=mask, seedPoint=seed, newVal=color, loDiff=lowBounds, upDiff=highBounds, flags=flags)
  # cv2.imshow("mask", mask)
  return srcImg, mask

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

def segmentImage(img, mask):
  h, w = img.shape[:2]
  result = img.copy()
  for i in range(h):
    for j in range(w):
      if mask[i][j] == 0:
        result[i][j] = 0
  return result



img = cv2.imread("imagens/prato4.jpg")
img = cv2.resize(img, (800,600))
imgOriginal = img.copy()

img = preprocessImage(img)
imgComPontos = img.copy()

cv2.imshow("floodfill", img)
cv2.setMouseCallback('floodfill', captureMousePosition)
#good seeds for prato4.jpg
# (354, 467)
# (308, 258)
# (531, 289)
# seedPoints.append((308, 258))
# seedPoints.append((355, 474))
# seedPoints.append((538, 294))

cv2.waitKey(0)

for seed, color in zip(seedPoints, colors):
  print("Preenchendo o ponto "+ str(seed) + " com a cor " + str(color))
  # img = lateFlood(img, seed, color)
  img, mask = flood(img, seed, color)
  masks.append(mask)

for i in range(len(masks)):
  #Pra mostrar a foto, tenho que multiplicar por 255, pq a mascara fica com 1 nos lugares selecionados. Como a imagem não é binária, não dá pra ver.  
  # cv2.imshow(str(i), masks[i] * 255)
  cv2.imshow(str(i), segmentImage(imgOriginal, masks[i]))

cv2.waitKey()
