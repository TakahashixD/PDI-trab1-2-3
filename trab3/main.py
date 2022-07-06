import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.morphology import reconstruction


def preencherburacos(img):
    seed = img.copy()
    seed[1:-1, 1:-1] = img.max()
    mask = img
    selem = np.ones([3] * seed.ndim, dtype=int)
    preenchida = reconstruction(seed, mask, method='erosion', selem=selem)
    return preenchida

def limpezadebordas(img):
    seed = img.copy()
    seed[1:-1, 1:-1] = img.min()
    mask = img
    selem = np.ones([3] * seed.ndim, dtype=int)
    limpa = reconstruction(seed, mask, method='dilation', selem=selem)
    return img - limpa

img = cv2.imread('image.tif', 0)
cv2.imshow('original', img)
preenchida = preencherburacos(img)
limpa = limpezadebordas(img)
cv2.imshow('preenchida', preenchida)
cv2.imshow('bordas limpas', limpa)
cv2.waitKey(0)
cv2.destroyAllWindows()
