import cv
import cv2
import sys
import numpy as np
import math
from cv import *

CROP_WIDTH = 32
CROP_HEIGHT = 32
DEBUG = True

def cropImage(img, point):
    x = point[0] - (CROP_WIDTH / 2)
    y = point[1] - (CROP_HEIGHT / 2)
    if DEBUG == True:
      print("Coordenadas do CROP: ")
      print("(y:" + str(y) + ", x:" + str(x) + ")")
      print("[" + str(y) + ":" + str(y+CROP_HEIGHT) + "," + str(x) + ":" + str(x+CROP_WIDTH) + "]")
    result = img[y:(y+CROP_HEIGHT), x:(x+CROP_WIDTH)]
    return result

def findBounds(crop):
  return (20,20,20), (20,20,20)


# def cv2array(im):
#   depth2dtype = {
#         cv.IPL_DEPTH_8U: 'uint8',
#         cv.IPL_DEPTH_8S: 'int8',
#         cv.IPL_DEPTH_16U: 'uint16',
#         cv.IPL_DEPTH_16S: 'int16',
#         cv.IPL_DEPTH_32S: 'int32',
#         cv.IPL_DEPTH_32F: 'float32',
#         cv.IPL_DEPTH_64F: 'float64',
#     }

#   arrdtype=im.depth
#   a = np.fromstring(
#          im.tostring(),
#          dtype=depth2dtype[im.depth],
#          count=im.width*im.height*im.nChannels)
#   a.shape = (im.height,im.width,im.nChannels)
#   return a

# def array2cv(a):
#   dtype2depth = {
#         'uint8':   cv.IPL_DEPTH_8U,
#         'int8':    cv.IPL_DEPTH_8S,
#         'uint16':  cv.IPL_DEPTH_16U,
#         'int16':   cv.IPL_DEPTH_16S,
#         'int32':   cv.IPL_DEPTH_32S,
#         'float32': cv.IPL_DEPTH_32F,
#         'float64': cv.IPL_DEPTH_64F,
#     }
#   try:
#     nChannels = a.shape[2]
#   except:
#     nChannels = 1
#   cv_im = cv.CreateImageHeader((a.shape[1],a.shape[0]),
#           dtype2depth[str(a.dtype)],
#           nChannels)
#   cv.SetData(cv_im, a.tostring(),
#              a.dtype.itemsize*nChannels*a.shape[1])
#   return cv_im

# def findImagePath():
#     imgPath = "bife_sem_prato.jpg"
#     if (len(sys.argv) > 1):
#         imgPath = sys.argv[1]
#     print imgPath
#     return imgPath

# def findZscore():
#   zscore = 1
#   if(len(sys.argv) > 2):
#        zscore = sys.argv[2]
#   print "zscore = " + str(zscore)
#   return float(zscore)

# #whites.append(len(filter(lambda (x): x[0] == 255, ar[row]))

# def findMaxWidth(img, delta):
#   ar = cv2array(img)
#   rowWhites = []
#   for row in range(len(ar)):
#     whites = sum(ar[row] == 255)[0]
#     rowWhites.append(whites)
#   return np.array(whites).max()

# def split(array):
#     b = array[:,:,0]
#     g = array[:,:,1]
#     r = array[:,:,2]
#     return b, g, r

# def findColorBounds(chanel, zscore):
#   #hist = np.histogram(chanel, 255, (0, 255))[0]
#   #histMaxIndex = hist.argmax()
#   #mean = np.mean(chanel)
#   sigma = np.std(chanel)
#   newSigma = zscore * sigma
#   return newSigma, newSigma
#   # smoothedHist = np.array(map(lambda (x): x-5 if (x-5) > 0 else 0, hist))
#   #smoothedHist = hist

#   #Primeiro valor do histograma que nao deu 0
#   # first = next((i for i, x in enumerate(smoothedHist) if x != 0))
  
#   # #histograma invertido
#   # reversedHist = smoothedHist[::-1]

#   # #Ultimo valor do histograma que nao deu 0
#   # last = (len(hist) -1) - next((i for i, x in enumerate(reversedHist) if x != 0))

#   # #Indice do maior valor do histograma
#   # histMax = smoothedHist.argmax()
#   # lowerBound = histMax - first
#   # upperBound = last - histMax

#   # if(lowerBound < upperBound):
#   #   return lowerBound, lowerBound
#   # else:
#   #   return upperBound, upperBound

#   #return lowerBound, upperBound


# def findBounds(crop, zscore):
#     ar = cv2array(crop)
#     b,g,r = split(ar)
#     bbounds = findColorBounds(b, zscore)
#     gbounds = findColorBounds(g, zscore)
#     rbounds = findColorBounds(r, zscore)

#     return zip(bbounds, gbounds, rbounds)
