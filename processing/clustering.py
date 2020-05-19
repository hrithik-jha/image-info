import numpy as np
from scipy.cluster.hierarchy import fclusterdata
from os import walk
import cv2

path = "C:\\Users\\Abhay\\Desktop\\Image processing\\image-info\\data"

index = {}
images = {}
# A custom distance function
def distance(i, j):
    #print(i[0], j[0])
    #print(f[int(i[0])], f[int(j[0])])
    dist = cv2.compareHist(index[f[int(i[0])]], index[f[int(j[0])]], cv2.HISTCMP_CORREL)
    return max(-1*dist, 0)

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

dSet = []

for i in range(0, len(f)):
    buff = [i, 0]
    dSet.append(buff)

for imagePath in f:
    # extract the image filename (assumed to be unique) and
    # load the image, updating the images dictionary
    filename = imagePath
    image = cv2.imread(path + '\\' + imagePath)
    images[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #print(filename)
    # extract a 3D RGB color histogram from the image,
    # using 8 bins per channel, normalize, and update
    # the index
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    index[filename] = hist

print(dSet)
fclust = fclusterdata(dSet, 1.0, metric=distance)

print(fclust)