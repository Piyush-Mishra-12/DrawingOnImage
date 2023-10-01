import cv2
import glob
import easyocr
import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt

path = glob.glob("C:/Users/Piyush Mishra/Desktop/job/InputImage/*.jpg")

for n in path:
	read = easyocr.Reader(['en'])
	op = read.readtext(n)
	img_1 = cv2.imread(n)
	img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
	plt.imshow(img_1)

	img = cv2.imread(n)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   
	dpi = 80
	fig_width, fig_height = int(img.shape[0]/dpi), int(img.shape[1]/dpi)
	plt.figure()
	#f, axarr = plt.subplots(1,2, figsize=(fig_width, fig_height)) 
	#axarr[0].imshow(img)
	plt.imshow(img)
	result = read.readtext(n)

	for (bbox, text, prob) in result:
		print(f'Detected text: {text} (Probability: {prob:.2f})')

		(top_left, top_right, bottom_right, bottom_left) = bbox
		top_left = (int(top_left[0]), int(top_left[1]))
		bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
    	
		img = cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(255, 0, 0), thickness=1)
		img = cv2.putText(img=img, text=text, org=(top_left[0], top_left[1] - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=2)
	
	#axarr[1].imshow(img)
	plt.imshow(img)
	plt.savefig(f'overlay' + str(n) + '.jpg', bbox_inches='tight')
