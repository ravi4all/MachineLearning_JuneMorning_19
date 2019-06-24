import cv2

img = cv2.imread('img_2.jpg', cv2.COLOR_BGR2GRAY)
print(img)
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    cv2.imshow('image', img)
    cv2.putText(img,"Kohli",(10,20),font,1,(255,255,0),1)
    cv2.rectangle(img, (100,40), (200,100),(255,255,255),2 )
    if cv2.waitKey(1) == 27:
        break