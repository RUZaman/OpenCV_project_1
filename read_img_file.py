import cv2

img=cv2.imread('image2.png')

img=cv2.line(img,(0,0),(100,100),(250,0,0),10)
img=cv2.circle(img,(150,150),60,(250,0,0),15)
img=cv2.rectangle(img,(150,150),(400,400),(0,200,250),10)
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print("shapee of color img " )
print(img.shape)

img2=img.copy()
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


print("shapee of grray scale " )
print(img.shape)

blurImg=cv2.blur(img2,(15,15))
cannyIm=cv2.Canny(img2,83,85)
print("shapee of canny  img " )
print(cannyIm.shape)
dialate=cv2.dilate(cannyIm,(15,15))
erod=cv2.erode(cannyIm,(15,15))
print("shapee of erod  img " )
print(erod.shape)


cv2.imshow("gray",img)
cv2.imshow("color",img2)
cv2.imshow("blurr",blurImg)
cv2.imshow("cannyIm",cannyIm)
cv2.imshow("dialate",dialate)
cv2.imshow("erod",erod)



cv2.waitKey(0)

