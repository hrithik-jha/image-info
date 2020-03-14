# import the necessary packages
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
from os import walk

# initialize the index dictionary to store the image name
# and corresponding histograms and the images dictionary
# to store the images themselves
index = {}
images = {}

path = "C:\\Users\\Hrithik Jha\\image-info\\video-extraction\\data"

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

print(f)

# loop over the image paths
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

results = {}
reverse = True
methodName = 'Correlation'

# loop over the index
for (k, hist) in index.items():
	# compute the distance between the two histograms
	# using the method and update the results dictionary
	d = cv2.compareHist(index["frame1450.jpg"], hist, cv2.HISTCMP_CORREL)
	results[k] = d
# sort the results
results = sorted([(v, k) for (k, v) in results.items()], reverse = reverse)
print(results)
#print(images)

# show the query image
fig = plt.figure("Query")
ax = fig.add_subplot(1, 1, 1)
ax.imshow(images['frame1450.jpg'])
plt.axis("off")
# initialize the results figure
fig = plt.figure("Results: %s" % (methodName))
# fig.suptitle(methodName, fontsize = 20)
# loop over the results
'''
for (i, (v, k)) in enumerate(results[0:10]):
	# show the result
    ax = fig.add_subplot(1, len(images), i + 1)
    # ax.set_title("%s: %.2f" % (k, v))
    plt.figure(figsize = (20,20))
    plt.imshow(images[k])    
    
    plt.axis("off")
# show the OpenCV methods
plt.show()
'''