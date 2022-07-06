import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('img2.jpg', 0)
paleta = plt.get_cmap('plasma')
paletaRGB = paleta(np.arange(256))

red = paletaRGB[:, 0] 
green = paletaRGB[:, 1] 
blue = paletaRGB[:, 2] 

imgRed = red[img] 
imgGreen = green[img] 
imgBlue = blue[img] 

imgColorida = np.dstack((imgBlue, imgGreen, imgRed))
cv2.imshow('original', img)
# # cv2.imshow('banda vermelha', imgRed)
# # cv2.imshow('banda verde', imgGreen)
# # cv2.imshow('banda azul', imgBlue)
cv2.imshow('pseudocolorida', imgColorida)
cv2.waitKey(0)
cv2.destroyAllWindows()






