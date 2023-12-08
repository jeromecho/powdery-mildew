import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from os import listdir

def show_img(img):
  plt.axis('off')
  plt.imshow(img)
  plt.show()

# MUTATES
def color_convert(img):
  im_lab = cv.cvtColor(im, cv.COLOR_BGR2HSV)
  im_normalized = normalize_lightness(im_lab)
  return im_normalized

# MUTATES
def normalize_lightness(img):
    for row in img:
      for cell in row:
        cell[1] = 50
        cell[2] = 50
    return img

for im_path in listdir('./test'):
    rel_path = './test/' + im_path
    im = cv.imread(rel_path)
    color_cvtd_im = color_convert(im)
    show_img(color_cvtd_im)

"""
1. Build a LAB sampler that lets you get LAB values at a point
2. Try to set a threshold that lets you detect powdery mildew, and that adds t
   results array a value that is 'true' or 'false' based on whether powdery mildew
   classificaiton worked out
"""




