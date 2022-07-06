import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.filters.rank import maximum, minimum
from skimage.morphology import rectangle

def normalizacao(img, m, n):
    min = minimum(img, rectangle(m, n))
    max = maximum(img, rectangle(m, n))
    return (255*((img-min)/(max-min+np.finfo(float).eps))).astype(np.uint8)


img = cv2.imread('img3.tif', 0)
#Alterar 'm' e 'n' para escolher as dimensões da vizinhança
m = 3
n = 3
img_n = normalizacao(img, m, n)
cv2.imshow('original', img)
cv2.imshow('normalizada', img_n)
cv2.waitKey(0)
cv2.destroyAllWindows()

