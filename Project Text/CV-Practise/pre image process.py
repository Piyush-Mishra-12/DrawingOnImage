import cv2
import numpy as ny
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

path = r"D:\\Study\\python\\CV Practise\\Class 5.jepg"
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


sobelx = cv2.Sobel(img,-1,1,0)
sobely = cv2.Sobel(sobelx,-1,0,1)
sobel = cv2.Sobel(img,-1,1,1)
sobelxy = cv2.addWeighted(sobelx,1,sobely,0.5,0)
lap = cv2.Laplacian(sobelxy,-1)

words_in_image = pytesseract.image_to_string(sobelxy)

print(words_in_image)

cv2.imshow('orignal',img)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.imshow('sobelxy',sobelxy)
cv2.imshow('lap',lap)
cv2.waitKey(2)==27