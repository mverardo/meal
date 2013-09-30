CROP_WIDTH = 64
CROP_HEIGHT = 64
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

def splitChannels(array):
    b = array[:,:,0]
    g = array[:,:,1]
    r = array[:,:,2]
    return [b, g, r]

def findBounds(crop):
  c = 1
  channels = splitChannels(crop)
  ranges = [[int((channel.max() - channel.min())/c), int((channel.max() - channel.min())/c)] for channel in channels]
  bounds = zip(*ranges)
  return bounds[0], bounds[1]