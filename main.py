import numpy as np
from PIL import Image
import cv2
from matplotlib import pyplot as plt
import pytesseract
from subprocess import check_call

#Noise Reduction
img = cv2.imread('image3.jpg')
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
im = Image.fromarray(dst)
im.save("NReduced.jpg")

#Binarization on Noise Reduced Image
img = cv2.imread('NReduced.jpg',0)
ret,thresh_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#print ret
im = Image.fromarray(thresh_img)
im.save("BinZised.jpg")


#Create a hocr file named result.It contains co-ordinates of each word

tesseractParams = ['tesseract', 'BinZised.jpg', 'result', 'hocr']
check_call(tesseractParams)



#below is the code to extract and store position of each character
"""

# read the image and get the dimensions
img = cv2.imread(filename)
h, w, _ = img.shape # assumes color image

# run tesseract, returning the bounding boxes
boxes = pytesseract.image_to_boxes(img) # also include any config options you use
print(boxes)	print the rectangles around each character
# draw the bounding boxes on the image
for b in boxes.splitlines():
	b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

 #show annotated image and wait for keypress.Uncomment the below two lines to see the extracted characters
cv2.imshow(filename, img)
cv2.waitKey(0)

"""
def hocr_to_dataframe(fp):

    from lxml import etree
    import pandas as pd
    import os

    doc = etree.parse(fp)
    words = []
    wordConf = []

    for path in doc.xpath('//*'):
        if 'ocrx_word' in path.values():
            conf = [x for x in path.values() if 'x_wconf' in x][0]
            wordConf.append(int(conf.split('x_wconf ')[1]))
            words.append(path.text)

    dfReturn = pd.DataFrame({'word' : words,
                             'confidence' : wordConf})

    return(dfReturn)

x=open("result.hocr","r")
#print(hocr_to_dataframe(x))
x=hocr_to_dataframe(x)
ans={}
#print(x)
for index,a in x.iterrows():
    if(a["word"] in ans.keys()):
        ans[a["word"]].append(a["confidence"])
    else:
        z=[a["confidence"]]
        ans[a["word"]]=z
for i in ans:
    print(i,ans[i])